<template>
  <div>
    <div class="row">
        <div class="col-md-2.5">
          <div class="search-title"> Device List</div>
        </div>
        <div class="col-md-8">
          <input class="form-search" type="text" placeholder="Search" aria-label="Search" style="position: relative; top:50%;">
        </div>
        <div class="col-md-1"></div>

        <div class="col-md-11">
            <b-card class= "list01" title="Device-Info">
               <b-card-text><br><br></b-card-text>
              <b-button class="authority-search" style="color:white; background-color:#f04b4c; position:relative; top:-10%;">Authority</b-button>
              <b-button class= "ownership-search" style="color:white; background-color:#f04b4c;">Ownership</b-button>
              <b-button class= "tier-search" style="color:white; background-color:#f04b4c;">Tier</b-button>
            </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-11">
            <b-card class= "list02" title="Device-Info">
              <b-card-text><br><br></b-card-text>
              <b-button class="authority-search" style="color:white; background-color:#f04b4c;">Authority</b-button>
              <b-button class= "ownership-search" style="color:white; background-color:#f04b4c;">Ownership</b-button>
              <b-button class= "tier-search" style="color:white; background-color:#f04b4c;">Tier</b-button>
            </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-11">
            <b-card class= "list03" title="Device-Info">
              <b-card-text><br><br></b-card-text>
              <b-button class="authority-search" style="color:white; background-color:#f04b4c;">Authority</b-button>
              <b-button class= "ownership-search" style="color:white; background-color:#f04b4c;">Ownership</b-button>
              <b-button class= "tier-search" style="color:white; background-color:#f04b4c;">Tier</b-button>
            </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-11">
            <b-card class= "list04" title="Device-Info">
              <b-card-text><br><br></b-card-text>
              <b-button class="authority-search" style="color:white; background-color:#f04b4c;">Authority</b-button>
              <b-button class= "ownership-search" style="color:white; background-color:#f04b4c;">Ownership</b-button>
              <b-button class= "tier-search" style="color:white; background-color:#f04b4c;">Tier</b-button>
            </b-card>
        </div>
        <div class="col-md-1"></div>
       </div>
  </div>

</template>

<script>
</script>

<style>
.search-title {
position: relative;
top: 30%;
  left:2%;
font-weight: bold;
font-size: 3em;
}
.form-search {
  border: 1px solid #3d6098;
  box-shadow: 0 0 0 1px #3d6098;
  position: relative;
  top: 50%;
  width:90%;
  height:50%;
  left:3%;
}
.authority-search {
  position: relative;
width: 10%;
}
.ownership-search {
position: relative;
width: 150px;
}
.tier-search {
position: relative;
width: 150px;
}
.list01 {
position: relative;
left:-0.6%;
top:25%;
}
.list02 {
position: relative;
left:-0.6%;
top:40%;
}
.list03 {
position: relative;
left:-0.6%;
top:55%;
}
.list04 {
position: relative;
left:-0.6%;
top:70%;
}


</style>
