from django.test import TestCase
from .models import Provider, Course


class CodetaskTestCase(TestCase):
    def setUp(self):
        self.provider, _ = Provider.objects.get_or_create(name="Test Provider", description="Test Description")
        self.course, _ = Course.objects.get_or_create(title="Test Course", description="Test Description", provider=self.provider)

    def test_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_provider_detail_page(self):
        response = self.client.get(f'/provider/{self.provider.id}/')
        self.assertEqual(response.status_code, 200)

    def test_course_list_page(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)

    def test_course_detail_page(self):
        response = self.client.get(f'/course/{self.course.id}/')
        self.assertEqual(response.status_code, 200)
