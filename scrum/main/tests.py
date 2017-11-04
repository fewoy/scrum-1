from django.test import TestCase
from django.urls import resolve
from main.views import index

class IndexTest(TestCase):

    def test_root_resolves_to_index(self):
        page = resolve('/')
        self.assertEqual(page.func, index)