<!doctype html>
<html lang="fr">
    <head>
        <title>Test Technique - {Tesfazghi Robiel}</title>
        <meta charset="utf-8">

        <link rel="stylesheet" href="css/custom.css">
        <script src="js/jquery.min.js"></script>
        <script src="js/custom.js"></script>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="js/charts.js" defer></script>

        <style>
        /* CSS styles for layout and canvas sizing */
        .chart-container {
            width: 49%;
            display: inline-block;
            text-align: center;
            vertical-align: top;
        }

        .chart-container canvas {
            width: 200px; 
            height: 200px; 
        }

        .full-width-container {
            width: 100%;
            text-align: center;
            vertical-align: top;
        }

        /* Make sure the canvas size is responsive */
        @media (max-width: 768px) {
            .chart-container canvas {
                width: 150px;
                height: 150px;
            }
        }
    </style>

    </head>
    <body>
        <span style="float: right;"><i>Version de l'API : v1.0.0</i></span>
        <h1  style="text-align:center; margin:10px">Installations photovoltaïques</h1>