"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from .models import Producto
from django.test import Client, TestCase
import json as json

class TestIndex(TestCase):
    def setUp(self):
        self.product = Producto.objects.create(cantidad=1, nombre="test product", codigo="123")

    def test_index_contains_products(self):
        """
        Tests that index path is showing product data.
        """
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'test product')


class TestProductAddition(TestCase):
    def test_product_add(self):
        """
        Tests that the product added has been created.
        """
        c = Client()
        data = {'cantidad': 1, 'nombre': "test", "codigo": "123"}
        response = c.post('/productos/add/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['id'], 1)


class TestProductEdition(TestCase):
    def setUp(self):
        self.product = Producto.objects.create(cantidad=1, nombre="test", codigo="123")

    def test_product_edit(self):
        """
        Tests that the product edited has been modified.
        """
        c = Client()
        data = {'pk': self.product.pk, 'cantidad': 2, 'nombre': 'new_test', 'codigo': '456'}
        response = c.post('/productos/update/', data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Producto.objects.filter(nombre='new_test').exists())

class TestProductDeletion(TestCase):
    def setUp(self):
        self.product = Producto.objects.create(cantidad=1, nombre="test", codigo="123")

    def test_product_delete(self):
        """
        Tests that the product deleted no longer exists.
        """
        c = Client()
        data = {'pk': self.product.pk}
        response = c.post('/productos/delete/', data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Producto.objects.filter(pk=1).exists())
