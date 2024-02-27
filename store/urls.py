from django.urls import path
from . import views

urlpatterns = [
    path("product/getall/", views.product_list),
    path("product/get/<int:id>", views.product_detail),
    path("product/add/", views.create_product),
    path("product/update/<int:id>", views.update_product),
    path("collection/", views.collection_list),
    path("collection/<int:id>", views.collection_detail)
]

