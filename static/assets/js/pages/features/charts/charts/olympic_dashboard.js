  var options = {
      series: [{
          name: 'Monthly Count',
          data: [{
                  x: 'Product 1',
                  y: 1292,
              },
              {
                  x: 'Product 2',
                  y: 4432,
              },
              {
                  x: 'Product 3',
                  y: 5423,
              },
              {
                  x: 'Product 4',
                  y: 6653,
              },
              {
                  x: 'Product 5',
                  y: 8133,
              },
              {
                  x: 'Product 6',
                  y: 7132,
              },
              {
                  x: 'Product 7',
                  y: 7332,
              },
          ]
      }],
      chart: {
          height: 350,
          type: 'bar'
      },
      plotOptions: {
          bar: {
              columnWidth: '60%'
          }
      },
      colors: ['#00E396'],
      dataLabels: {
          enabled: false
      },
      legend: {
          show: true,
          showForSingleSeries: true,
          customLegendItems: ['Actual', 'Expected'],
          markers: {
              fillColors: ['#00E396', '#775DD0']
          }
      }
  };

  var chart = new ApexCharts(document.querySelector("#monthly_chart_count"), options);
  chart.render();

  var options = {
      series: [{
          name: 'Weekly Count',
          data: [{
                  x: 'Product 1',
                  y: 1292,
              },
              {
                  x: 'Product 2',
                  y: 4432,
              },
              {
                  x: 'Product 3',
                  y: 5423,
              },
              {
                  x: 'Product 4',
                  y: 6653,
              },
              {
                  x: 'Product 5',
                  y: 8133,
              },
              {
                  x: 'Product 6',
                  y: 7132,
              },
              {
                  x: 'Product 7',
                  y: 7332,
              },
          ]
      }],
      chart: {
          height: 350,
          type: 'bar'
      },
      plotOptions: {
          bar: {
              columnWidth: '60%'
          }
      },
      colors: ['#00E396'],
      dataLabels: {
          enabled: false
      },
      legend: {
          show: true,
          showForSingleSeries: true,
          customLegendItems: ['Actual', 'Expected'],
          markers: {
              fillColors: ['#00E396', '#775DD0']
          }
      }
  };

  var chart = new ApexCharts(document.querySelector("#weekly_chart_count"), options);
  chart.render();

  var options = {
      series: [{
          name: 'Daily Count',
          data: [{
                  x: 'Product 1',
                  y: 1292,
              },
              {
                  x: 'Product 2',
                  y: 4432,
              },
              {
                  x: 'Product 3',
                  y: 5423,
              },
              {
                  x: 'Product 4',
                  y: 6653,
              },
              {
                  x: 'Product 5',
                  y: 8133,
              },
              {
                  x: 'Product 6',
                  y: 7132,
              },
              {
                  x: 'Product 7',
                  y: 7332,
              },
          ]
      }],
      chart: {
          height: 350,
          type: 'bar'
      },
      plotOptions: {
          bar: {
              columnWidth: '60%'
          }
      },
      colors: ['#00E396'],
      dataLabels: {
          enabled: false
      },
      legend: {
          show: true,
          showForSingleSeries: true,
          customLegendItems: ['Actual', 'Expected'],
          markers: {
              fillColors: ['#00E396', '#775DD0']
          }
      }
  };

  var chart = new ApexCharts(document.querySelector("#daily_chart_count"), options);
  chart.render();