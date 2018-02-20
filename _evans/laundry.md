---
title: "evans"
layout: "evans"
---
**Current Time:** {{ site.time | date: '%H:%M %p' }}


<script>

function bodyOnLoad(){
    var d = new Date ();
    var curTime = d.getTime();
    alert(curTime);
    var tl = document.getElementById("wash-left-time-left").innerHTML;
    alert((curTime - tl)/(1000 * 60));
}

// function submitForm(form){
    
//     var d1 = new Date (),
//         d2 = new Date ( d1 );
//     d2.setMinutes ( d1.getMinutes() + 60 );
//     var d1H = d1.getHours()<10?'0':'' + d1.getHours();
//     var d1M =  d1.getMinutes()<10?'0':'' + d1.getMinutes();
//     var d2H = d2.getHours()<10?'0':'' + d2.getHours();
//     var d2M =  d2.getMinutes()<10?'0':'' + d2.getMinutes();
//     var timeDone = d2H + ':' + d2M;
//     var timeLeft = (d2.getTime() - d1.getTime()) / (1000 * 60)
//     var name = form.name.value;
//     if (form.washer.value == 1) {
//         document.getElementById("wash-left-name").value = name;
//         document.getElementById("wash-left-time").value = d1H + ':' + d1M;
//         document.getElementById("wash-left-time-done").value = timeDone;
//         document.getElementById("wash-left-time-left").value = timeLeft;
//     }
//     else if (form.washer.value == 2) {
//         document.getElementById("wash-middle-name").innerHTML = name;
//         document.getElementById("wash-middle-time").innerHTML = d1H + ':' + d1M;
//         document.getElementById("wash-middle-time-done").innerHTML = timeDone;
//         document.getElementById("wash-middle-time-left").innerHTML = timeLeft;
//     }
//     else {
//         document.getElementById("wash-right-name").innerHTML = name;
//         document.getElementById("wash-right-time").innerHTML = d1H + ':' + d1M;
//         document.getElementById("wash-right-time-done").innerHTML = timeDone;
//         document.getElementById("wash-right-time-left").innerHTML = timeLeft;
//     }
// } 
</script>

<script>
$(document).ready(function(){
$("#submitForm").click(function() {
        alert("hi");
        //$("#wash-left-time-left").attr('value',50);
    });
});
    
</script>

<body onload="bodyOnLoad();">

<table>
  <tr>
    <th>Washer</th>
    <th>Person</th>
    <th>Time-in</th>
    <th>Time-Done</th>
    <th>Time-left</th>
  </tr>
  <tr>
    <td id="wash-left">Left </td>
    <td id="wash-left-name"> </td>
    <td id="wash-left-time"> </td>
    <td id="wash-left-time-done"> </td>
    <td id="wash-left-time-left"> </td>
  </tr>
  <tr>
    <td id="wash-middle">Middle</td>
    <td id="wash-middle-name"></td>
    <td id="wash-middle-time"></td>
    <td id="wash-middle-time-done"> </td>
    <td id="wash-middle-time-left"> </td>
  </tr>
  <tr>
    <td id="wash-right">Right</td>    
    <td id="wash-right-name"></td>
    <td id="wash-right-time"></td>
  </tr>
</table>

<br>
<form action="" name="add">
    Name: <input type="text" name="name" id="name" value="Mickey"><br>
    Washer #: <select id="washer">
                    <option value="1">left</option>
                    <option value="2">Middle</option>
                    <option value="3">Right</option>
                    </select>
    <br>
    <input type="button" value="Submit" id="submitForm"> <!-- onclick="submitForm(this.form)" -->
</form>
</body>