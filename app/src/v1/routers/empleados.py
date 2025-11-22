from flask import Blueprint, jsonify, request
import uuid
from src.v1.db.conexion import conexion


empleados=Blueprint('empleados_blueprint',__name__)

@empleados.route('/agregar', methods=['POST'])
def agregar_empleado():
    try:
        data = request.json
        opcion = data.get('opcion')
        numeroempleado = data.get('numeroempleado')
        nombre = data.get('nombre')
        appaterno = data.get('appaterno')
        appmaterno = data.get('appmaterno')
        direccion = data.get('direccion')
        codigopostal = data.get('codigopostal')
        telefono = data.get('telefono')
        curp = data.get('curp')
        nss = data.get('nss')
        puesto = data.get('puesto')
        
        conn = conexion()
        conn.conectar()
        query = f"select * from fnoperacionesempleados({opcion},{numeroempleado},'{nombre}','{appaterno}','{appmaterno}','{direccion}','{codigopostal}','{telefono}','{curp}','{nss}',{puesto},'');"
        resultado = conn.ejecutarquery(query)
        conn.cerrar()
        return jsonify(resultado), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@empleados.route('/modificar', methods=['PUT'])
def modificar_empleado():
    try:
        data = request.json
        opcion = data.get('opcion')
        numeroempleado = data.get('numeroempleado')
        direccion = data.get('direccion')
        codigopostal = data.get('codigopostal')
        telefono = data.get('telefono')
        curp = data.get('curp')
        nss = data.get('nss')
        puesto = data.get('puesto')
        
        conn = conexion()
        conn.conectar()
        query = f"select * from fnoperacionesempleados({opcion},{numeroempleado},'','','','{direccion}','{codigopostal}','{telefono}','{curp}','{nss}',{puesto},'');"
        resultado = conn.ejecutarquery(query)
        conn.cerrar()
        return jsonify(resultado), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@empleados.route('/baja', methods=['DELETE'])
def baja_empleado():
    try:
        data = request.json
        opcion = data.get('opcion')
        numeroempleado = data.get('numeroempleado')
        causabaja = data.get('causabaja')
        
        conn = conexion()
        conn.conectar()
        query = f"select * from fnoperacionesempleados({opcion},{numeroempleado},'','','','','','','','',0,'{causabaja}');"
        resultado = conn.ejecutarquery(query)
        conn.cerrar()
        return jsonify(resultado), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@empleados.route('/consulta', methods=['GET'])
def consulta_empleado():
    try:
        opcion = request.args.get('opcion')
        numeroempleado = request.args.get('numeroempleado')
        
        conn = conexion()
        conn.conectar()
        query = f"select * from fnoperacionesempleados({opcion},{numeroempleado},'','','','','','','','',0,'');"
        resultado = conn.ejecutarquery(query)
        conn.cerrar()
        return jsonify(resultado), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
