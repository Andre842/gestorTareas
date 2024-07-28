from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarea, name='listar_tarea'),
    path('editar_tarea/<str:pk>', views.editar_tarea, name="editar_tarea"),
    path('eliminar_tarea/<str:pk>', views.eliminar_tarea, name="eliminar_tarea")
    # path('editar_tarea/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),
    # path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
]