from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'productos.views.home', name='home'),
	url(r'^productos/', include('productos.urls', namespace='productos')),
)
