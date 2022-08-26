from django.urls import path

from . import views

app_name = 'circlelist'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('download/', views.downloadCircle, name='download'),
    path('showcirclelist', views.showCirclelist, name='showCirclelist'),
    path('showcirclelist/<int:circle_id>/', views.detail, name='detail'),
    path('search/', views.circle_search, name='search'),
    ]