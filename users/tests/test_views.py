# # from django.test import TestCase

# # class TestSignupView(TestCase):

# #     def setUp(self):
# #         self.username = "user"
# #         self.email = "user@test.com"
# #         self.password = "test.1234"

# #     def test_signup_view(self):


# import pytest
# from django import urls


# @pytest.mark.django_db
# def test_register(client):
#     register_url = urls.reverse('register')
#     resp = client.post(register_url, {
#         "username": "sahar",
#         "email": "sahar@test.com",
#         "password1": "123456",
#         "password2": "123456"
#     })
