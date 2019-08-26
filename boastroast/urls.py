"""boastroast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from .views import homepage, post, upvote, downvote, boasts, roasts, highestvoted

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name="homepage"),
    path('postsubmit/', post, name="post"),
    path('upvote/<int:element_id>', upvote, name="upvote"),
    path('downvote/<int:element_id>', downvote, name="downvote"),
    path('boasts/', boasts, name='boasts'),
    path('roasts/', roasts, name='roasts'),
    path('mostvotes/', highestvoted, name='highestvoted')

]
