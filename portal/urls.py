from django.urls import path
from . import views

app_name = 'portal'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index/',views.index, name='index'),
    path('portal/create/', views.AttendCreateView.as_view(), name='attend_create'),
    path('portal/create/complete/', views.AttendCreateCompleteView.as_view(), name='attend_create_complete'),
    path('portal/list/', views.AttendListView.as_view(), name='attend_list'),
    path('portal/list/<uuid:pk>/', views.AttendDetailView.as_view(), name='attend_detail'),
]