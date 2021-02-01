var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 50
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

var svg = d3
  .select("body")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

  var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

  var attributeData = d3.csv("radar_chart.csv").then(function(data) {

  attributeData.forEach(function(data) {
    data.year = +data.year;
    data.acousticness = +data.acousticness;
    data.danceability = +data.daceability;
    data.energy = +data.energy;
    data.instrumentalness = +data.instrumentalness;
    data.liveness = +data.liveness;
    data.mode = +data.mode;
    data.speechiness = +data.speechiness;
    data.valence = +data.valence;
  });  

});



//var ctx = document.getElementById('myChart');
//var myRadarChart = new Chart(ctx, {
 //   type: 'radar',
 //   data: data,
  //  options: 
//})