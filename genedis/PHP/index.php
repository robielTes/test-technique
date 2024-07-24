<?php
    require_once 'classes/API.php';
    include 'header.php';

    header("Access-Control-Allow-Origin: *"); // Permet les requêtes de n'importe quel domaine
    header("Access-Control-Allow-Methods: GET, POST, OPTIONS"); // Permet les méthodes HTTP spécifiées
    header("Access-Control-Allow-Headers: Content-Type"); 

    $api = new API();
    $installations = $api->installationsGet();
    $installations = json_decode($installations, true);
    
?>

        <div style="width: 49%; display: inline-block; text-align: center; vertical-align: top;">
            <h2>Installations par année</h2>
            <canvas id="barChart" width="200" height="200"></canvas>
        </div>
        <div style="width: 49%; display: inline-block; text-align: center; vertical-align: top;">
            <h2>Répartition des capacités par propriétaire</h2>
            <canvas id="pieChart" width="200" height="200"></canvas>
            </div>
        <div style="width: 100%; display: inline-block; text-align: center; vertical-align: top;">
            <h2>Liste des installations</h2>
        
        <div id="response"></div>
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

