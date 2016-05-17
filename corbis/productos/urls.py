from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^add_product/$', 'productos.views.add_product', name='add_product'),
	url(r'^update_product/$', 'productos.views.update_product', name="update_product"),
	url(r'^delete_product/$', 'productos.views.delete_product', name="remove_product"),
)