"""
URL configuration for django_intro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .view import views
from .view import line
from .view.branch import LineBranchAPI, BranchAPI
from .view.station import BranchStationAPI, StationAPI

app_name = 'mbta'
urlpatterns = [
    path('stations/', views.list_stations),
    path('lines/', line.list_lines),
    path('lines/<str:id>', line.get_line),
    path('lines/<str:line_id>/branches', LineBranchAPI.as_view()),
    path('branches/<str:id>', BranchAPI.as_view()),
    path('branches/<str:branch_id>/stations', BranchStationAPI.as_view()),
    path('stations/<str:id>', StationAPI.as_view()),

    path('test/', views.lines_view)
]
