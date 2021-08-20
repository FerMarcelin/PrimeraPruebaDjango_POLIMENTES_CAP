from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


# Create your models here.
class Domicilio(models.Model):  # models.Model es para cuando NO voy a crear un manager de la clase (tabla)
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=80, null=False, blank=False)
    edificio = models.CharField(max_length=20, null=True, blank=True)
    numero = models.IntegerField(null=False, blank=False)
    colonia = models.CharField(max_length=80, null=False, blank=False)
    delegacion = models.CharField(max_length=80, null=False, blank=False)
    cp = models.IntegerField(null=False, blank=False)
    ciudad = models.CharField(max_length=80, null=False, blank=False)

    class Meta:
        db_table = "Domicilios"
        ordering = ['id']
        verbose_name = "domicilio"

    def get_data(self):
        return {
            'calle': self.calle,
            'edificio': self.edificio,
            'numero': self.numero,
            'colonia': self.colonia,
            'delegacion': self.delegacion,
            'cp': self.cp,
            'ciudad': self.ciudad
        }

    def col_cp(self):
        return {
            'colonia': self.colonia,
            'cp': self.cp,
        }

    def get_id(self):
        return self.id


class ManagerUser(BaseUserManager):  # PREGUNTA!! ¿para qué funciona exqactamente esta clase?
    def create_user(self, name, apellido, email, phone, domicilio_id, password=None):
        if name is None:
            raise TypeError("No hay nombre")
        if email is None:
            raise TypeError("No hay email")

        print(password)

        user = self.model(name=name, apellido=apellido, email=email, domicilio_id=domicilio_id, phone=phone)

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    apellido = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    phone = models.IntegerField(null=False, blank=False, unique=True)
    password = models.TextField(max_length=64, blank=True)
    username = models.CharField(max_length=255, null=False, blank=False)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.DO_NOTHING, null=False, blank=False)

    objects = ManagerUser()
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = "Usuarios"
        ordering = ['phone']
        verbose_name = "usuario"

    def __str__(self):
        return self.name

    def regresa_con_formato(self):
        return f"{self.name},{self.email},{self.password}"

    def regresa_dicc(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'domicilio': self.domicilio.get_data(),
                'password': self.password}

    def regresa_nombre(self):
        return f"{self.name}"

    def regresa_id(self):
        return self.id

    def regresa_dicc_conID(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}

    def regresa_nombre_apellido(self):
        return f"{self.name},{self.apellido}"

    def eje2(self):
        return {'name': self.name, 'apellido': self.apellido, 'domicilio': self.domicilio.col_cp()}

    def eje3(self):
        return {
            'last_login': self.last_login,
            'id': self.id,
            'name': self.name,
            'apellido': self.apellido,
            'email': self.email,
            'username': self.username,
            'phone': self.phone,
            'domicilio': self.domicilio.get_data(),
            'password': self.password
        }
