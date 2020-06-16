<template>
  <div>
    <div class="row">
        <div class="col-md-2.5">
          <div class="main-title">Device List</div>
        </div>
        <div class="col-md-9">
          <input class="form-control" type="text" placeholder="Search" aria-label="Search">
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-11">
            <b-card class= "list01" title="Device-Info">
              <b-button class= "service">Service</b-button>
              <b-button class= "using">Using</b-button>
            </b-card>
            <b-card class= "list02" title="Device-Info">
              <b-button class= "service">Service</b-button>
              <b-button class= "using">Using</b-button>
            </b-card>
            <b-card class= "list03" title="Device-Info">
              <b-button class= "service">Service</b-button>
              <b-button class= "using">Using</b-button>
            </b-card>
            <b-card class= "list04" title="Device-Info">
              <b-button class= "service">Service</b-button>
              <b-button class= "using">Using</b-button>
            </b-card>
        </div>
        <div class="col-md-1"></div>
       </div>
  </div>

</template>

<script>
</script>

<style>
.main-title {
position: relative;
top: 30px;
font-weight: bold;
font-size: 50px;
}
.form-control {
  border: 1px solid #3d6098;
  box-shadow: 0 0 0 1px #3d6098;
  position: relative;
  top: 50px;
  left: 20px;
}
.service {
position: relative;
top: -45px;
left: 1320px;
background-color: #f04b4c;
font-size: 20px;
width: 150px;
}
.using {
position: relative;
top: 10px;
left: 1165px;
background-color: #f04b4c;
font-size: 20px;
width: 150px;
}
.list01 {
position: relative;
left:-10px;
top:90px;
}
.list02 {
position: relative;
left:-10px;
top:110px;
}
.list03 {
position: relative;
left:-10px;
top:130px;
}
.list04 {
position: relative;
left:-10px;
top:150px;
}


</style>
