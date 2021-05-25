
    d3.json('/static/data/data_count.json', function(data) {
    data = MG.convert.date(data, "date","%Y-%m-%d %H:%M:%S");

    var markers = [{
        'date': new Date('2020-05-08T00:00:00.000Z'),
        'label': '1st Milestone'
    }, {
        'date': new Date('2020-05-12T00:00:00.000Z'),
        'label': '2nd Milestone'
    }];

    MG.data_graphic({
        // title: "Markers",
        description: "Markers are vertical lines that can be added at arbitrary points. Markers that are close to each other won't collide.",
        data: data,
        chart_type: 'point',
        width: 500,
        height: 150,
        right: 40,
        markers: markers,
        // format: 'percentage',
        target: document.getElementById('data_count'),
        x_accessor: 'date',
        y_accessor: 'value',
        brushing: true,
    });
});