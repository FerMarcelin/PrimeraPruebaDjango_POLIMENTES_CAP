from django.test import TestCase
from MiPrimeraAppDjango.wsgi import *
from Users.models import User, Domicilio

# Create your tests here.

# u4 = User.objects.create_user(name='Clara', email='clara@correo.com', phone=168546556, password='rstuvw')
# print(u4)
"""data = {
    'calle': 'Triangulo',
    'edificio': 'A',
    'numero': 245,
    'colonia': 'Prado Churubusco',
    'delegacion': 'Coyoacan',
    'cp': 48976,
    'ciudad':'CDMX'
}"""
"""data3 = {
    'calle': 'Circulo',
    'edificio': 'B',
    'numero': 89,
    'colonia': 'bliblibli',
    'delegacion': 'Benito Juarez',
    'cp': 46598,
    'ciudad':'CDMX'
}"""
#dom1 = Domicilio.objects.create(**data)
#dom3 = Domicilio.objects.create(**data3)
#print(dom1.id)
#domi = Domicilio.objects.get(id=3)
#print(domi.id)
#u1 = User.objects.create_user(name='Alan', apellido='Ramirez', email='alan@correo.com', phone=156549687, domicilio=domi.id, password= '123456')
#u2 = User.objects.create_user(name='Marco', apellido='Lopez', email='marco@correo.com', phone=256854987, domicilio=domi.id, password='chilaquiles')
#u3 = User.objects.create_user(name='Alfredo', apellido='Morales', email='alf@correo.com', phone=419587627, domicilio=domi.id,password='pasta')
"""u7 = User.objects.create_user(name='Gabriel', email='gabriel@correo.com', phone=32168752, password='verduras')
u8 = User.objects.create_user(name='Axel', email='axel@correo.com', phone=95612487, password='frijoles')
u9 = User.objects.create_user(name='Cristina', email='cristina@correo.com', phone=413062598, password='enchiladas')
u10 = User.objects.create_user(name='Omar', email='omar@correo.com', phone=865213476, password='spaghetti')"""
#u11 = User.objects.create_user(name='Alfredo', apellido='Morales', email='alf@correo.com', phone=419587627, password='pasta')

"""EJERCICIO 2: 17ago2021
tabla = User.objects.all()
lista = []
for i in tabla:
    data= i.eje2()
    lista.append(data)
print(lista)"""

"""EJERCICIO 3: 17ago2021
tabla = User.objects.all()
lista = []
for i in tabla:
    data= i.eje3()
    lista.append(data)
print(lista)"""

"""tabla = User.objects.all().values('name', 'apellido', 'domicilio_id')
print(tabla)
for i in tabla:
    print (i)
    print(i.get('domicilio_id'))
    dom= Domicilio.objects.get(id=i.get('domicilio_id'))
    print(dom.calle)"""
# lista = []
# Para regresar diccionario con nombres correos y password de todos los usuarios
"""for i in tabla:
    data= i.regresa_dicc()
    lista.append(data)
print(lista)"""
# Para regresar lista con nombres de todos los usuarios
"""for i in tabla:
    nombre = i.regresa_nombre()
    lista.append(nombre)
print(lista)"""
# Para regresar lista con id de todos los usuarios
"""for i in tabla:
    ID = i.regresa_id()
    lista.append(ID)
print(lista)"""

# Para regresar diccionario con id, nombre y correo de todos los usuarios
"""for i in tabla:
    datos= i.regresa_dicc_conID()
    lista.append(datos)
print(lista)"""

# Para regresar nombre y apellido con formato
"""for i in tabla:
    nombre_completo= i.regresa_nombre_apellido()
    lista.append(nombre_completo)
print(lista)"""
# print(u11)"""
"""Para traer TODA la info del domicilio pero solo de aquellos registros que sus nombre inicia con la laetra A 
y haciendo uso del método get_data dado de alta en el modelo Domicilio, accediendo a la instancia de Domicilio 
a través de la llave foránea ‘domicilio_id’ contenida en el diccionario datos generado por el método regresa_dicc de la instancia User
nombre = 'A'
usuario = User.objects.filter(name__startswith=nombre)
print(usuario)
for i in usuario:
    datos = i.regresa_dicc()
    print (datos)
    #print(Domicilio.objects.get(id=datos.get('domicilio_id')).get_data())"""

"""Para traer TODA la info del domicilio pero solo de aquellos registros que sus nombre inicia con la laetra A 
y haciendo uso del método get_data dado de alta en el modelo Domicilioaccediendo a el desde el metodo regresa_dic()
cuando en su elemento domicilio instancio para poder asi acceder al get_data
nombre = 'A'
usuario = User.objects.filter(name__startswith=nombre)
print(usuario)
for i in usuario:
    datos = i.regresa_dicc()
    print (datos)
    #print(Domicilio.objects.get(id=datos.get('domicilio_id')).get_data())"""
