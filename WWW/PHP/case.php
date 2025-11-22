<?php //controlador 
declare(strict_types=1);

include_once('./Clases/Empleados.php');
include_once('./Clases/Puestos.php');

$arrRespuesta = array(); //respuesta
$iOpcion = (string) filter_input(INPUT_POST, 'iOpcion'); //entrada
$opcion = (int) filter_input(INPUT_POST, 'opcion'); //entrada
$numeroempleado = (int) filter_input(INPUT_POST, 'numeroempleado'); //entrada
$nombre = (string) filter_input(INPUT_POST, 'nombre');
$appaterno = (string) filter_input(INPUT_POST, 'apellidopaterno'); //entre '' el nombre en la tabla, el post lo busca como 'apellidopaterno'
$appmaterno = (string) filter_input(INPUT_POST, 'apellidomaterno');
$direccion = (string) filter_input(INPUT_POST, 'direccion');
$codigopostal = (string) filter_input(INPUT_POST, 'codigopostal');
$telefono = (string) filter_input(INPUT_POST, 'telefono');
$curp = (string) filter_input(INPUT_POST, 'curp');
$nss = (string) filter_input(INPUT_POST, 'nss');
$puesto = (int) filter_input(INPUT_POST, 'puesto');
$causabaja = (string) filter_input(INPUT_POST, 'causabaja');
$idpuesto = (int) filter_input(INPUT_POST, 'idpuesto');
$descripcion = (string) filter_input(INPUT_POST, 'descripcion');
$empleadoalta = (int) filter_input(INPUT_POST, 'empleadoalta');
$empleadobaja = (int) filter_input(INPUT_POST, 'empleadobaja');

$arrRespuesta = match ($iOpcion) {
    //case 1-5 es para empleados
    '1' => Empleados::consultaEmpleadoActivo($opcion, $numeroempleado),
    '2' => Empleados::agregarEmpleado($opcion, $numeroempleado, $nombre, $appaterno, $appmaterno, $direccion, $codigopostal, $telefono, $curp, $nss, $puesto),
    '3' => Empleados::modificarEmpleado($opcion, $numeroempleado, $direccion, $codigopostal, $telefono, $curp, $nss, $puesto),
    '4' => Empleados::bajaEmpleado($opcion, $numeroempleado, $causabaja),

    //case 6-11 es para puestos
    '6' => Puestos::consultaPuestoActivo($opcion, $idpuesto),
    '7' => Puestos::agregarPuesto($opcion, $idpuesto, $descripcion, $empleadoalta),
    '8' => Puestos::modificarPuesto($opcion, $idpuesto, $descripcion),
    '9' => Puestos::bajaPuesto($opcion, $idpuesto, $empleadobaja),

    default => ['error' => 'Opción no válida']
};

echo json_encode($arrRespuesta);