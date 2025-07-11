from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns, set_language

urlpatterns = [
    path('i18n/set-lang/', set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

