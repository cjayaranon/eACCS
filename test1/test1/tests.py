from django.urls import reverse
from django.test import TestCase

class HomeTests(TestCase):
    def test_login_view_status_code(self):
        url = reverse('login')
        responce = self.client.get(url)
        self.assertEquals(responce.status_code, 200)
        
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def test_front_office_view_status_code(self):
        url = reverse('front-office')
        responce = self.client.get(url)
        self.assertEquals(responce.status_code, 200)
        
    def test_new_client_view_status_code(self):
        url = reverse('new-client')
        responce = self.client.get(url)
        self.assertEquals(responce.status_code, 200)
        
    def test_error_view_status_code(self):
        url = reverse('error')
        responce = self.client.get(url)
        self.assertEquals(responce.status_code, 200)