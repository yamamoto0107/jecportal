from django.urls import path
from . import views

app_name = 'portal'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('portal/create/', views.AttendCreateView.as_view(), name='attend_create'),
    path('portal/create/complete/', views.AttendCreateCompleteView.as_view(), name='attend_create_complete'),

]