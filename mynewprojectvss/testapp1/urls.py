
from django.urls import path
from .views import employee_data

urlpatterns = [
    path('', employee_data.as_view()),  # Handles POST at /testapp1/
    path('employee/', employee_data.as_view()),  # Handles POST at /testapp1/
    path('employee/<int:pk>/', employee_data.as_view())
    

]