var margin = {top: 30, right: 50, bottom: 30, left: 50},
    width = screen.width/2- margin.left - margin.right,
    height = screen.height/2 - margin.top - margin.bottom;

// Parse the date / time
var parseDate = d3.time.format("%d-%b-%y").parse;

// Set the ranges
var x = d3.time.scale().range([0, width]);
var y = d3.scale.linear().range([height, 0]);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom"); // labels will appear below the axis line

var yAxis = d3.svg.axis().scale(y)
    .orient("left"); 

// Define the line
var valueline = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.close); });

// Adds the svg canvas
var svg = d3.select("#graph")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g") //group the svg shapes
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

// Get the data
// d3.tsv.parse(extractData(), function(data) {
//     console.log(data);
//     data.forEach(function(d) {
//         d.date = parseDate(d.date);
//         d.close = +d.close;
//     });

data = d3.tsv.parse(extractData(), function(data){
    return {
        date:parseDate(data.date),
        close: +data.close
    };
});

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.close; })]);

    // Add the valueline path.
    svg.append("path")
        .attr("class", "line")
        .attr("d", valueline(data));

    // Add the X Axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);

    // Add the title
    svg.append("text")
       .attr("class", "title")
       .attr("x", (width / 2))             
       .attr("y", 0 - (margin.top / 2))
       .attr("text-anchor", "middle")  
       .text("AAPL stock vs Time");
