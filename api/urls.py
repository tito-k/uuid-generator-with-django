from django.urls import path

from .views import add_and_show_uuid


urlpatterns = [
    path('', add_and_show_uuid),
]