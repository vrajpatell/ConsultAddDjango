from django.contrib import admin
from django.urls import include, path
from firstapplication import views
from django.conf.urls.static import static


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='index')
                  # path('firstapplication/', include('firstapplication.urls')),
              ]