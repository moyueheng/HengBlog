"""
Django settings for HengBlog project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import sys, os
from os.path import join as pjoin

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


sys.path.insert(0, pjoin(BASE_DIR, "apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "HENG_SECRET_KEY",
    "django-insecure-+nc7^+mpze8&311m=647h0hg10e0%@5^kc0iobh9z=sry+%s^o",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("HENG_DEBUG", "True").upper() == "TRUE"

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

if DEBUG is True:
    INSTALLED_APPS.append('test_app')

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # 新增多语支持
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "HengBlog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [pjoin(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "HengBlog.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 关闭国际时间，不然数据库报错

# 设置I18n和L10N为True
USE_I18N = True
USE_L10N = True


# 用于存放django.po和django.mo编译过的翻译文件
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# 静态文件收集
STATIC_URL = "/static/"

# debug状态的时候其实是在这里面的目录下面找
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# 最后会收集到下面这个目录
STATIC_ROOT = pjoin("/var/www/HengBlog/", "static")

# 媒体文件收集
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# 网站默认设置和上下文信息
SITE_LOGO_NAME = os.getenv("HENG_LOGO_NAME", "logo.png")
SITE_END_TITLE = os.getenv("HENG_SITE_END_TITLE", "HengBlog")
SITE_DESCRIPTION = os.getenv(
    "HENG_SITE_DESCRIPTION", "网站描述 给予django3.2和bootstrap5的django博客"
)
SITE_KEYWORDS = os.getenv("HENG_SITE_KEYWORDS", "HENG,Django博客,个人博客")

# 个性化设置，非必要信息
# 个人 Github 地址
MY_GITHUB = os.getenv("HENG_GITHUB", "https://github.com/moyueheng")


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": SITE_END_TITLE,
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": SITE_END_TITLE,
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": f"{SITE_END_TITLE} Admin",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": SITE_LOGO_NAME,
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Welcome text on the login screen
    "welcome_sign": f"Welcome to the {SITE_END_TITLE}",
    # Copyright on the footer
    "copyright": "moyueheng@126.com",
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # external url that opens in a new window (Permissions can be added)
        {
            "name": "提问",
            "url": f"{MY_GITHUB}/issues",
            "new_window": True,
        },
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
    ],
}
