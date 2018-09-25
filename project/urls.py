from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$", views.present, name='present'),
    url(r"^\d+$", views.index, name='index'),
]
