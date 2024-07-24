
$(document).ready(function() {
    const pieChart = document.getElementById('pieChart');
    const barChart = document.getElementById('barChart');

    const installationsAnneeInstallationURL = `http://localhost:8081/installations/anneeInstallation`;
    const installationsByCapacityURL = `http://localhost:8081/installations/capacite`;

    function fetchPieChartData() {
        return $.ajax({
            url: installationsAnneeInstallationURL,
            method: 'GET',
            dataType: 'json'
        });
    }

    function fetchBarChartData() {
        return $.ajax({
            url: installationsByCapacityURL,
            method: 'GET',
            dataType: 'json'
        });
    }

    function transformData(rawData) {
        const labels = [];
        const values = [];
        
        rawData.forEach(item => {
            labels.push(item[0]); // First element is the label
            values.push(item[1]); // Second element is the value
        });
        
        return {
            labels: labels,
            values: values
        };
    }

    function updatePieChart(chart, data) {
        const transformedData = transformData(data);
        
        if (transformedData && Array.isArray(transformedData.labels) && Array.isArray(transformedData.values)) {
            chart.data.labels = transformedData.labels;
            chart.data.datasets[0].data = transformedData.values;
            chart.update();
        } else {
            console.error('Invalid data format for Pie Chart:', transformedData);
        }
    }

    function updateBarChart(chart, data) {
        const transformedData = transformData(data);
        
        if (transformedData && Array.isArray(transformedData.labels) && Array.isArray(transformedData.values)) {
            chart.data.labels = transformedData.labels;
            chart.data.datasets[0].data = transformedData.values;
            chart.update();
        } else {
            console.error('Invalid data format for Bar Chart:', transformedData);
        }
    }

    const pieChartInstance = new Chart(pieChart, {
        type: 'pie',
        data: {
            labels: [],
            datasets: [{
                label: 'Installation Years',
                data: [],
                backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(54, 162, 235)',
                    'rgb(255, 205, 86)',
                    'rgb(75, 192, 192)',
                    'rgb(153, 102, 255)',
                    'rgb(255, 159, 64)'
                ],
                hoverOffset: 4
            }]
        },
    });

    const barChartInstance = new Chart(barChart, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Capacity of Installations',
                data: [],
                borderWidth: 1,
                backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(54, 162, 235)',
                    'rgb(255, 205, 86)',
                    'rgb(75, 192, 192)',
                    'rgb(153, 102, 255)',
                    'rgb(255, 159, 64)'
                ],
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    fetchPieChartData().done(function(data) {
        console.log("Pie Chart Data:", data);  // Log data to inspect its structure
        updatePieChart(pieChartInstance, data);
    }).fail(function(jqXHR, textStatus, errorThrown) {
        console.error('Failed to fetch Pie Chart data:', textStatus, errorThrown);
    });

    fetchBarChartData().done(function(data) {
        console.log("Bar Chart Data:", data);  // Log data to inspect its structure
        updateBarChart(barChartInstance, data);
    }).fail(function(jqXHR, textStatus, errorThrown) {
        console.error('Failed to fetch Bar Chart data:', textStatus, errorThrown);
    });
});