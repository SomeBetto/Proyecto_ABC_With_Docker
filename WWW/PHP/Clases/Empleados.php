<?php

declare(strict_types=1);

final class Empleados
{

    private static string $apiUrl = "http://api:3000/empleados";

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

    public static function agregarEmpleado(int $opcion, int $numeroempleado, string $nombre, string $appaterno, string $appmaterno, string $direccion, string $codigopostal, string $telefono, string $curp, string $nss, int $puesto): mixed
    {
        $data = array(
            'opcion' => $opcion,
            'numeroempleado' => $numeroempleado,
            'nombre' => $nombre,
            'appaterno' => $appaterno,
            'appmaterno' => $appmaterno,
            'direccion' => $direccion,
            'codigopostal' => $codigopostal,
            'telefono' => $telefono,
            'curp' => $curp,
            'nss' => $nss,
            'puesto' => $puesto
        );
        return self::callApi('POST', '/agregar', $data);
    }

    public static function modificarEmpleado(int $opcion, int $numeroempleado, string $direccion, string $codigopostal, string $telefono, string $curp, string $nss, int $puesto): mixed
    {
        $data = array(
            'opcion' => $opcion,
            'numeroempleado' => $numeroempleado,
            'direccion' => $direccion,
            'codigopostal' => $codigopostal,
            'telefono' => $telefono,
            'curp' => $curp,
            'nss' => $nss,
            'puesto' => $puesto
        );
        return self::callApi('PUT', '/modificar', $data);
    }

    public static function bajaEmpleado(int $opcion, int $numeroempleado, string $causabaja): mixed
    {
        $data = array(
            'opcion' => $opcion,
            'numeroempleado' => $numeroempleado,
            'causabaja' => $causabaja
        );
        return self::callApi('DELETE', '/baja', $data);
    }

    public static function consultaEmpleadoActivo(int $opcion, int $numeroempleado): mixed
    {
        $endpoint = "/consulta?opcion={$opcion}&numeroempleado={$numeroempleado}";
        return self::callApi('GET', $endpoint);
    }

}