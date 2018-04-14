var i = 0;

var diameter = 1960;
var padding = 210;

var tree = d3.layout.tree()
    .size([150, diameter / 1.5 - padding])
    .separation(function(a, b) { return (a.parent == b.parent ? 1 : 2) / a.depth; });

var diagonal = d3.svg.diagonal.radial()
    .projection(function(d) { return [d.y, d.x / 180 * Math.PI + 1.57]; });

var svg = d3.select("body").append("svg")
    .attr("width", diameter / 1.1)
    .attr("height", diameter / 1.7)
  .append("g")
    .attr("transform", "translate(" + diameter / 2.3 + "," + diameter / 15.3 + ")");

d3.selection.prototype.moveToFront = function() {
  return this.each(function() {
    this.parentNode.appendChild(this);
  });
};

// load the external data
//d3.json("treeData.json", function(error, treeData) {
//  root = treeData[0];
//  update(root);
//});

//console.log("{% url 'api:channelworm-gene-list-api' %}?format=json");
//d3.json("{% url 'api:channelworm-gene-list-api' %}?format=json", function(error, treeData) {
//    root = d3.hierarchy(treeData[0]);
//    update(root);
////            console.log('treeData'+treeData);
////            console.log(root);
////            console.log(error);
//        });


function update(source) {

  var nodes = tree.nodes(root).reverse(),
    links = tree.links(nodes);


  nodes.forEach(function(d) { d.y = d.depth * 210; });

  var node = svg.selectAll("g.node")
    .data(nodes, function(d) { return d.id || (d.id = ++i); });

  var ad = function(d) { return d.aydi; };
  var ads = function(d) { return (d.aydi + "c1"); };

  var nodeEnter = node.enter().append("g")
    .attr("class", "node")
    .attr("id", ads)
    .attr("transform", function(d) { return "rotate(" + (d.x) + ")translate(" + d.y + ")"; })
    ;

  nodeEnter.append("circle")
    .attr("r", 5)
    .attr("id", ad)
    .attr("onmouseover", 'handleMouseOver(this.id)')
    .attr("onmouseout", 'handleMouseOut(this.id)')
    .attr("onclick", 'handleClick(this.id)');

  nodeEnter.append("text")
    .attr("x", function(d) {
      return d.children || d._children ? -2 : 2; })
    .attr("dy", ".35em")
    .attr("text-anchor", function(d) { return d.x < 90 ? "start" : "end"; })
    .attr("transform", function(d) { return d.x < 90 ? "translate(10)" : "rotate(180)translate(-10)"; })
    .text(function(d) { return d.name; })
    .style("fill-opacity", 1);


  var link = svg.selectAll("path.link")
    .data(links, function(d) { return d.target.id; });


  link.enter().insert("path", "g")
    .attr("class", "link")
    .attr("d", diagonal);
}
function handleClick(aydii) {
  var ch = document.getElementsByClassName("jumbotron");
  for (var c = 0; c < ch.length; c++) {
    if (ch[c].style.display == "block") {
      ch[c].style.display = "none";
    }
    else {
      document.getElementById(aydii + "d").style.display = "block";
      document.getElementById(aydii + "d").scrollIntoView();
    }
  }

}
function handleMouseOver(aydii) {
  document.getElementById(aydii + "c").style.display = "block"
  var rec = document.getElementById(aydii).getBoundingClientRect();
  var to = rec.top + 10;
  var le = rec.left + 10;
  document.getElementById(aydii + "c").style.left = le + "px";
  document.getElementById(aydii + "c").style.top = to + "px";
}
function handleMouseOut(aydii) {
  document.getElementById(aydii + "c").style.display = "none";
}
function hMOv(aydii) {
  document.getElementById(aydii).style.display = "block"
}
function hMOu(aydii) {
  document.getElementById(aydii).style.display = "none"
}
d3.select(self.frameElement).style("height", diameter + "px");