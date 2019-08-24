window.alert('hello world')

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
var djangoData = {{ data_array|safe}}
function drawChart() {
  var data = google.visualization.arrayToDataTable(djangoData);
  var showEvery = parseInt(data.getNumberOfRows() / 3);
  var options = {
    // title: '',
    curveType: 'function',
    legend: { position: 'none' },
    backgroundColor: '#FFFFFF',
    chartArea: {'width': '85%', 'height': '70%'},
    vAxis: {
      viewWindowMode: "explicit",
      viewWindow:{ min: 0 }},

    hAxis: {
      showTextEvery: showEvery,

    },

    colors: ['#B413FE'],
    lineWidth: 3,
    vAxes: {0:
      {gridlines:
        {color: 'transparent'}
      }
    }
  };
  var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
  chart.draw(data, options);
}
