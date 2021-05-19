// let labels1 = ['A', 'B', 'C', 'D', 'F'];
// let data1 = [69, 31];
// let colors1 = ['#49A9EA', '#36CAAB'];

// Grade Variables
// var AP = '{{ (item).AP }}'; 
// var A = '{{ (item).A }}'; 
// var AM = '{{ (item).AM }}'; 
// var BP = '{{ (item).BP }}'; 
// var B = '{{ (item).B }}'; 
// var BM = '{{ (item).BM }}'; 
// var CP = '{{ (item).CP }}'; 
// var C = '{{ (item).C }}'; 
// var CM = '{{ (item).CM }}'; 
// var DP = '{{ (item).DP }}'; 
// var D = '{{ (item).D }}'; 
// var DM = '{{ (item).DM }}'; 
// var F = '{{ (item).F }}'; 
// var W = '{{ (item).W }}'; 

// Initialize Doughnut Chart
let myDoughnutChart = document.getElementById("myChart").getContext('2d');

let chart1 = new Chart(myDoughnutChart, {
    type: 'doughnut',
    data: {

        labels: ['A', 'B', 'C', 'D', 'F'],
        datasets: [ {
            data: [
                    50,// parseInt(AP)+parseInt(A)+parseInt(AM),
                    25,// parseInt(BP)+parseInt(B)+parseInt(BM),
                    12.5,// parseInt(CP)+parseInt(C)+parseInt(CM),
                    6.25,// parseInt(DP)+parseInt(D)+parseInt(DM),
                    3.75// parseInt(F),
                ],
            backgroundColor: ['#93c47d', '#6d9eeb', '#ffd966', '#f6b26b', '#e06666']
        }]
    },
    options: {
        title: {
            text: "Chart Title",
            display: false
        },
        animation: {
            animateScale: true
        },
        responsive: true
    }


});


// Bar Graph
let labels2 = ['American Airlines Group', 'Ryanair', 'China Southern Airlines', 'Lufthansa Group'];
let data2 = [199.6, 130.3, 126.3, 130];
let colors2 = ['#49A9EA', '#36CAAB', '#34495E', '#B370CF'];

let myChart2 = document.getElementById("myChart2").getContext('2d');

let chart2 = new Chart(myChart2, {
    type: 'bar',
    data: {
        labels: ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'],
        datasets: [ {
            data: [50, 100, 150, 200, 250, 300, 350, 300, 250, 200, 150, 100, 50],
            backgroundColor: ['#49A9EA', '#36CAAB', '#34495E', '#B370CF', '#49A9EA', '#36CAAB', '#34495E', '#B370CF', '#49A9EA', '#36CAAB', '#34495E', '#B370CF', '#49A9EA']
        }]
    },
    options: {
        title: {
            text: "Number of passengers carried in 2017 (in mio.)",
            display: false
        },
        legend: {
          display: false
        },
        animation: {
            animateScale: true
        }
    }
});


let labels3 = ['Attack', 'Defense', 'Passing', 'Tackle', 'Speed'];
let myChart3 = document.getElementById("myChart3").getContext('2d');

let chart3 = new Chart(myChart3, {
    type: 'radar',
    data: {
        labels: labels3,
        datasets: [
          {
            label: 'Messi',
            fill: true,
            backgroundColor: "rgba(179, 181, 198, 0.2)",
            borderColor: "rgba(179, 181, 198, 1)",
            pointBorderColor: "#fff",
            pointBackgroundColor: "rgba(179, 181, 198, 1)",
            data: [50, 12, 55, 7, 29]
          },
          {
            label: 'Ronaldo',
            fill: true,
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgba(255, 99, 132, 1)",
            pointBorderColor: "#fff",
            pointBackgroundColor: "rgba(255, 99, 132, 1)",
            data: [51, 10, 32, 20, 44]
          }
        ]
    },
    options: {
        title: {
            text: "Skills",
            display: true
        }
    }
});

let labels4 = ['Germany', 'France', 'UK', 'Italy', 'Spain', 'Others(23)'];
let data4 = [83, 67, 66, 61, 47, 187];
let colors4 = ['#49A9EA', '#36CAAB', '#34495E', '#B370CF', '#AC5353', '#CFD4D8'];

let myChart4 = document.getElementById("myChart4").getContext('2d');

let chart4 = new Chart(myChart4, {
    type: 'pie',
    data: {
        labels: labels4,
        datasets: [ {
            data: data4,
            backgroundColor: colors4
        }]
    },
    options: {
        title: {
            text: "Population of the European Union (in mio)",
            display: true
        }
    }
});