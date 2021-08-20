"""
SERIALIZADORES
Aqui solo se hace la lógica de programación tal cual
"""
from rest_framework.serializers import *
from Users.models import User, Domicilio


class DomicilioSerializer(Serializer):
    calle = CharField()
    edificio = CharField()
    numero = IntegerField()
    colonia = CharField()
    delegacion = CharField()
    cp = IntegerField()
    ciudad = CharField()

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return Domicilio.objects.create(**validated_data)


class UserSerializer(Serializer):
    name = CharField(allow_null=False)
    apellido = CharField(allow_null=True)
    email = EmailField(allow_null=False)
    phone = IntegerField(max_value=9999999999, allow_null=False)
    domicilio_id = IntegerField(read_only=True)
    password = CharField()

    """
    def validate_email(self, value):
        # Metodo exists del ORM que me regresa T o F dependiendo si el valor especificado en el filter existe 
        
        if User.objects.filter(email=value).exists() :
            raise ValidationError({'status': "Credenciales invalidas"})
            
        return value
    """

    """
    def validate_phone(self, value):
        if User.objects.filter(phone=value).exists():
            raise ValidationError({'status': "Datos invalidos"})
        return value
    """

    def validate(self, attrs):
        """
        ESTO ES PARA CUANDO USAMOS EL CONTEXT, QUE AL FINAL NO FUNCIONÓ PORQUE NO NOS PERMITÍA
        VALIDAR AL MISMO TIEMPO Y SE PODÍA CREAR EL DOMICILIO AÚN CUANDO EL USUARIO ESTABA MAL

        attrs['domicilio_id'] = self.context['domicilio_id']
        """

        if User.objects.filter(email=attrs['email']).exists():
            raise ValidationError({'status': "Correo invalido"})

        if User.objects.filter(phone=attrs['phone']).exists():
            raise ValidationError({'status': "Telefono invalido"})

        return attrs

    def create(self, domicilio_id: int):
            self.validated_data['domicilio_id'] = domicilio_id
            return User.objects.create_user(**self.validated_data)



    """
    def to_representation(self, instance):
        Ayuda a generar un listado personalizado y recibe la instancia que por
        defecto es la instancia del serializador donde se encuentra definido
        
        return {
            'user': instance.regresa_dicc()
        }
    """


