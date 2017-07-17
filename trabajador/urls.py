from django.conf.urls import include,url
from django.contrib import admin
from views import TrabajadorList,TrabajadorCreate,index,TrabajadorUpdate,TrabajadorDelete


urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^crear_trabajador/',TrabajadorCreate.as_view(), name='crear'),
    url(r'^listar_trabajador/',TrabajadorList.as_view(), name='listar'),
    url(r'^editar/(?P<pk>\d+)/$',TrabajadorUpdate.as_view(),name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',TrabajadorDelete.as_view(),name='eliminar'),
]
