// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';


// get the data from the server

var httpx = new XMLHttpRequest();


httpx.onreadystatechange = function(){
	
	if(this.readyState == 4 && this.status == 200){
		var response = JSON.parse(httpx.responseText);
		var high	= response['high'];
		var medium	= response['medium'];
		var low		= response['low'];
		console.log(medium);
	}
	


	// Pie Chart Example
	var ctx = document.getElementById("myPieChart");

	var myPieChart = new Chart(ctx, {
	  type: 'doughnut',
	  data: {
		labels: ["High", "Medium", "Low"],
		datasets: [{
		  data: [high, medium, low],
		  backgroundColor: ['#dc3545', '#ffc107', '#28a745'],
		  hoverBackgroundColor: ['#dc3545', '#ffc107', '#28a745'],
		  hoverBorderColor: "rgba(234, 236, 244, 1)",
		}],
	  },
	  options: {
		maintainAspectRatio: false,
		tooltips: {
		  backgroundColor: "rgb(255,255,255)",
		  bodyFontColor: "#858796",
		  borderColor: '#dddfeb',
		  borderWidth: 1,
		  xPadding: 15,
		  yPadding: 15,
		  displayColors: false,
		  caretPadding: 10,
		},
		legend: {
		  display: false
		},
		cutoutPercentage: 80,
	  },
	});
	
};

httpx.open('GET', 'statistic');
httpx.send();



