import pytest
from django import urls


@pytest.mark.django_db
def test_redirect_to_home_when_logged_in(client):
    """Verify we redirect to the home page when a user is logged in"""
    url = urls.reverse('login')
    resp = client.post(url, {
        "username": "sahar",
        "password": "123456",
    })
    assert resp.status_code == 200
    assert resp.url == urls.reverse('/')


def test_redirect_to_login_when_logged_out(client):
    """Verify we redirect to the login page when a user is not logged in"""
    url = urls.reverse('logout')
    resp = client.get(url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('login')


@pytest.mark.django_db
def test_redirect_to_login_when_register(client):
    """Verify we redirect to the login page when a user is register"""
    url = urls.reverse('register')
    resp = client.post(url, {
        "username": "sahar",
        "email": "sahar@test.com",
        "password1": "123456",
        "password2": "123456"
    })
    assert resp.status_code == 200
    assert resp.url == urls.reverse('login')


@pytest.mark.django_db
def test_redirect_to_profile(client):
    """Verify we redirect to the profile page"""
    url = urls.reverse('profile')
    resp = client.get(url)
    assert resp.status_code == 302
