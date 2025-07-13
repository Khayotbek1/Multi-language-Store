from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns, set_language

from main.views import *

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('i18n/set-lang/', set_language, name='set_language'),
    path('categories/', CategoryListCreateAPIView.as_view()),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

