var options = {
    series: [{
        name: "Fuel",
        data: [10, 41, 35, 51, 49, 62, 69, 91, 148, 21, 132, 75]
    }],
    chart: {
        height: 350,
        type: 'line',
        zoom: {
            enabled: false
        }
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        curve: 'straight'
    },
    title: {
        text: 'Fuel Usage Per Month',
        align: 'left'
    },
    grid: {
        row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.5
        },
    },
    tooltip: {
        y: {
            formatter: function(val) {
                return val + " ltr"
            }
        }
    },
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    }
};

var chart = new ApexCharts(document.querySelector("#monthly_use_of_fuel"), options);
chart.render();


var options = {
    series: [{
        name: 'Total Cost',
        data: [35, 41, 36, 26, 45, 48, 52, 53, 41, 21, 35]
    }],
    chart: {
        type: 'bar',
        height: 350
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '55%',
            endingShape: 'rounded'
        },
    },
    dataLabels: {
        enabled: false
    },

    title: {
        text: 'Fuel Cost Per Month',
        align: 'left'
    },
    stroke: {
        show: true,
        width: 2,
        colors: ['transparent']
    },
    xaxis: {
        categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    yaxis: {
        title: {
            text: ' (thousands)'
        }
    },
    fill: {
        opacity: 1
    },
    tooltip: {
        y: {
            formatter: function(val) {
                return val + " thousands"
            }
        }
    },
    colors: [success]
};

var chart = new ApexCharts(document.querySelector("#monthly_cost_of_fuel"), options);
chart.render();