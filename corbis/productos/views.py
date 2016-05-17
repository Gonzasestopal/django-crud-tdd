# Create your views here.d
import json
import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from productos.forms import ProductoForm
from productos.models import Producto

from django.views.decorators.csrf import ensure_csrf_cookie

def home(request):

	productos = Producto.objects.all()

	return render(request, 'index.html', {'productos': productos})

@ensure_csrf_cookie
def add_product(request):

	if request.method == 'POST':

		form = ProductoForm(request.POST)

		if form.is_valid():

			producto = Producto.objects.create(
				codigo=request.POST.get('codigo'),
				nombre=request.POST.get('nombre'),
				cantidad=request.POST.get('cantidad'),
			)

			data = {key: request.POST[key] for key in request.POST}
			data['id'] = producto.pk
			data = json.dumps(data)
			return HttpResponse(data, content_type='application/json')

	else:
		return HttpResponse(status=500)

def update_product(request):
	instance = Producto.objects.get(pk=request.POST.get('pk'))

	if request.method == 'POST':

			instance.codigo = request.POST.get('codigo')
			instance.nombre = request.POST.get('nombre')
			instance.cantidad = int(request.POST.get('cantidad'))
			instance.save()

			return HttpResponse(status=200)

	else:
		return HttpResponse(status=500)

def delete_product(request):
	instance = Producto.objects.get(id=request.POST.get('pk'))

	if request.method == 'POST':

			instance.delete()

			return HttpResponse(status=200)

	else:
		return HttpResponse(status=500)