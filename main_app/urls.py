from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('plants/', views.plant_index, name='plant-index'),
  path('plants/<int:plant_id>/', views.plant_detail, name='plant-detail'),
  path('plants/<int:plant_id>/add-watering/', views.add_watering, name='add-watering'),
  path('plants/create/', views.PlantCreate.as_view(), name='plant-create'),
  path('plants/<int:pk>/update', views.PlantUpdate.as_view(), name='plant-update'),
  path('plants/<int:pk>/delete', views.PlantDelete.as_view(), name='plant-delete'),
  path('pots/create/', views.PotCreate.as_view(), name='pot-create'),
]
