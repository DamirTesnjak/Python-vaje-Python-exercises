var lat, lon;
var urlString;
var click = 0;

$(document).ready(function() {
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(function(position) {
    lat = "lat=" + position.coords.latitude;
    lon = "lon=" + position.coords.longitude;
    getData(lon, lat);
  });
} else {
  console.log("Geolocation is not supported by this browser.");
}
});

function getData(lon, lat) {
urlString ="https://fcc-weather-api.glitch.me/api/current?" + lon + "&" + lat;
$.getJSON(urlString, function(data) {
  document.getElementById("city").innerHTML =data.name + ", " + data.sys.country;
  document.getElementById("icon").innerHTML = "<img src=" + data.weather[0].icon + 'width="32" height="32">';
  document.getElementById("temperature").innerHTML =Math.round(data.main.temp * 10) / 10 + " " + String.fromCharCode(176) + "C";
  document.getElementById("weather").innerHTML =data.weather[0].description;
});
}

function convert() {
$.getJSON(urlString, function(data) {
  if (click == 0) {
    var C = data.main.temp;
    click += 1;
    var F = Math.round((C * 9 / 5 + 32) * 10) / 10;
    document.getElementById("temperature").innerHTML = F + " " + String.fromCharCode(176) + "F";
  } else {
    click = 0;
    document.getElementById("temperature").innerHTML =Math.round(data.main.temp * 10) / 10 + " " + String.fromCharCode(176) + "C";
  }
});
}
