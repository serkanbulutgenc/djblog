# Create your tests here.
from django.test import TestCase
from django.urls import reverse


class HomeAppTest(TestCase):
    def setUp(self):
        self.test_var = 'John'

    def test_homeview_response(self):
        res = self.client.get(reverse('core:home:index'))

        self.assertEqual(res.status_code, 200)

        self.assertContains(res, 'hero')

        self.assertTemplateUsed(res, 'home/index.html')
