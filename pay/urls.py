from django.conf.urls import url
from pay.views import index

urlpatterns = [
    url(r'^order', index)
]
