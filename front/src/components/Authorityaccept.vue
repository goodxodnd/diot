<template>
    <div class="row">
        <div class="col-md-2">
          <div class= "sub-title">My Device List</div>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-9">
          <div class="main-title">Authority Accept</div>
        </div>
        <div class="col-md-2">
          <input class="form-control" type="text" placeholder="Search" aria-label="Search">
            <b-card class="card01" title="Device name"><b-button class= "authority">Authority</b-button>
               <b-card-text>
               service-<br>2020.06.15<br>Tier
               </b-card-text>
            </b-card>
            <b-card class="card02" title="Device name"><b-button class= "authority">Authority</b-button>
               <b-card-text> service-<br>2020.06.15<br>Tier</b-card-text>
            </b-card>
            <b-card class="card03" title="Device name"><b-button class= "authority">Authority</b-button>
               <b-card-text> service-<br>2020.06.15<br>Tier</b-card-text>
            </b-card>
             <b-card class="card04" title="Device name"><b-button class= "authority">Authority</b-button>
               <b-card-text> service-<br>2020.06.15<br>Tier</b-card-text>
            </b-card>
          </div>
        <div class="col-md-1"></div>
        <div class="col-md-8">
          <b-card class="card05" title="Set Alram" sub-title="Device Info">
             <b-button class= "accept">Accept</b-button><b-button class="reject">Reject</b-button>
               <b-card-text> service-<br>2020.06.15<br>Tier</b-card-text>
          </b-card>
          <b-card class="card06" title="Stop Watch" sub-title="Device Info">
             <b-button class= "accept">Accept</b-button><b-button class="reject">Reject</b-button>
               <b-card-text> service-<br>2020.06.15<br>Tier</b-card-text>
          </b-card>
          <b-card class="card07" title="Timer" sub-title="Device Info">
            <b-button class= "accept">Accept</b-button><b-button class="reject">Reject</b-button>
               <b-card-text> service-<br>2020.06.15<br>Tier</b-card-text>
          </b-card>
          <b-card class="card08" title="Timer" sub-title="Device Info">
             <b-button class= "accept">Accept</b-button><b-button class="reject">Reject</b-button>
               <b-card-text> service-<br>2020.06.15<br>Tier</b-card-text>
          </b-card>
        </div>
        <div class="col-md-1"></div>
    </div>

</template>

<script>
</script>

<style>
.sub-title {
position: relative;
top: 45px;
font-weight: bold;
font-size: 35px;
}
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
  width: 250px;
}
.authority {
position: relative;
top: 80px;
left: 110px;
background-color: #f04b4c;
width:100px;
}
.card01 {
position: relative;
top:80px;
}
.card02 {
position: relative;
top:110px;
}
.card03 {
position: relative;
top:140px;
}
.card04 {
position: relative;
top:170px;
}
.accept {
position: relative;
top: -60px;
left: 950px;
background-color: #f04b4c;
width:100px;
}
.reject {
position: relative;
top: 0px;
left: 850px;
background-color: #f04b4c;
width:100px;
}
.card05 {
position: relative;
top: 80px;
}
.card06 {
position: relative;
top: 120px;
}
.card07 {
position: relative;
top: 160px;
}
.card08 {
position: relative;
top: 200px;
}




</style>
