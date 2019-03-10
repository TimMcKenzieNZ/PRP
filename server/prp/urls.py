"""prp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.http import HttpResponse
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('api/', include('programmes.urls')),
    path('admin/', admin.site.urls),
    # This is for checking if the server is alive/dead so the loadmanager can runn a new docker img if necessasry
    url(r'^status/ping', lambda request: HttpResponse("PONG")),

]

if settings.DEBUG: # If we are in development mode
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # for uplosding during dev
