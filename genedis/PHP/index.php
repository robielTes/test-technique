<?php
    require_once 'classes/API.php';
    include 'header.php'; // Inclut le fichier header.php

    header("Access-Control-Allow-Origin: *"); // Permet les requêtes de n'importe quel domaine
    header("Access-Control-Allow-Methods: GET, POST, OPTIONS"); // Permet les méthodes HTTP spécifiées
    header("Access-Control-Allow-Headers: Content-Type"); 

    $api = new API(); // Crée une instance de la classe API
    $installations = $api->installationsGet(); // Récupère les listes des installations
    $installations = json_decode($installations, true); // Décode le JSON en tableau associatif
?>
        <div class="chart-container">
            <h2>Installations par année</h2>
            <canvas id="barChart"></canvas>
        </div>
        <div class="chart-container">
            <h2>Répartition des capacités par propriétaire</h2>
            <canvas id="pieChart"></canvas>
        </div>
        <div class="full-width-container">
            <h2>Liste des installations</h2>
        </div>
        
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
                        if ($columnCount !=0 && $columnCount != 4) { // Ne pas afficher l'id et l'année d'installation
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
      

include 'footer.php'; // Inclut le fichier footer.php
?>

