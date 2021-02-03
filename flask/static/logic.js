
// This is where the user input would feed into our Javascript

let form = d3.select("#form");
// form.on("submit", runFilter);

// console.log(song_info);
// console.log(song_info.Audio_Features[0]);


let audio_features = song_info.Audio_Features[0]



let removeObjectProperties = function (obj, props) {

  for (var i = 0; i < props.length; i++) {
    if (obj.hasOwnProperty(props[i])) {
      delete obj[props[i]];
    }
  }

};

removeObjectProperties(audio_features, ["analysis_url", "id", "key", "mode", "time_signature", "track_href", "type", "duration_ms", "uri"]);

let keys_list = [];
let values_list = [];
Object.entries(audio_features).forEach(function ([key, value]) {
  keys_list.push(key);
  values_list.push(value);
});
console.log(keys_list);
console.log(values_list);

let headline = d3.select("#info");
headline.selectAll("h3")
  .data(["Song: " + song_info.Track_Title, "Popularity Score: " + song_info.Track_Popularity, "Release Date: " + song_info.Release_Date])
  .enter()
  .append("h3")
  .text(function (d) { return d; });

let preview_path = song_info.Track_Preview_URL
let preview_div = d3.select("video");

preview_div.selectAll("source")
  .data(preview_path)
  .enter()
  .append("source")
  .attr("src", preview_path)
  .attr("type", "audio/mpeg");

let tbody = d3.select("tbody").append("tr");
let thead = d3.select("thead").append("tr");
thead.selectAll("th")
  .data(keys_list)
  .enter()
  .append("th")
  .classed("table-head", true)
  .text(function (d) { return d; });
tbody.selectAll("td")
  .data(values_list)
  .enter()
  .append("td")
  .text(function (d) { return d; });

let year_stats = song_info.Yearly_Avgs;
let released = song_info.Release_Date
let year_compare = []
// year_stats.forEach((year) => {
//     Object.entries(entry).forEach(([key, value]) => {
//       if (key == released) {
//         year_compare.push(value);
//       }
//      });
//     });

  console.log(year_compare);

  radar_data = [{
    type: 'scatterpolar',
    r: [song_info.Yearly_Avgs[0], song_info.Yearly_Avgs[1], song_info.Yearly_Avgs[2], song_info.Yearly_Avgs[3], song_info.Yearly_Avgs[4], song_info.Yearly_Avgs[6], song_info.Yearly_Avgs[8], song_info.Yearly_Avgs[0]],
    theta: [song_info.Compare_Keys[0], song_info.Compare_Keys[1], song_info.Compare_Keys[2], song_info.Compare_Keys[3], song_info.Compare_Keys[4], song_info.Compare_Keys[6], song_info.Compare_Keys[8], song_info.Compare_Keys[0]],
    fill: 'toself',
    name: released
  },
  {
    type: 'scatterpolar',
    r: [song_info.Compare_Scale[6], song_info.Compare_Scale[0], song_info.Compare_Scale[1], song_info.Compare_Scale[7], song_info.Compare_Scale[8], song_info.Compare_Scale[5], song_info.Compare_Scale[9], song_info.Compare_Scale[6]],
    theta: [song_info.Compare_Keys[0], song_info.Compare_Keys[1], song_info.Compare_Keys[2], song_info.Compare_Keys[3], song_info.Compare_Keys[4], song_info.Compare_Keys[6], song_info.Compare_Keys[8], song_info.Compare_Keys[0]],
    fill: 'toself',
    name: song_info.Track_Title
  }
  ]
  
  radar_layout = {
    polar: {
      radialaxis: {
        visible: true,
        range: [0, 1]
      }
    },
    showlegend: true
  }
  
  Plotly.newPlot("myDiv", radar_data, radar_layout)



// function runFilter() {

//     audio_features.forEach(function (feature) {
//       let row = tbody.append("tr");
//       Object.entries(feature).forEach(function ([key, value]) {
//         var cell = row.append("td");
//         cell.text(value);
//       });
//     });

// };


  // // Build the plots and charts with the input
  // buildAPI(song);

  // fetch(`/songinteraction`, {
  //   method: "GET",
  // })
  //   .then(response => response.json())
  //   .then(({ song_input }) => {
  //     beats.forEach(
  //       // do something to create tables/charts/displays
  //     )
  //   });

