import unittest
from app import app, buscar_cuenta

class BilleteraTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    #Este test lo que hace es realizar el pago al destino 123 un valor de 100 soles
    def test_realizar_pago_exitoso(self):
        response = self.app.get('/billetera/pagar?minumero=21345&numerodestino=123&valor=100')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Realizado', response.data.decode('utf-8'))

    #Este test lo que hace es obtener los contactos del numero 999 que no existe en la base de datos
    def test_obtener_contactos_error(self):
        response = self.app.get('/billetera/contactos?minumero=999')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'La cuenta no existe.')

    #Este test lo que hace es enviar un pago por un valor de 1000 que es un saldo insuficiente según nuestros datos.
    def test_realizar_pago_error(self):
        response = self.app.get('/billetera/pagar?minumero=123&numerodestino=999&valor=1000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Saldo insuficiente para realizar la transferencia.')

    #Este test lo que hace es obtener el historial del numero 999 que no existe en la base de datos
    def test_obtener_historial_error(self):
        response = self.app.get('/billetera/historial?minumero=999')
        self.assertEqual(response.data.decode('utf-8'), 'La cuenta no existe.')

if __name__ == '__main__':
    unittest.main()
