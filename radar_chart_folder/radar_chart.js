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

  d3.csv("radar_chart.csv").then(function(data) {

    var parseTime = d3.timeParse("%Y");

  data.forEach(function(data) {
    data.year = parseTime(data.year);
    data.acousticness = +data.acousticness;
    data.danceability = +data.daceability;
    data.energy = +data.energy;
    data.instrumentalness = +data.instrumentalness;
    data.liveness = +data.liveness;
    data.mode = +data.mode;
    data.speechiness = +data.speechiness;
    data.valence = +data.valence;
  });  
var xLinearScale = d3.scaleTime()
  .domain(d3.extent(data, d => d.year))
  .range([0, width]);
var yLinearScale = d3.scaleLinear().range([height, 0]);

  // set yMax using an if/else statement
var acousticnessMax = d3.max(data, d => d.acousticness);
var danceabilityMax = d3.max(data, d => d.danceability);
var energyMax = d3.max(data, d => d.energy);
var instrumentalnessMax = d3.max(data, d => d.instrumentalness);
var livenessMax = d3.max(data, d => d.liveness);
var modeMax = d3.max(data, d => d.mode);
var speechinessMax = d3.max(data, d => d.speechiness);
var valenceMax = d3.max(data, d => d.valence);

var yMax;
if (acousticnessMax > danceabilityMax) {
  yMax = acousticnessMax;
}
else if (danceabilityMax > energyMax) {
  yMax = danceabilityMax;
}
else if (energyMax > instrumentalnessMax) {
  yMax = energyMax;
}
else if (instrumentalnessMax > livenessMax) {
  yMax = instrumentalnessMax;
}
else if (livenessMax > modeMax) {
  yMax = livenessMax;
}
else if (modeMax > speechinessMax) {
  yMax = modeMax;
}
else if (speechinessMax > valenceMax) {
  yMax = speechinessMax;
}
else if (valenceMax > acousticnessMax) {
  yMax = valenceMax;
}

yLinearScale.domain([0, yMax]);
  // add xaxis
var bottomAxis = d3.axisBottom(xLinearScale).tickFormat(d3.timeFormat("%Y"));
var leftAxis = d3.axisLeft(yLinearScale);


  // add yaxis
chartGroup.append("g")
  .attr("transform", `translate(0, ${height})`)
  .call(bottomAxis);

chartGroup.append("g").call(leftAxis);

  // generate lines
var line1 = d3.line()
  .x(d => xLinearScale(d.year))
  .y(d => yLinearScale(d.acousticness));

var line2 = d3.line()
  .x(d => xLinearScale(d.year))
  .y(d => yLinearScale(d.danceability));
var line3 = d3.line()
  .x(d => xLinearScale(d.year))
  .y(d => yLinearScale(d.energy));
var line4 = d3.line()
  .x(d => xLinearScale(d.year))
  .y(d => yLinearScale(d.instrumentalness));
var line5 = d3.line()
  .x(d => xLinearScale(d.year))
  .y(d => yLinearScale(d.liveness));
var line6 = d3.line()
  .x(d => xLinearScale(d.year))
  .y(d => yLinearScale(d.mode));
var line7 = d3.line()
  .x(d => xLinearScale(d.year))
  .y(d => yLinearScale(d.speechiness));
var line8 = d3.line()
  .x(d => xLinearScale(d.year))
  .y(d => yLinearScale(d.valence));
  //append paths 
chartGroup
  .append("path")
  .attr("d", line1(data))
  .classed("line orange", true);

  //append paths 

chartGroup
  .append("path")
  .attr("d", line3(data))
  .classed("line red", true);
chartGroup
  .append("path")
  .attr("d", line4(data))
  .classed("line green", true);
chartGroup
  .append("path")
  .attr("d", line5(data))
  .classed("line pink", true);
chartGroup
  .append("path")
  .attr("d", line6(data))
  .classed("line black", true);
chartGroup
  .append("path")
  .attr("d", line7(data))
  .classed("line purple", true);
chartGroup
  .append("path")
  .attr("d", line8(data))
  .classed("line brown", true);





  

});



