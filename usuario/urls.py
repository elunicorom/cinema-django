from django.conf.urls import include,url
from django.contrib import admin
from views import UsuarioCreate

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^crear_usuario/',UsuarioCreate.as_view(), name='crear'),
]
