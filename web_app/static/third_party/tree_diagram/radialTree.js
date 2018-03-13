
    var svg = d3.select("svg"),
        width = +svg.attr("width"),
        height = +svg.attr("height"),
        g = svg.append("g").attr("transform", "translate(" + (width / 2 + 40) + "," + (height / 2 + 90) + ")");

    var stratify = d3.stratify()
        .parentId(function(d) { return d.id.substring(0, d.id.lastIndexOf(".")); });

    var tree = d3.tree()
        .size([2 * Math.PI, 500])
        .separation(function(a, b) { return (a.parent == b.parent ? 1 : 2) / a.depth; });

    d3.json("celllineage.json", function(error, data) {
      if (error) throw error;

//      var root = tree(stratify(data));
      var root = data[0];
      console.log(root);
      console.log(data);

      var link = g.selectAll(".link")
        .data(root.links())
        .enter().append("path")
          .attr("class", "link")
          .attr("d", d3.linkRadial()
              .angle(function(d) { return d.x; })
              .radius(function(d) { return d.y; }));

      var node = g.selectAll(".node")
        .data(root.descendants())
        .enter().append("g")
          .attr("class", function(d) { return "node" + (d.children ? " node--internal" : " node--leaf"); })
          .attr("transform", function(d) { return "translate(" + radialPoint(d.x, d.y) + ")"; });

      var ad = function(d) { return d.data.type; };
      node.append("circle")
          .attr("r", 2.5);
          <!--.attr("id", ad);-->

      node.append("text")
          .attr("dy", "0.31em")
          .attr("x", function(d) { return d.x < Math.PI === !d.children ? 6 : -6; })
          .attr("text-anchor", function(d) { return d.x < Math.PI === !d.children ? "start" : "end"; })
          .attr("transform", function(d) { return "rotate(" + (d.x < Math.PI ? d.x - Math.PI / 2 : d.x + Math.PI / 2) * 180 / Math.PI + ")"; })
          .text(function(d) { return d.id.substring(d.id.lastIndexOf(".") + 1); });
    });

    function radialPoint(x, y) {
      return [(y = +y) * Math.cos(x -= Math.PI / 2), y * Math.sin(x)];
    }
