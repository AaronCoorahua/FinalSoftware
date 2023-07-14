from flask import Flask, request
import datetime

app = Flask(__name__)

class Operacion:
    def __init__(self, numero_destino, valor):
        self.numero_destino = numero_destino
        self.fecha = datetime.datetime.now()
        self.valor = valor

class Cuenta:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos
        self.operaciones = []

    def historial(self):
        historial = f"Saldo de {self.nombre}: {self.saldo}\nOperaciones de {self.nombre}\n"
        for operacion in self.operaciones:
            tipo = "Pago realizado" if operacion.valor < 0 else "Pago recibido"
            fecha = operacion.fecha.strftime("%d/%m/%Y")
            historial += f"{tipo} de {abs(operacion.valor)} de {operacion.numero_destino}\n"
        historial += f"{len(self.operaciones)} de {len(self.operaciones) + 1}"
        return historial

    def pagar(self, destino, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.operaciones.append(Operacion(destino, -valor))
            return f"Realizado en {datetime.datetime.now().strftime('%d/%m/%Y')}."
        else:
            return "Saldo insuficiente para realizar la transferencia."

# Inicialización de cuentas y contactos
cuentas = [
    Cuenta("21345", "Arnaldo", 200, {"123": "Luisa", "456": "Andrea"}),
    Cuenta("123", "Luisa", 400, {"456": "Andrea"}),
    Cuenta("456", "Andrea", 300, {"21345": "Arnaldo"})
]

@app.route('/billetera/contactos', methods=['GET'])
def obtener_contactos():
    minumero = request.args.get('minumero')
    cuenta = buscar_cuenta(minumero)
    if cuenta:
        return "\n".join([f"{numero}: {nombre}" for numero, nombre in cuenta.contactos.items()])
    else:
        return "La cuenta no existe."

@app.route('/billetera/pagar', methods=['GET'])
def realizar_pago():
    minumero = request.args.get('minumero')
    numerodestino = request.args.get('numerodestino')
    valor = int(request.args.get('valor'))
    cuenta = buscar_cuenta(minumero)
    if cuenta:
        resultado = cuenta.pagar(numerodestino, valor)
        return resultado
    else:
        return "La cuenta no existe."

@app.route('/billetera/historial', methods=['GET'])
def obtener_historial():
    minumero = request.args.get('minumero')
    cuenta = buscar_cuenta(minumero)
    if cuenta:
        historial = cuenta.historial()
        return historial
    else:
        return "La cuenta no existe."

# Búsqueda de cuenta por número
def buscar_cuenta(numero):
    for cuenta in cuentas:
        if cuenta.numero == numero:
            return cuenta
    return None

if __name__ == '__main__':
    app.run()
