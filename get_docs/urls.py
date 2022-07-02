from django.urls import path
from get_docs import views

urlpatterns = [
    path('get_data/', views.GetData.as_view()),
]
