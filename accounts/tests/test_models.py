# import pytest
# from django.contrib.auth import get_user_model
# from users.models import Profile

# User = get_user_model()


# @pytest.fixture
# def user_client(client):
#     """
#     User fixture for tests with unprivileged user
#     """
#     user = User.objects.create_user(
#         username='user',
#         email='user@test.com',
#         password='pass1234',
#     )
#     response = client.post(reverse('register'), data={
#                            'username': 'user', 'email': 'sahar@test.com', 'password': 'pass1234'})

#     assert response.status_code == 302
#     return user_client


# @pytest.fixture
# def user_client():
#     user = User.objects.create(username="sahar",
#                                email="sahar@test.com",
#                                password="123456")
#     return User.objects.create(user)


# def profile_client():
#     profile = Profile.objects.create(user=user_client)
#     return Profile.objects.create(profile)

# # @pytest.mark.django_db
# # def test_deactivate(user):
# #     user.deactivate()
# #     assert not user.is_active

# # @pytest.mark.django_db
# # def test_deactivate_activate(user):
# #     user.deactivate()
# #     user.activate()
# #     assert user.is_active


# def test(client):
#     response = client.post(
#         'profile/', data={"user": "sahar"})
#     assert Profile.objects.count == 1
#     assert profile_client.objects.last().user == "sahar"
