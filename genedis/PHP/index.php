<?php
    require_once 'classes/API.php';
    include 'header.php';

    $api = new API();
    $installations = $api->installationsGet();
    $installations = json_decode($installations, true);
    
?>

        <div style="width: 49%; display: inline-block; text-align: center; vertical-align: top;">
            <h2>Installations par année</h2>
            <canvas id="barChart" width="300" height="300"></canvas>
        </div>
        <div style="width: 49%; display: inline-block; text-align: center; vertical-align: top;">
            <h2>Répartition des capacités par propriétaire</h2>
            <canvas id="pieChart" width="300" height="300"></canvas>
            </div>
        <div style="width: 100%; display: inline-block; text-align: center; vertical-align: top;">
            <h2>Liste des installations</h2>
        
        <?php 
            if (is_array($installations) && !empty($installations)) {
                ?>
                <table style='width: 50%; margin: auto;'>
                    <thead>
                        <tr>
                            <th>Installation</th>
                            <th>Commune</th>
                            <th>Capacité</th>
                            <th>Propriétaire</th>
                        </tr>
                    </thead>
                    <tbody>                          
                <?php
                foreach ($installations as $installation) {
                    echo "<tr>";
                    $columnCount = 0;
                    foreach ($installation as $key => $value) {
                        if ($columnCount !=0 && $columnCount != 4) {
                            echo "<td>" . htmlspecialchars($value) . "</td>";
                        }
                        $columnCount++;
                    }
                    echo "</tr>";
                }
            
                echo "</table>";
            } else {
                echo "No properties found.";
            }
      
include 'footer.php';
?>



<script>
        const pieChart = document.getElementById('pieChart');
        const barChart = document.getElementById('barChart');

        new Chart(pieChart, {
            type: 'pie',
            data:  {
                labels: [
                    'Red',
                    'Blue',
                    'Yellow'
                ],
                datasets: [{
                    label: 'My First Dataset',
                    data: [300, 50, 100],
                    backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(54, 162, 235)',
                    'rgb(255, 205, 86)'
                    ],
                    hoverOffset: 4
                }]
            },
        });
        new Chart(barChart, {
            type: 'bar',
            data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3],
                borderWidth: 1
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
        </script>

    </script>
