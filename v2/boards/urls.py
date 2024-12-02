from django.urls import path
from .views import *

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("fecha_actual/<str:name>", fecha_actual, name="fecha_actual"),
    path("menu/", menu_view, name="menu"),
    path("datosform/", datosform_view, name="datos_form"),
    path("datosform2/", datosform_view2, name="datos_form2"),
    path("widgetform/", widget_view, name="widgetform"),
    
    #CRUD URLS
    path('list/', BoardsListView.as_view(), name='boards_list'),        # Listar todos los boards
    path('create/', BoardCreateView.as_view(), name='boards_create'),  # Crear un nuevo board
    path('<int:pk>/', BoardDetailView.as_view(), name='board_detail'), # Ver detalle de un board
    path('<int:pk>/update/', BoardUpdateView.as_view(), name='boards_update'), # Actualizar un board
    path('<int:pk>/delete/', BoardDeleteView.as_view(), name='boards_delete'), # Eliminar un board
]