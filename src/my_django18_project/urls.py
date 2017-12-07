"""my_django18_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from my_django18_project import postRecord

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'profiles.views.home', name='home'),
    url(r'^contact/$', 'profiles.views.contact', name='contact'),
    url(r'^about/$', 'profiles.views.about', name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^search/$', 'my_django18_project.views.twt_search', name='search'),
    url(r'^insertToDb/$', 'my_django18_project.views.twt_save'),
    url(r'^deleteFromDb/$', 'my_django18_project.views.twt_delete'),
    url(r'^getHist/$', 'my_django18_project.views.twt_hist'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
