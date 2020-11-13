"""
Django settings for bookmanage project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# __file__表示文件的名字
# abspath是绝对路径

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'stncjjg^j1ewdk+9o_&xh4n!^gv5o*-3ik6v7d%%ri_y36($b$'

# SECURITY WARNING: don't run with debug turned on in production!
# 开发者进行调试使用

DEBUG = True

# 上线时候调成False
# DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book.apps.BookConfig',
    'login.apps.LoginConfig',
    'pay.apps.PayConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookmanage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # dirs设置模板路径
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmanage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# sqlsite 主要是嵌入式关系型数据库
# 主要是在移动端使用
# sqlite属于小型数据库
# 中型数据库：mysql sqlserver
# 大型数据库:oracle,DB2
DATABASES = {
    'default': {
        # engine引擎
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'127.0.0.1', #ip地址
        'PORT':'3306', # 端口号
        'USER':'root',# 用户名
        'PASSWORD':'zhaoyuwei66',# 密码
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),# 指定数据库
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# django如何区分静态资源与动态资源呢？
# 就是通过STATIC_URL
# 我们在访问静态资源http://ip:port + STATIC_URL + 文件名
# django就会认为我们在访问静态资源，这个时候就会在静态资源文件夹里面进行匹配
STATIC_URL = '/static/'

# 告知系统静态文件在哪里
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
