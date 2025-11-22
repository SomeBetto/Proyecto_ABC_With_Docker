import unittest
import requests
import json
import time
import os

class TestAPI(unittest.TestCase):
    BASE_URL = os.getenv("API_URL", "http://localhost:3000")
    
    # Datos de prueba para Empleado
    empleado_data = {
        "opcion": 1, # Asumiendo que 1 es para agregar
        "numeroempleado": 9999,
        "nombre": "Test",
        "appaterno": "User",
        "appmaterno": "Integration",
        "direccion": "Calle Falsa 123",
        "codigopostal": "12345",
        "telefono": "5551234567",
        "curp": "TEST990101HDFXXX00",
        "nss": "12345678901",
        "puesto": 1 # Asumiendo que existe el puesto 1
    }

    # Datos de prueba para Puesto
    puesto_data = {
        "opcion": 1, # Asumiendo que 1 es para agregar
        "idpuesto": 99,
        "descripcion": "Puesto de Prueba",
        "empleadoalta": 1
    }

    def test_1_agregar_empleado(self):
        print("\nTesting Agregar Empleado...")
        url = f"{self.BASE_URL}/empleados/agregar"
        response = requests.post(url, json=self.empleado_data)
        self.assertEqual(response.status_code, 200)
        print(f"Response: {response.json()}")

    def test_2_consulta_empleado(self):
        print("\nTesting Consulta Empleado...")
        url = f"{self.BASE_URL}/empleados/consulta"
        params = {
            "opcion": 4, # Asumiendo que 4 es consulta
            "numeroempleado": self.empleado_data["numeroempleado"]
        }
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 200)
        print(f"Response: {response.json()}")

    def test_3_modificar_empleado(self):
        print("\nTesting Modificar Empleado...")
        url = f"{self.BASE_URL}/empleados/modificar"
        mod_data = self.empleado_data.copy()
        mod_data["direccion"] = "Nueva Direccion 456"
        mod_data["opcion"] = 2 # Asumiendo que 2 es modificar
        response = requests.put(url, json=mod_data)
        self.assertEqual(response.status_code, 200)
        print(f"Response: {response.json()}")

    def test_4_baja_empleado(self):
        print("\nTesting Baja Empleado...")
        url = f"{self.BASE_URL}/empleados/baja"
        baja_data = {
            "opcion": 3, # Asumiendo que 3 es baja
            "numeroempleado": self.empleado_data["numeroempleado"],
            "causabaja": "Fin de pruebas"
        }
        response = requests.delete(url, json=baja_data)
        self.assertEqual(response.status_code, 200)
        print(f"Response: {response.json()}")

    def test_5_agregar_puesto(self):
        print("\nTesting Agregar Puesto...")
        url = f"{self.BASE_URL}/puestos/agregar"
        response = requests.post(url, json=self.puesto_data)
        self.assertEqual(response.status_code, 200)
        print(f"Response: {response.json()}")

    def test_6_consulta_puesto(self):
        print("\nTesting Consulta Puesto...")
        url = f"{self.BASE_URL}/puestos/consulta"
        params = {
            "opcion": 4, # Asumiendo que 4 es consulta
            "idpuesto": self.puesto_data["idpuesto"]
        }
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 200)
        print(f"Response: {response.json()}")

    def test_7_modificar_puesto(self):
        print("\nTesting Modificar Puesto...")
        url = f"{self.BASE_URL}/puestos/modificar"
        mod_data = self.puesto_data.copy()
        mod_data["descripcion"] = "Puesto Modificado"
        mod_data["opcion"] = 2 # Asumiendo que 2 es modificar
        response = requests.put(url, json=mod_data)
        self.assertEqual(response.status_code, 200)
        print(f"Response: {response.json()}")

    def test_8_baja_puesto(self):
        print("\nTesting Baja Puesto...")
        url = f"{self.BASE_URL}/puestos/baja"
        baja_data = {
            "opcion": 3, # Asumiendo que 3 es baja
            "idpuesto": self.puesto_data["idpuesto"],
            "empleadobaja": 1
        }
        response = requests.delete(url, json=baja_data)
        self.assertEqual(response.status_code, 200)
        print(f"Response: {response.json()}")

if __name__ == '__main__':
    unittest.main()
