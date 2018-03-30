var i = 0;

var diameter = 1560;
var padding = 210;

var tree = d3.layout.tree()
    .size([80, diameter / 2 - padding])
    .separation(function(a, b) { return (a.parent == b.parent ? 1 : 2) / a.depth; });

var diagonal = d3.svg.diagonal.radial()
    .projection(function(d) { return [d.y, d.x / 180 * Math.PI]; });

var svg = d3.select("body").append("svg")
    .attr("width", diameter)
    .attr("height", diameter)
  .append("g")
    .attr("transform", "translate(" + diameter / 7 + "," + diameter / 1.3 + ")");

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

  // Compute the new tree layout.
  var nodes = tree.nodes(root).reverse(),
    links = tree.links(nodes);


  // Normalize for fixed-depth.
  nodes.forEach(function(d) { d.y = d.depth * 300; });

  // Declare the nodes…
  var node = svg.selectAll("g.node")
    .data(nodes, function(d) { return d.id || (d.id = ++i); });

  var ad = function(d) { return d.aydi; };
  var ads = function(d) { return (d.aydi + "c1"); };
  // Enter the nodes.
  var nodeEnter = node.enter().append("g")
    .attr("class", "node")
    .attr("id", ads)
    .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + d.y + ")"; })
    ;

  nodeEnter.append("circle")
    .attr("r", 7)
    .attr("id", ad)
    .attr("onmouseover", 'handleMouseOver(this.id)')
    .attr("onmouseout", 'handleMouseOut(this.id)')
    .attr("onclick", 'handleClick(this.id)');

  nodeEnter.append("text")
    .attr("x", function(d) {
      return d.children || d._children ? -13 : 13; })
    .attr("dy", ".35em")
    .attr("text-anchor", function(d) { return d.x < 180 ? "start" : "end"; })
    .attr("transform", function(d) { return d.x < 180 ? "translate(30)" : "rotate(180)translate(-30)"; })
    .text(function(d) { return d.name; })
    .style("fill-opacity", 1);


  // Declare the links…
  var link = svg.selectAll("path.link")
    .data(links, function(d) { return d.target.id; });


  // Enter the links.
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