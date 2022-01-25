from django.test import TestCase

from .models import *

from django.db.models import Max
# Create your tests here.

class ProbaStrzelniczaTestCase(TestCase):
    def setUp(self):
        a = Pocisk.objects.create(id="123", nazwa="9 mm")
        b = Pocisk.objects.create(id="321", nazwa="7,52 mm")

        ProbaStrzelnicza.objects.create(pocisk=a, id_pocisk="123")
        ProbaStrzelnicza.objects.create(pocisk=a, id_pocisk="123"
                                        )
        ProbaStrzelnicza.objects.create(pocisk=b, id_pocisk="321")

    def test_pocisk(self):
        a = Pocisk.objects.get(id="123")
        self.assertEqual(a.Pocisk.count(), 1)

    def test_valid_proba(self):
        a = Pocisk.objects.create(id="123")
        #b = Pocisk.objects.create(id="321")
        f = ProbaStrzelnicza.objects.get(pocisk=a, id_pocisk=9)
        self.assertTrue(f.is_valid_proba())

    def test_invalid_proba(self):
        a = Pocisk.objects.create(id="123")
        #b = Pocisk.objects.create(id="321")
        f = ProbaStrzelnicza.objects.get(pocisk=a, id_pocisk=-9)
        self.assertFalse(f.is_valid_proba())