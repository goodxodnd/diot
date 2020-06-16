<template>
    <div class="row">
        <div class="col-md-12">
          <div class="main-title">Device List</div>
        </div>
        <div class="col-md-11">
          <b-card class="box01">
            <b-card-text class="text">
              No Device.<br>Do you want to add a device?<br><br><br><br><br><br><br>
              <b-button class= "add">Add</b-button>
            </b-card-text>


          </b-card>
        </div>
        <div class="col-md-1"></div>
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
.box01{
position: relative;
top:90px;
}
.text {
position: relative;
font-weight: bold;
font-size: 40px;
top: 120px;
left: 500px;
}
.add {
position: relative;
top: -250px;
left: 100px;
width:250px;
background-color: #f04b4c;
font-size:40px;
font-weight: bold;
}
</style>
