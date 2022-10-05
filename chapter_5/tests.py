from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Blog


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@test.com", password="secret"
        )
        cls.post = Blog.objects.create(
            title="A GOOD TITLE",
            body="NICE BODY CONTENT",
            author=cls.user,
        )

    def test_blog_model(self):
        self.assertEqual(self.post.title, "A GOOD TITLE")
        self.assertEqual(self.post.body, "NICE BODY CONTENT")
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(str(self.post), "A GOOD TITLE")
        self.assertEqual(self.post.get_absolute_url(), "/five/blog/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/five/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/five/blog/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("chapter_5:home5"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "NICE BODY CONTENT")
        self.assertTemplateUsed(response, "chapter_5/home.html")

    def test_post_detailview(self): 
        response = self.client.get(reverse("chapter_5:about5",
        kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A GOOD TITLE")
        self.assertTemplateUsed(response, "chapter_5/about.html")
