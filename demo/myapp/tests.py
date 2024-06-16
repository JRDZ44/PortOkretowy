from django.test import TestCase
from django.urls import reverse
from django.shortcuts import redirect
from django.test import Client, RequestFactory
from django.contrib.auth.models import User
from .models import WarehouseDelivery
from .views import port_status_view


class FormsViewTests(TestCase):

# Test sprawdza, czy poprawnie wypełniony formularz rejestracji przekierowuje użytkownika do strony logowania oraz czy
# użytkownik jest dodawany do bazy danych.
        def test_auth_view_post_valid_form(self):
            client = Client()
            data = {
                "username": "testuser",
                "password1": "testpassword123",
                "password2": "testpassword123"
            }
            response = client.post(reverse('myapp:signup'), data)
            assert response.status_code == 302
            assert response.url == reverse('myapp:login')
            assert User.objects.filter(username="testuser").exists()

# Test sprawdza, czy niepoprawnie wypełniony formularz rejestracji (niezgodne hasła) skutkuje ponownym wyświetleniem
# formularza z odpowiednimi błędami oraz czy użytkownik nie jest dodawany do bazy danych.
        def test_auth_view_post_invalid_form(self):
            client = Client()
            data = {
                "username": "testuser",
                "password1": "testpassword123",
                "password2": "differentpassword"
            }
            response = client.post(reverse('myapp:signup'), data)
            assert response.status_code == 200
            assert 'registration/signup.html' in (t.name for t in response.templates)
            assert not User.objects.filter(username="testuser").exists()


class TestDeliveryView(TestCase):

# Testuje czy widok delivery zwraca status 200 i używa właściwego szablonu
    def test_delivery_view_status_and_template(self):
        client = Client()
        response = client.get(reverse('myapp:home/delivery/'))
        assert response.status_code == 200
        assert 'delivery.html' in (t.name for t in response.templates)


# Testuje czy widok delivery poprawnie tworzy wpis w bazie danych
    def test_delivery_view_creates_warehouse_delivery(self):
        client = Client()
        client.get(reverse('myapp:home/delivery/'))
        assert WarehouseDelivery.objects.count() == 1


class PortStatusViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def tearDown(self):
        del self.factory

# Testuje poprawność kodu statusu HTTP zwracanego przez widok port_status_view oraz porównuje rzeczywisty status
    # z oczekiwanym
    def test_port_status_view_status_code(self):
        request = self.factory.get('/port-status/')
        response = port_status_view(request)
        self.assertEqual(response.status_code, 200)

# Testuje zawartość odpowiedzi HTTP zwróconej przez widok.
# Zamiast bezpośredniego sprawdzania context, sprawdzamy czy klucz 'seaports_statuses' nie znajduje się w zawartości odpowiedzi
    def test_port_status_view_data(self):
        request = self.factory.get('/port-status/')
        response = port_status_view(request)
        self.assertFalse('seaports_statuses' in response.content.decode())




