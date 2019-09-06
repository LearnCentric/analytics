from django.conf.urls import url
from django.contrib import admin

from charts import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]
