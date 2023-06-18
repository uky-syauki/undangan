// Color Variableslet cardColor, headingColor, labelColor, borderColor, legendColor;

// if (isDarkStyle) {
//     cardColor = config.colors_dark.cardColor;
//     headingColor = config.colors_dark.headingColor;
//     labelColor = config.colors_dark.textMuted;
//     legendColor = config.colors_dark.bodyColor;
//     borderColor = config.colors_dark.borderColor;
//   } else {
cardColor = config.colors.cardColor;
headingColor = config.colors.headingColor;
labelColor = config.colors.textMuted;
legendColor = config.colors.bodyColor;
borderColor = config.colors.borderColor;
cyanColor = "rgb(0,188,227)";

let max = (arr) => {
  n = 0;
  for (let i = 0; i < arr.length; i++){
      if (n < arr[i]){
          n = arr[i];
      }
  }
  return n;
};
let besar = max(yVal)
//   }
  const barChart = document.getElementById('barChart');
  if (barChart) {
    const barChartVar = new Chart(barChart, {
      type: 'bar',
      data: {
        labels: xVal,
        datasets: [
          {
            data: yVal, //[275, 90, 190, 205, 125, 85, 55, 87, 127, 150, 230, 280, 190],
            backgroundColor: cyanColor,
            borderColor: 'transparent',
            maxBarThickness: 15,
            borderRadius: {
              topRight: 15,
              topLeft: 15
            }
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          duration: (besar+besar) //500
        },
        plugins: {
          tooltip: {
            rtl: true, //isRtl,
            backgroundColor: cardColor,
            titleColor: headingColor,
            bodyColor: legendColor,
            borderWidth: 1,
            borderColor: borderColor
          },
          legend: {
            display: false
          }
        },
        scales: {
          x: {
            grid: {
              color: borderColor,
              drawBorder: false,
              borderColor: borderColor
            },
            ticks: {
              color: labelColor
            }
          },
          y: {
            min: 0,
            max: 400,
            grid: {
              color: borderColor,
              drawBorder: false,
              borderColor: borderColor
            },
            ticks: {
              stepSize: 100,
              color: labelColor
            }
          }
        }
      }
    });
  }