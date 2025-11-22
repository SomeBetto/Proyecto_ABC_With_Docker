<?php

declare(strict_types=1);

final class Puestos
{

    private static string $apiUrl = "http://api:3000/puestos";

    private function __construct()
    {
    }

    private static function callApi(string $method, string $endpoint, ?array $data = null): mixed
    {
        $url = self::$apiUrl . $endpoint;
        $ch = curl_init($url);

        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method);

        if ($data) {
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
            curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
        }

        $response = curl_exec($ch);
        curl_close($ch);

        return json_decode((string) $response, true);
    }

    public static function consultaPuestoActivo(int $opcion, int $idpuesto): mixed
    {
        $endpoint = "/consulta?opcion={$opcion}&idpuesto={$idpuesto}";
        return self::callApi('GET', $endpoint);
    }

    public static function agregarPuesto(int $opcion, int $idpuesto, string $descripcion, int $empleadoalta): mixed
    {
        $data = array(
            'opcion' => $opcion,
            'idpuesto' => $idpuesto,
            'descripcion' => $descripcion,
            'empleadoalta' => $empleadoalta
        );
        return self::callApi('POST', '/agregar', $data);
    }

    public static function modificarPuesto(int $opcion, int $idpuesto, string $descripcion): mixed
    {
        $data = array(
            'opcion' => $opcion,
            'idpuesto' => $idpuesto,
            'descripcion' => $descripcion
        );
        return self::callApi('PUT', '/modificar', $data);
    }

    public static function bajaPuesto(int $opcion, int $idpuesto, int $empleadobaja): mixed
    {
        $data = array(
            'opcion' => $opcion,
            'idpuesto' => $idpuesto,
            'empleadobaja' => $empleadobaja
        );
        return self::callApi('DELETE', '/baja', $data);
    }

}