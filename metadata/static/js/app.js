
function buildMetadata(state) {
    
    
  d3.json("states.json").then((data) => {
 
      var chart = d3.select("#sample-metadata")
      chart.html("")
     
      Object.entries(state).forEach(([key, value]) => {
        chart.append("p").text(`${key} : ${value}`);
      });
    });

};

function init() {
    
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
    
    // Use the list of state names to populate the select options
    d3.json("states.json").then((data) => {

      var stateNames = data.states
      // Use the first state from the list to build the initial plots
      var firstState = stateNames[0];

      buildMetadata(firstState);
    
      stateNames.forEach((item) => {
        selector
          .append("option")
          .text(item.state)
          .property("value", item.state);
        });
    });
  }
  
  function optionChanged(newState) {
    // Fetch new data each time a new sample is selected
    // buildCharts(newState);
    console.log(newState)
    buildMetadata(newState);
  }
  
  // Initialize the dashboard

  init();