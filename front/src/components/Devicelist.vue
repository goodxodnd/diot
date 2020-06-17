<template>
  <div>
    <div class="row">
        <div class="col-md-2.5">
          <div class="main-title">Device List</div>
        </div>
        <div class="col-md-8">
          <input class="form-control" type="text" placeholder="Search" aria-label="Search">
        </div>
        <div class="col-md-2"></div>
        <div class="col-md-11">
            <b-card class= "list01" >
              <b-button class= "service" style="color:white; background-color:#f04b4c;">Service</b-button>
              <b-button class= "using" style="color:white; background-color:#f04b4c;">Using</b-button>
              <img src="../assets/printer.png" style="position:relative; top:15px; left:-290px ">
                 <div class="content02"><b>Printer(Color)</b><br>Device Info<br>DID-NUMBER 11564-23182-12945</div>
            </b-card>
            <b-card class= "list02" >
              <b-button class= "service" style="color:white; background-color:#f04b4c;">Service</b-button>
              <b-button class= "using" style="color:white; background-color:#f04b4c;">Using</b-button>
              <img src="../assets/printer.png" style="position:relative; top:15px; left:-290px ">
                 <div class="content02"><b>Printer(Mono)</b><br>Device Info<br>DID-NUMBER 11564-25282-23945</div>
            </b-card>
            <b-card class= "list03" >
              <b-button class= "service" style="color:white; background-color:#f04b4c;">Service</b-button>
              <b-button class= "using" style="color:white; background-color:#f04b4c;">Using</b-button>
              <img src="../assets/watch.png" style="position:relative; top:15px; left:-290px ">
                 <div class="content02"><b>Watch</b><br>Device Info<br>DID-NUMBER 23422-45673-12643</div>
            </b-card>
            <b-card class= "list04" >
              <b-button class= "service" style="color:white; background-color:#f04b4c;">Service</b-button>
              <b-button class= "using" style="color:white; background-color:#f04b4c;">Using</b-button>
              <img src="../assets/tabelet.png" style="position:relative; top:15px; left:-290px">
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
top: -10px;
left: 1100px;
background-color: #f04b4c;
font-size: 20px;
width: 150px;
}
.using {
position: relative;
top: 45px;
left: 945px;
background-color: #f04b4c;
font-size: 20px;
width: 150px;
}
.list01 {
position: relative;
left:-10px;
top:90px;
  height:140px;
}
.list02 {
position: relative;
left:-10px;
top:110px;
  height:140px;
}
.list03 {
position: relative;
left:-10px;
top:130px;
  height:140px;
}
.list04 {
position: relative;
left:-10px;
top:150px;
  height:140px;
}
.content02{
  position:relative;
  top:-50px;
  left:110px;
}

</style>
