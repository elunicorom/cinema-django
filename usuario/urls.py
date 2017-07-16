from django.conf.urls import include,url
from django.contrib import admin
from views import UsuarioList,UsuarioCreate,index,UsuarioUpdate,UsuarioDelete


urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^crear_usuarios/',UsuarioCreate.as_view(), name='crear'),
    url(r'^listar_usuarios/',UsuarioList.as_view(), name='listar'),
    url(r'^editar/(?P<pk>\d+)/$',UsuarioUpdate.as_view(),name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',UsuarioDelete.as_view(),name='eliminar'),
]
