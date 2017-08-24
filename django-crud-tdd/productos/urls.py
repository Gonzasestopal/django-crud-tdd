from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^add/$', 'productos.views.add_product', name='add'),
	url(r'^update/$', 'productos.views.update_product', name="update"),
	url(r'^delete/$', 'productos.views.delete_product', name="remove"),
)
