"""
VISTAS
Aquí va tal cual la ejecución de la lógica de programacion creada en los serializadores
"""
from rest_framework.views import APIView  # clase general que me permite acer GET PUT y DELETE en una sola vista
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import \
    RetrieveAPIView, \
    ListAPIView, \
    CreateAPIView  # clase que se encanrga SOLO DE OBTENER adatos, por ejemplo la LISTAPIVIEW es solo de listas y así
from Users.models import User, Domicilio
from Users.api.serializers.user_serializers import *


class ObtenerUsuario(APIView):
    def get(self, request):
        usuario = User.objects.all().values('last_login', 'name', 'apellido', 'email')
        return Response(usuario, status=status.HTTP_200_OK)


class ListaCompleta(APIView):
    def get(self, request):
        tabla = User.objects.all()
        lista = [i.eje3() for i in tabla]  # El for pero en lista de comprensión son mucho más rápidas
        """for i in tabla:
            data = i.eje3()
            lista.append(data)
        print(lista)"""
        # domi = Domicilio.get_data()
        # usuario = User.objects.all().values('name', 'apellido', 'domicilio' )
        return Response(lista, status=status.HTTP_200_OK)


class ListaParcial(APIView):
    def get(self, request):
        tabla = User.objects.all()
        lista = []
        for i in tabla:
            data = i.eje2()
            lista.append(data)
        print(lista)
        # domi = Domicilio.get_data()
        # usuario = User.objects.all().values('name', 'apellido', 'domicilio' )
        return Response(lista, status=status.HTTP_200_OK)


# Vistas genericas me permiten hacer lo mismo de peticiones pero sin usar tanto recurso
class RetrieveUser(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_queryset(self, **kwargs):
        return User.objects.get(**kwargs)

    def retrieve(self, request, *args, **kwargs):
        id = request.query_params['id']
        user = self.get_queryset(id=id)
        serializers = self.serializer_class(instance=user)
        print(serializers.data)
        return Response(serializers.data, status=status.HTTP_200_OK)


"""Esta clase generica sirve para listar """


class ListUser(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def list(self, request, *args, **kwargs):
        user = self.get_queryset()
        lista = []
        for i in user:
            serializer = self.serializer_class()
            data_user = serializer.to_representation(instance=i)
            lista.append(data_user)

        return Response(lista, status=status.HTTP_200_OK)


"""Esta clase (Create) sirve exclusivamente para hacer post"""


class CreateUser(CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateDom(CreateAPIView):
    serializer_class_domicilio = DomicilioSerializer

    def create(self, request, *args, **kwargs):
        serializer2 = self.serializer_class_domicilio(data=request.data)
        if serializer2.is_valid():
            serializer2.create(serializer2.data)
            return Response(serializer2.data, status=status.HTTP_201_CREATED)

        return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)


class Completo(CreateAPIView):
    serializer_class_user = UserSerializer
    serializer_class_domicilio = DomicilioSerializer

    def create(self, request, *args, **kwargs):

        serializer_domicilio = self.serializer_class_domicilio(data=request.data['domicilio'])
        if not serializer_domicilio.is_valid():
            return Response(serializer_domicilio.errors, status=status.HTTP_400_BAD_REQUEST)

        # context = {'domicilio_id': dom.get_id()}
        serializer_user = self.serializer_class_user(data=request.data['usuario'])  # context=context)
        if not serializer_user.is_valid():
            return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)

        dom = serializer_domicilio.create(serializer_domicilio.data)
        serializer_user.create(dom.get_id())

        return Response({'status': "Operación satisfactoria"}, status=status.HTTP_201_CREATED)
