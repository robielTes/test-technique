
$(document).ready(function() {
    const pieChart = document.getElementById('pieChart');
    const barChart = document.getElementById('barChart');

    const installationsAnneeInstallationURL = `http://localhost:8081/installations/anneeInstallation`;
    const installationsByCapacityURL = `http://localhost:8081/installations/capacite`;

    // Recuperation les installations par annee d'installation de l'API
    function fetchPieChartData() {
        return $.ajax({
            url: installationsAnneeInstallationURL,
            method: 'GET',
            dataType: 'json'
        });
    }

    // Recuperation les installations par capacite de l'API
    function fetchBarChartData() {
        return $.ajax({
            url: installationsByCapacityURL,
            method: 'GET',
            dataType: 'json'
        });
    }

    // Fonction pour transformer les donnees recues de l'API en format compatible avec les charts
    function transformData(rawData) {
        const labels = [];
        const values = [];
        
        rawData.forEach(item => {
            labels.push(item[0]);
            values.push(item[1]);
        });
        
        return {
            labels: labels,
            values: values
        };
    }

    // Fonction pour mettre a jour les donnees du Pie Chart
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

    // Fonction pour mettre a jour les donnees du Bar Chart
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

    // Creation des instances des charts pie des listes des installations par annee d'installation 
    const pieChartInstance = new Chart(pieChart, {
        type: 'pie',
        data: {
            labels: [],
            datasets: [{
                label: 'Les listes des installations',
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
    // Creation des instances des charts bar les capacites des installations par proprietaire
    const barChartInstance = new Chart(barChart, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'les capacites des installations',
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

    // Appel des fonctions pour mettre a jour les donnees des charts pie 
    fetchPieChartData().done(function(data) {
        updatePieChart(pieChartInstance, data);
    }).fail(function(jqXHR, textStatus, errorThrown) {
        console.error('Failed to fetch Pie Chart data:', textStatus, errorThrown);
    });

    // Appel des fonctions pour mettre a jour les donnees des charts bar
    fetchBarChartData().done(function(data) {
        updateBarChart(barChartInstance, data);
    }).fail(function(jqXHR, textStatus, errorThrown) {
        console.error('Failed to fetch Bar Chart data:', textStatus, errorThrown);
    });
});