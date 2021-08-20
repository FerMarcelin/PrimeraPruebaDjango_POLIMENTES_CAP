from django.urls import path
from Users.api.views.user_views import *

urlpatterns = [
    path("obtener-usuario/", ObtenerUsuario.as_view(), name='obtener-usuario'),
    path("lista-parcial/", ListaParcial.as_view(), name='lista-parcial'),
    path("retrieve-user/", RetrieveUser.as_view(), name='retrieve-user'),
    path("list-user/", ListUser.as_view(), name='list-user'),
    path("create-user/", CreateUser.as_view(), name='create-user'),
    path("create-dom/", CreateDom.as_view(), name='create-dom'),
    path("completo/", Completo.as_view(), name='completo'),


]
