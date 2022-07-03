from django.urls import path
from home import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('export_excel/', views.ExportExcel.as_view(), name='export_excel'),
]
