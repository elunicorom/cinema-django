from django.conf.urls import include,url
from django.contrib import admin
from views import UsuarioList,UsuarioCreate,index


urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^crear_usuarios/',UsuarioCreate.as_view(), name='crear'),
    url(r'^listar_usuarios/',UsuarioList.as_view(), name='listar'),
]
