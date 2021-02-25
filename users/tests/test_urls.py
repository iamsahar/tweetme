# # from django.urls import reverse, resolve


# # class TestUrls:
# #     def test_login_url(self):
# #         path = reverse('login')
# #         assert resolve(path).view_name=='login'

# #     def test_logout_url(self):
# #         path = reverse('logout')
# #         assert resolve(path).view_name=='logout'

# #     def test_register_url(self):
# #         path = reverse('register')
# #         assert resolve(path).view_name=='register'

# #     def test_profile_url(self):
# #         path = reverse('profile')
# #         assert resolve(path).view_name=='profile'


# # def test_an_admin_view(admin_client):
# #     response = admin_client.get('/admin/')
# #     assert response.status_code == 200


# from django import urls


# def test_profile_url(client):

#     url = urls.reverse('profile')
#     resp = client.get(url)
#     assert resp.status_code == 302