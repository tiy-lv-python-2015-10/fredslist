from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from api.views import ListCreatePost
from posting.models import Post, Favorite


class PostTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='bob', email='bob@bob.com', password='password1')

    def test_post_list(self):
        post = Post.objects.create(title='Title', description='Description', user=self.user)
        url = reverse('api_post_list_create')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_post = response.data['results'][0]
        self.assertEqual(response_post['title'], post.title)

    def test_post_list_request(self):
        post = Post.objects.create(title='Title', description='Description', user=self.user)
        factory = APIRequestFactory()
        view = ListCreatePost.as_view()
        url = reverse('api_post_list_create')
        request = factory.get(url, {}, format='json')
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_post = response.data['results'][0]
        self.assertEqual(response_post['title'], post.title)

    def test_create_chirp(self):
        url = reverse('api_post_list_create')
        data = {'title': 'Test1', 'description': 'Test description'}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.all().count(), 1)
        self.assertEqual(self.user.id, response.data['user'])

    def test_list_post_username_filter(self):
        post = Post.objects.create(title='Title', description='Description', user=self.user)
        user2 = User.objects.create_user(username='billy', email="billy@billy.com", password='password2')
        post2 = Post.objects.create(title='Title2', description='Description2', user=user2)
        url = reverse('api_post_list_create')
        response = self.client.get(url, {'username': user2.username}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        post_response = response.data['results'][0]
        self.assertEqual(post_response['user'], user2.id)

    def test_list_top50(self):
        post = Post.objects.create(title='Title', description='Description', user=self.user)
        user2 = User.objects.create_user(username='billy', email="billy@billy.com", password='password2')
        post2 = Post.objects.create(title='Title2', description='Description2', user=user2)
        post3 = Post.objects.create(title='Title3', description='Description3', user=user2)
        fav = Favorite.objects.create(post=post, user=self.user)
        fav2 = Favorite.objects.create(post=post, user=self.user)
        fav3 = Favorite.objects.create(post=post, user=self.user)
        fav4 = Favorite.objects.create(post=post2, user=self.user)
        fav5 = Favorite.objects.create(post=post2, user=self.user)
        fav6 = Favorite.objects.create(post=post3, user=self.user)
        url = reverse('api_top_50_list', kwargs={'top50': 'top50'})
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 3)
        first_post = response.data['results'][0]
        second_post = response.data['results'][1]
        third_post = response.data['results'][2]
        self.assertEqual(first_post['id'], post.id)
        self.assertEqual(second_post['id'], post2.id)
        self.assertEqual(third_post['id'], post3.id)