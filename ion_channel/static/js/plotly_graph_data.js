function makeplot(id) {
    http = window.location.protocol;
    host = window.location.hostname;
    port = window.location.port;
    if (port.IsNullOrEmpty) {
        host_url = http + '//' + host;
    }
    else {
        host_url = http + '//' + host + ':' + port;
    }
    path = '/api/graph_data/' + id + '?format=json';
//    console.log(host_url+path);
    Plotly.d3.json(host_url+path,
        function(data){ processData(data, id) }
    );
};

function processData(allRows, id) {

    graph_url = '/api/graph/details/' + id + '?format=json';
    Plotly.d3.json(host_url+graph_url, function(fig) {
        var graph_data = fig;

//        console.log(host_url+graph_url);

        var plot_data = [];
        for (var i=0; i<allRows.length; i++) {
            plot_data[i] = {
            'name': allRows[i].series_name,
            'mode': 'line',
            'type': 'scatter',
            'x': allRows[i].x,
            'y': allRows[i].y,
            };
         }

//        console.log(graph_data);
        var x_title = graph_data.x_axis_type + ' (' + graph_data.x_axis_unit + ')';
        var y_title = graph_data.y_axis_type + ' (' + graph_data.y_axis_unit + ')';
        var layout = {
                    'xaxis': {'title': x_title},
                    'yaxis': {'title': y_title}
                     };

        makePlotly(plot_data, layout, id);
        }
    );

}

function makePlotly( plot_data, layout, id ){
    var plotDiv = document.getElementById("plot");
    var traces = plot_data;

    Plotly.newPlot(id, traces, layout);
};