# import pytest
# # # from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

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
# def user():
#     return User.objects.create(is_active=True)

# @pytest.mark.django_db
# def test_deactivate(user):
#     user.deactivate()
#     assert not user.is_active

# @pytest.mark.django_db
# def test_deactivate_activate(user):
#     user.deactivate()
#     user.activate()
#     assert user.is_active

# def test(client):
#     response = client.post(
#         'register/', data={"username": "sahar", "email": "sahar@test.com", "password": "123456"})
#     assert User.objects.count == 1
#     assert user.object.last().username == 'sahar'
