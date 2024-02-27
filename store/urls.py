from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.product_list),
    path("hello/<int:id>", views.product_detail),
]
