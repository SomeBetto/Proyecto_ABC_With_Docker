from flask import Blueprint, jsonify, request
from src.v1.db.conexion import conexion

puestos = Blueprint('puestos_blueprint', __name__)

@puestos.route('/consulta', methods=['GET'])
def consulta_puesto():
    try:
        opcion = request.args.get('opcion')
        idpuesto = request.args.get('idpuesto')
        
        conn = conexion()
        conn.conectar()
        query = f"select * from fnoperacionespuestos({opcion},{idpuesto},'',0,0);"
        resultado = conn.ejecutarquery(query)
        conn.cerrar()
        return jsonify(resultado), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@puestos.route('/agregar', methods=['POST'])
def agregar_puesto():
    try:
        data = request.json
        opcion = data.get('opcion')
        idpuesto = data.get('idpuesto')
        descripcion = data.get('descripcion')
        empleadoalta = data.get('empleadoalta')
        
        conn = conexion()
        conn.conectar()
        query = f"select * from fnoperacionespuestos({opcion},{idpuesto},'{descripcion}',{empleadoalta},0);"
        resultado = conn.ejecutarquery(query)
        conn.cerrar()
        return jsonify(resultado), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@puestos.route('/modificar', methods=['PUT'])
def modificar_puesto():
    try:
        data = request.json
        opcion = data.get('opcion')
        idpuesto = data.get('idpuesto')
        descripcion = data.get('descripcion')
        
        conn = conexion()
        conn.conectar()
        query = f"select * from fnoperacionespuestos({opcion},{idpuesto},'{descripcion}',0,0);"
        resultado = conn.ejecutarquery(query)
        conn.cerrar()
        return jsonify(resultado), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@puestos.route('/baja', methods=['DELETE'])
def baja_puesto():
    try:
        data = request.json
        opcion = data.get('opcion')
        idpuesto = data.get('idpuesto')
        empleadobaja = data.get('empleadobaja')
        
        conn = conexion()
        conn.conectar()
        query = f"select * from fnoperacionespuestos({opcion},{idpuesto},'',0,{empleadobaja});"
        resultado = conn.ejecutarquery(query)
        conn.cerrar()
        return jsonify(resultado), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
