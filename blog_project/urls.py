# -*- coding: utf-8 -*-
"""blog_project URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from blog import views
from blog.upload import upload_image
from django.views.static import  serve#django自带的方法，处理一些静态文件
import blog_project

urlpatterns = [#图片上传的路由
    url(r"^uploads/(?P<path>.*)$", \
                serve, \
                {"document_root": blog_project.settings.MEDIA_ROOT,}),#图片服务器配置路由
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),#上传方法配置路由
    url(r'^admin/',admin.site.urls ),
    url(r'^', include("blog.urls")),
]
