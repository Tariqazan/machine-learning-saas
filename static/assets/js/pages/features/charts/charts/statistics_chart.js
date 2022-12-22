new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
    labels: ["Machine1", "Machine2", "Machine3", "Machine4", "Machine5", "Machine6"],
    datasets: [{
      data: [1000, 2000, 3000, 4000, 5000, 6000],
      label: "Machine1",
      borderColor: "#3e95cd",
      fill: false
    }, {
      data: [282, 3500, 411, 502, 1402, 3700, 5267],
      label: "Machine2",
      borderColor: "#8e5ea2",
      fill: false
    }, {
      data: [1068, 1700, 1708, 1900, 2003, 2076, 408, 5047, 6705, 734],
      label: "Machine3",
      borderColor: "#3cba9f",
      fill: false
    }, {
      data: [40, 20, 10, 16, 24, 38, 74, 167, 508, 784],
      label: "Machine4",
      borderColor: "#e8c3b9",
      fill: false
    }, {
      data: [600, 300, 200, 280, 7, 260, 820, 172, 312, 433],
      label: "Machine5",
      borderColor: "#c45850",
      fill: false
    },
    {
      data: [60, 30, 20, 26, 70, 26, 82, 172, 312, 433],
      label: "Machine6",
      borderColor: "#c45850",
      fill: false
    }
    ]
  },
  options: {
    title: {
      display: false,
      text: 'World population per region (in millions)'
    }
  }
});

new Chart(document.getElementById("line-chart2"), {
  type: 'line',
  data: {
    labels: ["Machine1", "Machine2", "Machine3", "Machine4", "Machine5", "Machine6"],
    datasets: [{
      data: [1000, 2000, 3000, 400, 1000, 600],
      label: "Operator",
      borderColor: "#3e95cd",
      fill: false
    }
    ]
  },
  options: {
    title: {
      display: false,
      text: 'World population per region (in millions)'
    }
  }
});

new Chart(document.getElementById("pie-chart"), {
  type: 'pie',
  data: {
    labels: ["Remaining", "Completed"],
    datasets: [{
      label: "Population (millions)",
      backgroundColor: ["#3e95cd", "#8e5ea2"],
      data: [2478, 5267]
    }]
  },
  options: {
    title: {
      display: true,
      text: 'Current Production'
    }
  }
});

new Chart(document.getElementById("polar-chart"), {
  type: 'polarArea',
  data: {
    labels: ["Maintainance", "Running", "OFF", "Idle"],
    datasets: [
      {
        label: "Machine Status",
        backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9"],
        data: [2478, 5267, 2634, 1584]
      }
    ]
  },
  options: {
    title: {
      display: false,
      text: 'Predicted world population (millions) in 2050'
    }
  }
});

new Chart(document.getElementById("doughnut-chart"), {
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
    title: {
      display: false,
      text: 'Predicted world population (millions) in 2050'
    }
  }
});

new Chart(document.getElementById("bar-chart-grouped"), {
  type: 'bar',
  data: {
    labels: ["January", "February", "March", "April"],
    datasets: [
      {
        label: "Start",
        backgroundColor: "#3e95cd",
        data: [133, 221, 783, 2478]
      }, {
        label: "End",
        backgroundColor: "#8e5ea2",
        data: [408, 547, 675, 734]
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'Change in cost'
    }
  }
});

new Chart(document.getElementById("mixed-chart"), {
  type: 'bar',
  data: {
    labels: ["January", "February", "March", "April"],
    datasets: [{
      label: "Expected",
      type: "line",
      borderColor: "#8e5ea2",
      data: [408, 547, 675, 734],
      fill: false
    }, {
      label: "Produced",
      type: "line",
      borderColor: "#3e95cd",
      data: [133, 221, 783, 2478],
      fill: false
    }, {
      label: "Expected",
      type: "bar",
      backgroundColor: "#3cba9f",
      data: [408, 547, 675, 734],
    }, {
      label: "Produced",
      type: "bar",
      backgroundColor: "#e8c3b9",
      backgroundColorHover: "#3e95cd",
      data: [133, 221, 783, 2478]
    }
    ]
  },
  options: {
    title: {
      display: false,
      text: 'Population growth (millions): Europe & Africa'
    },
    legend: { display: true }
  }
});

new Chart(document.getElementById("mixed-chart2"), {
  type: 'bar',
  data: {
    labels: ["January", "February", "March", "April"],
    datasets: [{
      label: "Expected",
      type: "line",
      borderColor: "#8e5ea2",
      data: [408, 547, 675, 734],
      fill: false
    }, {
      label: "Produced",
      type: "line",
      borderColor: "#3e95cd",
      data: [133, 221, 783, 2478],
      fill: false
    }, {
      label: "Expected",
      type: "bar",
      backgroundColor: "#3cba9f",
      data: [408, 547, 675, 734],
    }, {
      label: "Produced",
      type: "bar",
      backgroundColor: "#e8c3b9",
      backgroundColorHover: "#3e95cd",
      data: [133, 221, 783, 2478]
    }
    ]
  },
  options: {
    title: {
      display: false,
      text: 'Population growth (millions): Europe & Africa'
    },
    legend: { display: true }
  }
});

new Chart(document.getElementById("bar-chart1"), {
  type: 'bar',
  data: {
    labels: ["Machine1", "Machine2", "Machine3", "Machine4", "Machine5"],
    datasets: [
      {
        label: "Daily Production",
        backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
        data: [2478, 5267, 734, 784, 433]
      }
    ]
  },
  options: {
    legend: { display: false },
    title: {
      display: true,
      text: 'Production Per day'
    }
  }
});

new Chart(document.getElementById("bar-chart2"), {
  type: 'bar',
  data: {
    labels: ["January", "February", "March", "April","May", "June", "July", "August","September", "October", "November", "December"],
    datasets: [
      {
        label: "Returned Item",
        backgroundColor: ["#35cd", "#5ea2", "#ba9f", "#e8b9","#35cd", "#5ea2", "#ba9f", "#e8b9","#35cd", "#5ea2", "#ba9f", "#e8b9"],
        data: [2478, 5267, 2634, 1584,2478, 5267, 2634, 1584,2478, 5267, 2634, 1584]
      }
    ]
  },
  options: {
    title: {
      display: false,
      text: 'Predicted world population (millions) in 2050'
    }
  }
});

new Chart(document.getElementById("bar-chart3"), {
  type: 'bar',
  data: {
    labels: ["January", "February", "March", "April","May", "June", "July", "August","September", "October", "November", "December"],
    datasets: [
      {
        label: "Defect Items",
        backgroundColor: ["#35cd", "#5ea2", "#ba9f", "#e8b9","#35cd", "#5ea2", "#ba9f", "#e8b9","#35cd", "#5ea2", "#ba9f", "#e8b9"],
        data: [2478, 5267, 2634, 1584,2478, 5267, 2634, 1584,2478, 5267, 2634, 1584]
      }
    ]
  },
  options: {
    title: {
      display: false,
      text: 'Predicted world population (millions) in 2050'
    }
  }
});