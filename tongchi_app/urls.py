from django.conf.urls import url
from . import views

app_name = 'tongchi_app'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
]