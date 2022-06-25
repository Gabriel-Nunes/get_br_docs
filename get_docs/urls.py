from django.urls import path
from get_docs import views

urlpatterns = [
    path('get_docs/', views.TextList.as_view()),
]
