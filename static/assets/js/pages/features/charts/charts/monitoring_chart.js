new Chart(document.getElementById("half-doughnut-chart-temp"), {
  type: 'doughnut',
  data: {
    labels: ["Availibilty", "Productivity", "Rejectlines"],
    datasets: [
      {
        label: "Population (millions)",
        backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f"],
        data: [2478, 5267, 734]
      }
    ]
  },
  options: {
    rotation: 1 * Math.PI,
            circumference: 1 * Math.PI,
            legend: {
                display: false
            },
            tooltip: {
                enabled: false
            },
            cutoutPercentage: 65,
    title: {
      display: false,
      text: 'Predicted world population (millions) in 2050'
    }
  }
});


new Chart(document.getElementById("half-doughnut-chart-humidity"), {
  type: 'doughnut',
  data: {
    labels: ["Availibilty", "Productivity", "Rejectlines"],
    datasets: [
      {
        label: "Population (millions)",
        backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f"],
        data: [2478, 5267, 734]
      }
    ]
  },
  options: {
    rotation: 1 * Math.PI,
            circumference: 1 * Math.PI,
            legend: {
                display: false
            },
            tooltip: {
                enabled: false
            },
            cutoutPercentage: 65,
    title: {
      display: false,
      text: 'Predicted world population (millions) in 2050'
    }
  }
});


new Chart(document.getElementById("half-doughnut-chart-pm2"), {
  type: 'doughnut',
  data: {
    labels: ["Availibilty", "Productivity", "Rejectlines"],
    datasets: [
      {
        label: "Population (millions)",
        backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f"],
        data: [2478, 5267, 734]
      }
    ]
  },
  options: {
    rotation: 1 * Math.PI,
            circumference: 1 * Math.PI,
            legend: {
                display: false
            },
            tooltip: {
                enabled: false
            },
            cutoutPercentage: 65,
    title: {
      display: false,
      text: 'Predicted world population (millions) in 2050'
    }
  }
});


new Chart(document.getElementById("half-doughnut-chart-pm10"), {
  type: 'doughnut',
  data: {
    labels: ["Availibilty", "Productivity", "Rejectlines"],
    datasets: [
      {
        label: "Population (millions)",
        backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f"],
        data: [2478, 5267, 734]
      }
    ]
  },
  options: {
    rotation: 1 * Math.PI,
            circumference: 1 * Math.PI,
            legend: {
                display: false
            },
            tooltip: {
                enabled: false
            },
            cutoutPercentage: 65,
    title: {
      display: false,
      text: 'Predicted world population (millions) in 2050'
    }
  }
});



var downtown = document.getElementById("downtown").getContext("2d");

var downtown = new Chart(downtown, {
  type: 'bar',
  data: {
    labels: ['Machine1', 'Machine2', 'Machine3', 'Machine4', 'Machine5', 'Machine6'],
    datasets: [{
      label: 'Downtown Per Day(Hours)',
      backgroundColor: "#000080",
      data: [9, 5, 1, 2, 4, 2]
    }]
  },

  options: {
    legend: {
      display: true,
      position: 'top',
      labels: {
        fontColor: "#000080",
      }
    },
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
});





