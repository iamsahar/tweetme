# from django.test import TestCase
# from users.forms import SignUpForm
# from django.contrib.auth.models import User


# class SignUpFormTest(TestCase):
#     def test_valid_form(self):
#         u = User.objects.create(
#             username='username',
#             email='username@test.com',
#             password='1234'
#         )
#         data = {
#             'username': u.username,
#             'email': u.email,
#             'password1': u.password,
#             'password2': u.password,
#         }
#         form = SignUpForm(data=data)
#         print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', form)
#         self.assertTrue(form.is_valid())


#     def test_invalid_form(self):
#         u = User.objects.create(
#             username='username',
#             email='username@test.com',
#             password=''
#         )
#         data = {
#             'username': u.username,
#             'email': u.email,
#             'password1': u.password,
#             'password2': u.password,
#         }
#         form = SignUpForm(data=data)
#         self.assertFalse(form.is_valid())

