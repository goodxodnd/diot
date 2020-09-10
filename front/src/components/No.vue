<template>
	<!--
		SweetModal for Vue.js
		Sweet, easy and powerful modals and dialogs
		Copyright (c) 2017 Adepto.as AS · Oslo, Norway
		Dual licensed under the MIT and GPL licenses.
		See LICENSE-MIT.txt and LICENSE-GPL.txt
	-->
	<div :class="overlay_classes" v-show="is_open" v-on:click="_onOverlayClick">
		<div :class="modal_classes" :style="modal_style">
			<div class="sweet-box-actions">
				<!-- Custom Actions -->
				<slot name="box-action"></slot>

				<!-- Close Button -->
				<div class="sweet-action-close" v-on:click="close" v-if="!hideCloseButton">
					<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z" fill="#292c34" /></svg>
				</div>
			</div>

			<!-- Title: Housing the title and tabs, if no title is present -->
			<div class="sweet-title" v-if="has_title || has_tabs">
				<!-- Tabs but no title -->
				<template v-if="has_tabs && !has_title">
					<ul class="sweet-modal-tabs">
						<li v-for="tab in tabs" :class="_getClassesForTab(tab)">
							<a href="#" v-on:click.prevent="_changeTab(tab)">
								<div class="sweet-modal-valign">
									<span v-if="tab.icon" v-html="tab.icon" class="sweet-modal-tab-icon" />
									<span class="sweet-modal-tab-title">{{ tab.title }}</span>
								</div>
							</a>
						</li>
					</ul>
				</template>

				<!-- Title -->
				<template v-if="has_title">
					<h2 v-if="title" v-html="title"></h2>
					<slot name="title"></slot>
				</template>
			</div>

			<!-- Tabs: If title AND tabs are present -->
			<ul class="sweet-modal-tabs" v-if="has_title && has_tabs">
				<li v-for="tab in tabs" :class="_getClassesForTab(tab)">
					<a href="#" v-on:click.prevent="_changeTab(tab)">
						<div class="sweet-modal-valign">
							<span v-if="tab.icon" v-html="tab.icon" class="sweet-modal-tab-icon" />
							<span class="sweet-modal-tab-title">{{ tab.title }}</span>
						</div>
					</a>
				</li>
			</ul>

			<!-- Content: Wrapper -->
			<div class="sweet-content" ref="content">
				<!-- Icon: Error -->
				<div class="sweet-modal-icon sweet-modal-error" v-if="icon == 'error'" ref="icon_error">
					<span class="sweet-modal-x-mark">
						<span class="sweet-modal-line sweet-modal-left"></span>
						<span class="sweet-modal-line sweet-modal-right"></span>
					</span>
				</div>

				<!-- Icon: Warning -->
				<div class="sweet-modal-icon sweet-modal-warning" v-if="icon == 'warning'" ref="icon_warning">
					<span class="sweet-modal-body"></span>
					<span class="sweet-modal-dot"></span>
				</div>

				<!-- Icon: Info -->
				<div class="sweet-modal-icon sweet-modal-info" v-if="icon == 'info'" ref="icon_info"></div>

				<!-- Icon: Success -->
				<div class="sweet-modal-icon sweet-modal-success" v-if="icon == 'success'" ref="icon_success">
					<span class="sweet-modal-line sweet-modal-tip"></span>
					<span class="sweet-modal-line sweet-modal-long"></span>
					<div class="sweet-modal-placeholder"></div>
					<div class="sweet-modal-fix"></div>
				</div>

				<!-- Actual Content -->
				<div class="sweet-content-content" v-if="$slots.default">
					<slot></slot>
				</div>
			</div>

			<!-- Buttons -->
			<div class="sweet-buttons" v-if="$slots.button">
				<slot name="button"></slot>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'SweetModal',
		props: {
			title: {
				type: String,
				required: false,
				default: ''
			},
			overlayTheme: {
				type: String,
				required: false,
				default: 'light'
			},
			modalTheme: {
				type: String,
				required: false,
				default: 'light'
			},
			blocking: {
				type: Boolean,
				required: false,
				default: false
			},
			pulseOnBlock: {
				type: Boolean,
				required: false,
				default: true
			},
			icon: {
				type: String,
				required: false,
				default: ''
			},
			hideCloseButton: {
				type: Boolean,
				required: false,
				default: false
			},
			enableMobileFullscreen: {
				type: Boolean,
				required: false,
				default: true
			},
			width: {
				type: [Number, String],
				required: false,
				default: null
			}
		},
		mounted() {
			this.tabs = this.$children.filter(c => c.cmpName && c.cmpName == 'tab')
			if (this.has_tabs) {
				this.currentTab = this._changeTab(this.tabs[0])
			}
			document.addEventListener('keyup', this._onDocumentKeyup)
		},
		beforeDestroy() {
			this._unlockBody()
			document.removeEventListener('keyup', this._onDocumentKeyup)
		},
		data() {
			return {
				visible: false,
				is_open: false,
				is_bouncing: false,
				tabs: [],
				backups: {
					body: {
						height: null,
						overflow: null
					}
				}
			}
		},
		computed: {
			has_title() {
				return this.title || this.$slots.title
			},
			has_tabs() {
				return this.tabs.length > 0
			},
			has_content() {
				return this.$slots.default
			},
			current_tab() {
				return this.tabs.filter(t => t.active === true)[0]
			},
			overlay_classes() {
				return [
					'sweet-modal-overlay',
					'theme-' + this.overlayTheme,
					'sweet-modal-clickable',
					{
						'is-visible': this.visible,
						blocking: this.blocking
					}
				]
			},
			modal_classes() {
				return [
					'sweet-modal',
					'theme-' + this.modalTheme,
					{
						'has-title': this.has_title,
						'has-tabs': this.has_tabs,
						'has-content': this.has_content,
						'has-icon': this.icon,
						'is-mobile-fullscreen': this.enableMobileFullscreen,
						'is-visible': this.visible,
						'is-alert': (this.icon && !this.has_tabs) || (!this.icon && !this.title && !this.$slots.title),
						bounce: this.is_bouncing,
					}
				]
			},
			modal_style() {
				let width = this.width
				let maxWidth = null
				if (width !== null) {
					if (Number(width) == width) {
						width = width + 'px'
					}
					maxWidth = 'none'
				}
				return {
					width,
					maxWidth
				}
			}
		},
		methods: {
			/**
			 * Open the dialog
			 * Emits an event 'open'
			 *
			 * @param tabId string     Optional id or index of initial tab element.
			 */
			open(tabId = null) {
				if (tabId && this.has_tabs) {
					// Find tab with wanted id.
					let openingTabs = this.tabs.filter((tab) => {return tab.id === tabId})
					if (openingTabs.length > 0) {
						// Set current tab to first match.
						this.currentTab = this._changeTab(openingTabs[0])
					} else {
						// Try opening index instead of id as an alternative.
						let openingTab = this.tabs[tabId]
						if (openingTab) {
							this.currentTab = this._changeTab(openingTab)
						}
					}
				}
				this.is_open = true
				this._lockBody()
				this._animateIcon()
				setTimeout(() => this.visible = true, 30)
				this.$emit('open')
			},
			/**
			 * Close the dialog
			 * Emits an event 'close'
			 */
			close() {
				this.visible = false
				this._unlockBody()
				setTimeout(() => this.is_open = false, 300)
				this.$emit('close')
			},
			/**
			 * Bounce the modal.
			 */
			bounce() {
				this.is_bouncing = true
				setTimeout(() => this.is_bouncing = false, 330)
			},
			/**********************
			    INTERNAL METHODS
			 **********************/
			_lockBody() {
				this.backups.body.height = document.body.style.height
				this.backups.body.overflow = document.body.style.overflow
				document.body.style.height = '100%'
				document.body.style.overflow = 'hidden'
			},
			_unlockBody() {
				document.body.style.height = this.backups.body.height
				document.body.style.overflow = this.backups.body.overflow
			},
			_onOverlayClick(event) {
				if (!event.target.classList || event.target.classList.contains('sweet-modal-clickable')) {
					if (this.blocking) {
						if (this.pulseOnBlock) this.bounce()
					} else {
						this.close()
					}
				}
			},
			_onDocumentKeyup(event) {
				if (event.keyCode == 27) {
					if (this.blocking) {
						if (this.pulseOnBlock) this.bounce()
					} else {
						this.close()
					}
				}
			},
			_changeTab(tab) {
				this.tabs.map(t => t.active = t == tab)
				this.currentTab = tab
			},
			_getClassesForTab(tab) {
				return [
					'sweet-modal-tab',
					{
						active: tab.active,
						disabled: tab.disabled
					}
				]
			},
			_animateIcon() {
				if (!this.icon) return
				switch (this.icon) {
					case 'success':
						setTimeout(() => {
							this._applyClasses(this.$refs.icon_success, {
								'': [ 'animate' ],
								'.sweet-modal-tip': [ 'animateSuccessTip' ],
								'.sweet-modal-long': [ 'animateSuccessLong' ]
							})
						}, 80)
						break;
					case 'warning':
						this._applyClasses(this.$refs.icon_warning, {
							'': [ 'pulseWarning' ],
							'.sweet-modal-body': [ 'pulseWarningIns' ],
							'.sweet-modal-dot': [ 'pulseWarningIns' ]
						})
						break;
					case 'error':
						setTimeout(() => {
							this._applyClasses(this.$refs.icon_error, {
								'': [ 'animateErrorIcon' ],
								'.sweet-modal-x-mark': [ 'animateXMark' ]
							})
						}, 80)
						break;
				}
			},
			/**
			 * Apply classes from the classMap to $ref or children of $ref, a native
			 * DOMElement.
			 *
			 * ClassMap:
			 * {
			 *     'selector': [ 'class1', 'class2', ... ]
			 * }
			 *
			 * Empty Selector selects $ref.
			 *
			 * @param DOMNode $ref     Element to apply classes to or children of that element
			 * @param Object  classMap Class Map which elements get which classes (see doc)
			 */
			_applyClasses($ref, classMap) {
				for (let cl in classMap) {
					let classes = classMap[cl]
					let $el
					if (cl == '') {
						$el = $ref
					} else {
						$el = $ref.querySelector(cl)
					}
					$el.classList.remove(...classes)
					$el.classList.add(...classes)
				}
			}
		}
	}
</script>


