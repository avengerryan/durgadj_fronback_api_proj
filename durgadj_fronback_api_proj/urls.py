"""durgadj_fronback_api_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url, include
# from durgadj_fronback_api_proj.durgadj_fronback_api_app import views
from durgadj_fronback_api_app import views


# pip install django rest swagger

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Swagger API for Employee')





urlpatterns = [
    url(r'^swaggerdoc/$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^hydjobs/', views.hydjobs1),
    url(r'^blorejobs/', views.blorejobs),
    url(r'^punejobs/', views.punejobs),
    url(r'^chennaijobs/', views.chennaijobs),
    # url(r'^api/', include('durgadj_fronback_api_proj.durgadj_fronback_api_app.api.urls'))
    url(r'^api/', include('durgadj_fronback_api_app.api.urls')),

]

#
# urlpatterns += [
#     url(r'^swaggerdoc/$', schema_view)
# ]

















