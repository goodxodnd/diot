<template>
  <button v-on:click="alertDisplay">Click Me!</button>
</template>

<script>
  export default {
    data() {
      return {}
    },
    methods: {
        alertDisplay() {
          // Adding an input method from SweetAlert 2 automatically binds an input form.
        this.$swal.fire({
  icon: 'success',
  title: 'Device Regist Success!',
  showConfirmButton: false,
  timer: 1500
})
      }
    }
  }
</script>
