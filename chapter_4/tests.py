from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="class PostTests(TestCase):")

    def test_model_content(self):
        self.assertEqual(self.post.text, "class PostTests(TestCase):")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/four/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self): 
        response = self.client.get(reverse("homex"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "chapter_4/home.html")
        #self.assertContains(  response, "This is a test!")