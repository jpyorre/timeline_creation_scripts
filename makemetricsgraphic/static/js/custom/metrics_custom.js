d3.json('/static/data/query_count.json', function(data) {
    data = MG.convert.date(data, "date","%Y-%m-%d %H:%M:%S"); 
    console.log(data)
    MG.data_graphic({
      title: "Total Queries by day",
      chart_type: 'line',
      // description: "All Domains",
      data: data,
      width: 600,
      height: 200,
      right: 40,
      target: document.getElementById('total_queries'),
      x_accessor: 'date',
      y_accessor: 'value',
      brushing: true
      // x_label: ['All Domains']
    });
  });
