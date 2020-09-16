<template>
  <div class="row" :class="$mq" style="position:relative;">
        <div class="col-md-12">
          <div class="server-main-title" style="background-color:#3d6098; height:70px;">
            <img src='../assets/small-white-logo.png' style="position:relative; left:2%;">
          </div>
        </div>
        <div class="col-md-3">
          <img src='../assets/big-user.png' style="position:relative; left:10%; top:30%;">
        </div>
        <div class="col-md-9">
          <div class="result-user-name" style="font-size: 2.0em; font-weight:bold; position: relative; top:100%; left:-5%;"> John@did </div>
        </div>
        <div class="col-md-11">
          <div class="user-info-table" style="position:relative; top:160%;">

            <b-table-simple hover>
              <b-thead head-variant="secondary">
                <b-tr>
                <b-th>DeviceName</b-th>
                <b-th>DeviceType</b-th>
                <b-th>Info</b-th>
                <b-th>Device Did</b-th>
                <b-th>Owner Did</b-th>

                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr>
                  <b-td></b-td>
                  <b-td></b-td>
                  <b-td></b-td>
                  <b-td></b-td>
                  <b-td></b-td>



                </b-tr>
              </b-tbody>
            </b-table-simple>


          </div>
        </div>

  </div>
</template>
