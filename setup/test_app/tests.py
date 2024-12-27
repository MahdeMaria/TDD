from unittest import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from test_app.models import Post
from django.core.exceptions import ValidationError
from django.test import TestCase
from .serializers import PostSerializer
from .models import Post

class PostModelTest(TestCase):
    def test_create_post_with_valid_data(self):
        post = Post.objects.create(title='Teste Post', content='teste')
        self.assertEqual(post.title, 'Teste Post')
        self.assertEqual(post.content, 'teste')

    def test_create_post_without_title(self):
        post = Post(content='Post sem título')
        with self.assertRaises(ValidationError):
            post.full_clean()

    def test_create_post_without_content(self):
        post = Post(title='Post sem conteúdo')
        with self.assertRaises(ValidationError):
            post.full_clean()

class PostViewTest(APITestCase):
    def test_get_posts(self):
        Post.objects.create(title='primeiro Post', content='Content')
        response = self.client.get(reverse('post-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_post_with_valid_data(self):
        data = {'title': 'Novo Post', 'content': 'novo content'}
        response = self.client.post(reverse('post-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_post_without_title(self):
        data = {'content': 'Faltando title'}
        response = self.client.post(reverse('post-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_post_without_content(self):
        data = {'title': 'Faltando content'}
        response = self.client.post(reverse('post-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_post_invalid_data(self):
        response = self.client.post(reverse('post-list-create'), {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class PostSerializerTest(TestCase):
    def test_serializer_with_valid_data(self):
        post = Post.objects.create(title="Post Valido", content="valido")
        serializer = PostSerializer(post)
        self.assertEqual(serializer.data['title'], "Post Valido")

    def test_serializer_with_invalid_data(self):
        serializer = PostSerializer(data={'title': '', 'content': ''})
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)
        self.assertIn('content', serializer.errors)

    def test_serializer_missing_content(self):
        serializer = PostSerializer(data={'title': 'Faltando content'})
        self.assertFalse(serializer.is_valid())
        self.assertIn('content', serializer.errors)