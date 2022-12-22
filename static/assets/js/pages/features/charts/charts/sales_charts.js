var Data = []
var endpoint = "/api/data1/";
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
    new Chart(document.getElementById("bar-chart2"), {
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




var Data1 = []
var endpoint = "/api/data2/";
var label1 = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label1.push(key);
      Data1.push(value);
    });
    new Chart(document.getElementById("bar-chart3"), {
      type: 'bar',
      data: {
        labels: label1,
        datasets: [
          {
            label: "Which stock codes were used the most",
            backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
            data: Data1
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Which stock codes were used the most'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});


var Data2 = []
var endpoint = "/api/data3/";
var label2 = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label2.push(key);
      Data2.push(value);
    });
    new Chart(document.getElementById("bar-chart4"), {
      type: 'line',
      data: {
        labels: label2,
        datasets: [
          {
            label: "Which Countries Made The Most Transactions",
            borderColor: 'rgba(100, 220, 420, 0.9)',
            data: Data2
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Which Countries Made The Most Transactions'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});



var Data3 = []
var endpoint = "/api/data4/";
var label3 = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label3.push(key);
      Data3.push(value);
    });
    new Chart(document.getElementById("bar-chart5"), {
      type: 'bar',
      data: {
        labels: label3,
        datasets: [
          {
            label: "Which Invoices Had The Most Item",
            backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850", "#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
            data: Data3
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Which Invoices Had The Most Item'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});



var Data5 = []
var endpoint = "/api/data5/";
var label5 = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label5.push(key);
      Data5.push(value);
    });
    new Chart(document.getElementById("bar-chart6"), {
      type: 'line',
      data: {
        labels: label5,
        datasets: [
          {
            label: "Which Invoices Had The Most Item",
            // backgroundColor: 'rgba(100, 220, 0, 0.1)',
            borderColor: 'rgba(100, 220, 420, 0.9)',
            data: Data5
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Per Month Sales Amount'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});

var Data6 = []
var endpoint = "/api/data6/";
var label6 = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label6.push(key);
      Data6.push(value);
    });
    new Chart(document.getElementById("bar-chart7"), {
      type: 'bar',
      data: {
        labels: label6,
        datasets: [
          {
            label: "Which Invoices Had The Most Item",
            backgroundColor: 'rgba(100, 220,210, 0.8)',
            // borderColor: 'rgba(100, 220, 420, 0.9)',
            data: Data6
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Revenue Per Country'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});



var Data7 = []
var endpoint = "/api/data7/";
var label7 = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label7.push(key);
      Data7.push(value);
    });
    new Chart(document.getElementById("bar-chart8"), {
      type: 'bar',
      data: {
        labels: label7,
        datasets: [
          {
            label: "Which Invoices Had The Most Item",
            backgroundColor: 'rgba(100, 20,10, 0.8)',
            // borderColor: 'rgba(100, 220, 420, 0.9)',
            data: Data7
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Customer Behaviour Analysis'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});




var Data8 = []
var endpoint = "/api/data8/";
var label8 = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label8.push(key);
      Data8.push(value);
    });
    new Chart(document.getElementById("bar-chart9"), {
      type: 'bar',
      data: {
        labels: label8,
        datasets: [
          {
            label: "Which Invoices Had The Most Item",
            backgroundColor: 'rgba(160, 20,210, 0.8)',
            // borderColor: 'rgba(100, 220, 420, 0.9)',
            data: Data8
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Quantity of Items Per Invoice'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});



var Data9 = []
var endpoint = "/api/data9/";
var label9 = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label9.push(key);
      Data9.push(value);
    });
    new Chart(document.getElementById("bar-chart10"), {
      type: 'bar',
      data: {
        labels: label9,
        datasets: [
          {
            label: "Which Invoices Had The Most Item",
            backgroundColor: 'rgba(160, 20,210, 0.8)',
            // borderColor: 'rgba(100, 220, 420, 0.9)',
            data: Data9
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Quantity of Items Per Invoice'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});



var Data10 = []
var endpoint = "/api/data11/";
var label10 = []

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    const objectArray = Object.entries(data);

    objectArray.forEach(([key, value]) => {
      label10.push(key);
      Data10.push(value);
    });
    new Chart(document.getElementById("bar-chart11"), {
      type: 'bar',
      data: {
        labels: label10,
        datasets: [
          {
            label: "Which Invoices Had The Most Item",
            backgroundColor: 'rgba(160, 20,210, 0.8)',
            // borderColor: 'rgba(100, 220, 420, 0.9)',
            data: Data10
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Quantity of Items Per Invoice'
        }
      }
    });
  },
  error: function (data) {
    // alert the error if any error occured
    alert('Api not found');
  }

});