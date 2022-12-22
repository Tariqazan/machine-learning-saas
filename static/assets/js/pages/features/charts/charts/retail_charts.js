var Data = []
var endpoint = "/api/data11/";
var label = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label.push(key);
      Data.push(value);
    });
    new Chart(document.getElementById("retail_1"), {
      type: 'bar',
      data: {
        labels: label,
        datasets: [
          {
            label: "Best Selling",
            backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
            data: Data
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Best Selling'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});


var Data = []
var endpoint = "/api/data12/";
var label = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label.push(key);
      Data.push(value);
    });
    new Chart(document.getElementById("retail_2"), {
      type: 'bar',
      data: {
        labels: label,
        datasets: [
          {
            label: "Best Selling",
            backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
            data: Data
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Best Selling'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});

var Data = []
var endpoint = "/api/data13/";
var label = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label.push(key);
      Data.push(value);
    });
    new Chart(document.getElementById("retail_3"), {
      type: 'bar',
      data: {
        labels: label,
        datasets: [
          {
            label: "Best Selling",
            backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
            data: Data
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Best Selling'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});


var Data = []
var endpoint = "/api/data14/";
var label = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label.push(key);
      Data.push(value);
    });
    new Chart(document.getElementById("retail_4"), {
      type: 'bar',
      data: {
        labels: label,
        datasets: [
          {
            label: "Best Selling",
            backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
            data: Data
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Best Selling'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});

var Data = []
var endpoint = "/api/data15/";
var label = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label.push(key);
      Data.push(value);
    });
    new Chart(document.getElementById("retail_5"), {
      type: 'bar',
      data: {
        labels: label,
        datasets: [
          {
            label: "Best Selling",
            backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
            data: Data
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Best Selling'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});