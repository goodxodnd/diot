<template>
  <div>
    <div class="row">
        <div class="col-md-2.5">
          <div class="device-list-title">Device List</div>
        </div>
        <div class="col-md-8">
          <input class="form-control" type="text" placeholder="Search" aria-label="Search" style="position:relative; top:50%; ">
        </div>
        <div class="col-md-2"></div>
        <div class="col-md-11">
            <b-card class= "device-list01" >
              <b-button class= "service" style="color:white; background-color:#f04b4c;">Service</b-button>
              <b-button class= "using" style="color:white; background-color:#f04b4c;">Using</b-button>
              <img src="../assets/printer.png" style="position:relative; top:15%; left:-20%; ">
                 <div class="content02"><b>Printer(Color)</b><br>Device Info<br>DID-NUMBER 11564-23182-12945</div>
            </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-11">
            <b-card class= "device-list02" >
              <b-button class= "service" style="color:white; background-color:#f04b4c;">Service</b-button>
              <b-button class= "using" style="color:white; background-color:#f04b4c;">Using</b-button>
              <img src="../assets/printer.png" style="position:relative; top:15%; left:-20% ">
                 <div class="content02"><b>Printer(Mono)</b><br>Device Info<br>DID-NUMBER 11564-25282-23945</div>
            </b-card>
        </div>
        <div class="col-md-1"></div>
          <div class="col-md-11">
            <b-card class= "device-list03" >
              <b-button class= "service" style="color:white; background-color:#f04b4c;">Service</b-button>
              <b-button class= "using" style="color:white; background-color:#f04b4c;">Using</b-button>
              <img src="../assets/watch.png" style="position:relative; top:15%; left:-20% ">
                 <div class="content02"><b>Watch</b><br>Device Info<br>DID-NUMBER 23422-45673-12643</div>
            </b-card>
          </div>
        <div class="col-md-1"></div>
          <div class="col-md-11">
            <b-card class= "device-list04" >
              <b-button class= "service" style="color:white; background-color:#f04b4c;">Service</b-button>
              <b-button class= "using" style="color:white; background-color:#f04b4c;">Using</b-button>
              <img src="../assets/tabelet.png" style="position:relative; top:15%; left:-20%">
                 <div class="content02"><b>Tabelet</b><br>Device Info<br>DID-NUMBER 23421-23434-39423</div>
            </b-card>
          </div>
        <div class="col-md-1"></div>
       </div>
  </div>

</template>

<script>
</script>

<style>
.device-list-title {
position: relative;
top: 30%;
  left: 2%;
font-weight: bold;
font-size: 3em;
}
.form-control {
  border: 1px solid #3d6098;
  box-shadow: 0 0 0 1px #3d6098;
  position: relative;
  top: 50%;
}
.service {
position: relative;
top: -15%;
left: 90.5%;
background-color: #f04b4c;
font-size: 20px;
width: 10%;
}
.using {
position: relative;
top: 50%;
left: 80%;
background-color: #f04b4c;
font-size: 20px;
width: 10%;
}
.device-list01 {
position: relative;
left:-0.6%;
top:40%;
  height:140px;
}
.device-list02 {
position: relative;
left:-0.6%;
top:60%;
  height:140px;
}
.device-list03 {
position: relative;
left:-0.6%;
top:80%;
  height:140px;
}
.device-list04 {
position: relative;
left:-0.6%;
top:100%;
  height:140px;
}
.content02{
  position:relative;
  top:-50px;
  left:110px;
}

</style>
