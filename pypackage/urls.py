from django.urls import path, re_path
from pypackage import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='pypackage-index'),
    path('simple/', views.PackageView.as_view(), name='pypackage-simple'),
    path('simple/<slug:slug>/', views.VersionView.as_view(), name='pypackage-simple-version'),
]

