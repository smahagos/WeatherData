<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    /*function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['kentid', 'Temperature'],

    ]);

    var options = {
        title: 'Total number of each temperatures',
        legend: 'none'
    };

    var chart = new google.visualization.Histogram(document.getElementById('chart_div'));

    chart.draw(data, options);
    }*/
    function drawChart(){

    var data = google.visualization.arrayToDataTable([
        ['date', 'humidity'],
        %for item in data:
        [ {{item['kentid']}},{{int(float(item['humidity']))}} ],
        %end

    ]);

    var dataTable = new google.visualization.DataTable();
       dataTable.addColumn({ type: 'date', id: 'Date' });
       dataTable.addColumn({ type: 'number', id: 'Won/Loss' });

       dataTable.addRows([
          [ new Date(2012, 3, 13), 372],
          [ new Date(2012, 3, 13), 384]
        ]);

       var chart = new google.visualization.SteppedAreaChart(document.getElementById('chart_div'));

       var options = {
          title: 'The decline of \'The 39 Steps\'',
          vAxis: {title: 'Accumulated Rating'},
          isStacked: true
        };

       chart.draw(data, options);
    }
</script>
</head>
<body>
    <div id="chart_div" style="width: 900px; height: 500px;"></div>
</body>
