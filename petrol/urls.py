from django.urls import path
from . import views

urlpatterns = [
    path("petrol/", views.index, name="petrol"),
    path("petrol/success/", views.confirm_registration , name='confirm-registration')
]
