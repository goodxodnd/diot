<template>
    <div class="row">
        <div class="col-md-12">
          <div class="main-title">Service Registration</div>
        </div>
        <div class="col-md-2"></div>
        <div class="col-md-8">
           <div class="box">
            <div class="box-text">Registration</div>
            <div class="box-signup">
              <label class="txt01">Device</label>
              <input type="text" class="device-name"  placeholder="Enter Device Name">
              <label class="txt02">Discription</label>
              <input class="discription" type="text" placeholder="Enter Discription"/>
              <label class="txt03">Service Name</label>
              <input class="service-name" type="text" placeholder="Enter Service Name"/>
              <label class="txt04">Type</label>
              <input class="type" type="text" placeholder="Enter Type"/>
              <label class="txt05">Tier</label>
              <input class="tier" type="text" placeholder="Enter Tier"/>
              <label class="txt06">API</label>
              <input class="api" type="text" placeholder="Enter API"/>
            </div>
            <b-button variant="light" class="signup">R E G I S T R A T I O N</b-button></div>

          </div>
        <div class="col-md-2"></div>
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
.box {
background-color: #E7E7E7;
position: relative;
top:90px;
left: 190px;
width:700px;
height:720px;
border-radius:50px;
}
.box-text {
font-size: 40px;
font-weight: bold;
position: relative;
top: 20px;
left: 130px;
}
.box-signin{
font-size: 20px;
}
.device-name {
width: 400px;
height: 45px;
position: relative;
top: 75px;
left: 80px;
}
.discription {
width: 400px;
height: 45px;
position: relative;
top: 115px;
left: 130px;
}
.service-name {
width: 400px;
height: 45px;
position: relative;
top: 155px;
left: 130px;
}
.type {
width: 400px;
height: 45px;
position: relative;
top: 195px;
left: 130px;
}
.tier {
width: 400px;
height: 45px;
position: relative;
top: 230px;
left: 130px;
}
.api {
width: 400px;
height: 45px;
position: relative;
top: 270px;
left: 130px;
}
.signup {
width: 400px;
height:50px;
position: relative;
top:310px;
left:130px;
font-size: 27px;
font-weight: bold;
background-color:#3d6098;
color: white;
}
.txt01 {
position: relative;
top: 30px;
left: 130px;
}
.txt02 {
position: relative;
top:115px;
left: -327px;
}
.txt03 {
position: relative;
top:158px;
left: -275px;
}
.txt04 {
position: relative;
top:198px;
left: -275px;
}
.txt05 {
position: relative;
top:235px;
left: -275px;
}
.txt06 {
position: relative;
top:273px;
left: -275px;
}



</style>
