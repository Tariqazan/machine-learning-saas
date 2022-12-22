window.onload = function() {
    var dataLength = 20; // number of dataPoints visible at any point
    var updateInterval = 1000;

    // Temparature
    var temparature = [];
    var temparature_chart = new CanvasJS.Chart("temparature", {
        animationEnabled: true,
        theme: 'light2',
        title: {
            text: "Temparature"
        },
        data: [{
            type: "area",
            dataPoints: temparature
        }]
    });

    var temparature_value = 0;
    var temparature_axis = 1;

    var updatetempChart = function() {
        $.ajax({
            url: "/industry/data/",
            success: function(data) {
                for (var j = 0; j < data.temparature.length; j++) {
                    temparature_value = parseInt(data.temparature[j][1]);
                    temparature.push({
                        x: temparature_axis,
                        y: temparature_value
                    });
                    temparature_axis++;
                    if (temparature.length > dataLength) {
                        temparature.shift();
                    }
                }
            }
        })
        temparature_chart.render();
    };

    updatetempChart(dataLength);
    setInterval(function() {
        updatetempChart()
    }, updateInterval);



    // Humidity 
    var humidity = [];
    var humidity_chart = new CanvasJS.Chart("humidity", {
        animationEnabled: true,
        theme: 'light2',
        title: {
            text: "Humidity"
        },
        data: [{
            type: "line",
            dataPoints: humidity
        }]
    });

    var humidity_value = 0;
    var humidity_axis = 1;

    var updatehumidityChart = function() {
        $.ajax({
            url: "/industry/data/",
            success: function(data) {
                for (var j = 0; j < data.humidity.length; j++) {
                    humidity_value = parseInt(data.humidity[j][1]);
                    humidity.push({
                        x: humidity_axis,
                        y: humidity_value
                    });
                    humidity_axis++;
                    if (humidity.length > dataLength) {
                        humidity.shift();
                    }
                }
            }
        })
        humidity_chart.render();
    };

    updatehumidityChart(dataLength);
    setInterval(function() {
        updatehumidityChart()
    }, updateInterval);

    // Weight
    var weight = [];
    var weight_chart = new CanvasJS.Chart("weight", {
        animationEnabled: true,
        theme: 'light2',
        title: {
            text: "Weight"
        },
        data: [{
            type: "column",
            dataPoints: weight
        }]
    });

    var weight_value = 0;
    var weight_axis = 1;

    var updateweightChart = function() {
        $.ajax({
            url: "/industry/data/",
            success: function(data) {
                for (var j = 0; j < data.weight.length; j++) {
                    weight_value = parseInt(data.weight[j][1]);
                    weight.push({
                        x: weight_axis,
                        y: weight_value
                    });
                    weight_axis++;
                    if (weight.length > dataLength) {
                        weight.shift();
                    }
                }
            }
        })
        weight_chart.render();
    };

    updateweightChart(dataLength);
    setInterval(function() {
        updateweightChart()
    }, updateInterval);



    // humidity Temparature
    var pressure = [];
    var pressure_chart = new CanvasJS.Chart("pressure", {
        animationEnabled: true,
        theme: 'light2',
        title: {
            text: "pressure"
        },
        data: [{
            type: "line",
            dataPoints: pressure
        }]
    });

    var pressure_value = 0;
    var pressure_axis = 1;

    var updatepressureChart = function() {
        $.ajax({
            url: "/industry/data/",
            success: function(data) {
                for (var j = 0; j < data.pressure.length; j++) {
                    pressure_value = parseInt(data.pressure[j][1]);
                    pressure.push({
                        x: pressure_axis,
                        y: pressure_value
                    });
                    pressure_axis++;
                    if (pressure.length > dataLength) {
                        pressure.shift();
                    }
                }
            }
        })
        pressure_chart.render();
    };

    updatepressureChart(dataLength);
    setInterval(function() {
        updatepressureChart()
    }, updateInterval);
}