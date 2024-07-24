<?php
    require_once 'classes/API.php';
    include 'header.php';

    $api = new API();
    $installations = $api->getInstallations();
    $installations = json_decode($installations, true);
    
?>

        <div style="width: 49%; display: inline-block; text-align: center; vertical-align: top;">
            <h2>Installations par année</h2>
            <img src="media/bar.png" style="width: 670px;">
        </div>
        <div style="width: 49%; display: inline-block; text-align: center; vertical-align: top;">
            <h2>Répartition des capacités par propriétaire</h2>
            <img src="media/pie.png" style="width: 350px;">
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
