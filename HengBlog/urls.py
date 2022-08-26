"""HengBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve

urlpatterns = [
    path('favicon.ico', serve, {'path': 'logo.png'}),

    path("i18n/", include("django.conf.urls.i18n")),
]

if settings.DEBUG is False:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )  # 加入这个才能显示media文件

# 这里放需要国际化的url
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("test_app/", include("test_app.urls")),
)
