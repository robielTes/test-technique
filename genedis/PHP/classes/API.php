<?php

class API {

    // get Installations
    public function installationsGet() {
        $url = 'http://' . $_SERVER['SERVER_NAME'] . ':8081/installations';
        $response = file_get_contents($url);
        return $response;

    }

    // get Installations with a property id
    public function installationsParProprietaireGet($id) {
        $url = 'http://' . $_SERVER['SERVER_NAME'] . ':8081/installations/' . $id;
        $response = file_get_contents($url);
        return $response;
    }

    // get properties
    public function proprietairesGet() {
        $url = 'http://' . $_SERVER['SERVER_NAME'] . ':8081/proprietaires';
        $response = file_get_contents($url);
        return $response;
    }

    // create an installation
    public function createInstallationPost($nom, $commune, $capacite, $anneeInstallation, $idProprietaire) {
        $url = 'http://' . $_SERVER['SERVER_NAME'] . ':8081/installations';
        $data = array('nom' => $nom, 'commune' => $commune, 'capacite' => $capacite, 'anneeInstallation' => $anneeInstallation, 'idProprietaire' => $idProprietaire);
        $options = array(
            'http' => array(
                'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
                'method'  => 'POST',
                'content' => http_build_query($data)
            )
        );
        $context  = stream_context_create($options);
        $response = file_get_contents($url, false, $context);
        return $response;
    }
    //create a property
    public function createPropertyPost($nom) {
        $url = 'http://' . $_SERVER['SERVER_NAME'] . ':8081/proprietaires';
        $data = array('nom' => $nom);
        $options = array(
            'http' => array(
                'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
                'method'  => 'POST',
                'content' => http_build_query($data)
            )
        );
        $context  = stream_context_create($options);
        $response = file_get_contents($url, false, $context);
        return $response;
    }

    //installations by year
    public function installationsAnneeInstallationGet() {
        $url = 'http://' . $_SERVER['SERVER_NAME'] . ':8081/installations/anneeInstallation';
        $response = file_get_contents($url);
        return $response;
    }

    //installations by capacity
    public function getInstallationsByCapacity() {
        $url = 'http://' . $_SERVER['SERVER_NAME'] . ':8081/installations/capacite';
        $response = file_get_contents($url);
        return $response;
    }


}

?>
