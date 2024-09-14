import pytest
from http import HTTPStatus
from django.urls import reverse
from django.contrib.auth.models import Permission

def test_contacts_thanks(client):
    #Given:
    name = 'Rodrigo'
    #WHEN:
    response = client.get(reverse("contacts:thanks", args=(name,)))
    #WHEN:
    assert response.status_code == HTTPStatus.OK
    assert f"Obrigado {name}!" in response.content.decode()


def test_contact_create_unauthenticated_user(client):
    #Given:
    url = f"{reverse('accounts:login')}?next={reverse('contacts:create')}"
    #WHEN:
    response = client.get("/contacts/create/")
    #WHEN:
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == url


@pytest.mark.django_db
def test_contact_create_success(client, django_user_model):
    #Given:
    data = {"subject": "subject@subjectemail.com", "message": "Hello World!", "sender": "sender@senderemail.com", "cc_myself": True}

    username = "test_user"
    email= "email@testemail.com"
    password = "123test"
    user = django_user_model.objects.create_user(username=username, email=email, password=password)

    permission = Permission.objects.get(codename="add_contact")
    user.user_permissions.add(permission)

    #WHEN:
    client.force_login(user)
    response = client.post(reverse("contacts:create"), data)
    
    #WHEN:
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse("contacts:thanks", args=(data["subject"],))
    