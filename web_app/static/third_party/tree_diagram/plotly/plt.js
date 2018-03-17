// Multiple plots
//Plotly.d3.csv(url1, function(err, csvData1) {
//  Plotly.d3.csv(url2, function(err, csvData2) {
//    /* merge csvData1 and csvData2 into plotly 'data' and 'layout' */
//    Plotly.newPlot('graph', data, layout);
//  });
//});

Plotly.d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv', function (err, data) {
      // Create a lookup table to sort and regroup the columns of data,
      // first by year, then by continent:
      var lookup = {};
      function getData(year, continent) {
        var byYear, trace;
        if (!(byYear = lookup[year])) {;
          byYear = lookup[year] = {};
        }
         // If a container for this year + continent doesn't exist yet,
         // then create one:
        if (!(trace = byYear[continent])) {
          trace = byYear[continent] = {
            x: [],
            y: [],
            id: [],
            text: [],
            marker: {size: []}
          };
        }
        return trace;
      }

      // Go through each row, get the right trace, and append the data:
      for (var i = 0; i < data.length; i++) {
        var datum = data[i];
        var trace = getData(datum.year, datum.continent);
        trace.text.push(datum.country);
        trace.id.push(datum.country);
        trace.x.push(datum.lifeExp);
        trace.y.push(datum.gdpPercap);
        trace.marker.size.push(datum.pop);
      }

      // Get the group names:
      var years = Object.keys(lookup);
      // In this case, every year includes every continent, so we
      // can just infer the continents from the *first* year:
      var firstYear = lookup[years[0]];
      var continents = Object.keys(firstYear);

      // Create the main traces, one for each continent:
      var traces = [];
      for (i = 0; i < continents.length; i++) {
        var data = firstYear[continents[i]];
         // One small note. We're creating a single trace here, to which
         // the frames will pass data for the different years. It's
         // subtle, but to avoid data reference problems, we'll slice
         // the arrays to ensure we never write any new data into our
         // lookup table:
        traces.push({
          name: continents[i],
          x: data.x.slice(),
          y: data.y.slice(),
          id: data.id.slice(),
          text: data.text.slice(),
          mode: 'markers',
          marker: {
            size: data.marker.size.slice(),
            sizemode: 'area',
            sizeref: 200000
          }
        });
      }

      // Create a frame for each year. Frames are effectively just
      // traces, except they don't need to contain the *full* trace
      // definition (for example, appearance). The frames just need
      // the parts the traces that change (here, the data).
      var frames = [];
      for (i = 0; i < years.length; i++) {
        frames.push({
          name: years[i],
          data: continents.map(function (continent) {
            return getData(years[i], continent);
          })
        })
      }

      // Now create slider steps, one for each frame. The slider
      // executes a plotly.js API command (here, Plotly.animate).
      // In this example, we'll animate to one of the named frames
      // created in the above loop.
      var sliderSteps = [];
      for (i = 0; i < years.length; i++) {
        sliderSteps.push({
          method: 'animate',
          label: years[i],
          args: [[years[i]], {
            mode: 'immediate',
            transition: {duration: 300},
            frame: {duration: 300, redraw: false},
          }]
        });
      }

      var layout = {
        xaxis: {
          title: 'Life Expectancy',
          range: [30, 85]
        },
        yaxis: {
          title: 'GDP per Capita',
          type: 'log'
        },
        hovermode: 'closest',
         // We'll use updatemenus (whose functionality includes menus as
         // well as buttons) to create a play button and a pause button.
         // The play button works by passing `null`, which indicates that
         // Plotly should animate all frames. The pause button works by
         // passing `[null]`, which indicates we'd like to interrupt any
         // currently running animations with a new list of frames. Here
         // The new list of frames is empty, so it halts the animation.
        updatemenus: [{
          x: 0,
          y: 0,
          yanchor: 'top',
          xanchor: 'left',
          showactive: false,
          direction: 'left',
          type: 'buttons',
          pad: {t: 87, r: 10},
          buttons: [{
            method: 'animate',
            args: [null, {
              mode: 'immediate',
              fromcurrent: true,
              transition: {duration: 300},
              frame: {duration: 500, redraw: false}
            }],
            label: 'Play'
          }, {
            method: 'animate',
            args: [[null], {
              mode: 'immediate',
              transition: {duration: 0},
              frame: {duration: 0, redraw: false}
            }],
            label: 'Pause'
          }]
        }],
         // Finally, add the slider and use `pad` to position it
         // nicely next to the buttons.
        sliders: [{
          pad: {l: 130, t: 55},
          currentvalue: {
            visible: true,
            prefix: 'Year:',
            xanchor: 'right',
            font: {size: 20, color: '#666'}
          },
          steps: sliderSteps
        }]
      };

      // Create the plot:
      Plotly.plot('myDiv', {
        data: traces,
        layout: layout,
        frames: frames,
      });
});


function LineGraph(divSelector, xData, yData, xTitle, yTitle, color) {

    var svg = d3.select(divId),
        margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom,
        g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var parseTime = d3.timeParse("%d-%b-%y");

    var x = d3.scaleTime()
        .rangeRound([0, width]);

    var y = d3.scaleLinear()
        .rangeRound([height, 0]);

    var line = d3.line()
        .x(function(d) { return x(xData); })
        .y(function(d) { return y(yData); });

    g.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x))
    .select(".domain")
      .remove();

    g.append("g")
      .call(d3.axisLeft(y))
    .append("text")
      .attr("fill", "#000")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "0.71em")
      .attr("text-anchor", "end")
      .text(yTitle;

      g.append("path")
          .datum(data)
          .attr("fill", "none")
          .attr("stroke", color)
          .attr("stroke-linejoin", "round")
          .attr("stroke-linecap", "round")
          .attr("stroke-width", 1.5)
          .attr("d", line);
    });

}

