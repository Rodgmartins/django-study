import pytest
from http import HTTPStatus
from django.urls import reverse

def test_contacts_thanks(client):
    #Given:
    name = 'Rodrigo'
    #WHEN:
    response = client.get(f"/contacts/thanks/{name}")
    #WHEN:
    assert response.status_code == HTTPStatus.OK
    assert response.content.decode() == f"Obrigado {name}!"

def test_unauthenticated_user(client):
    #Given:
    url = f"{reverse('accounts:login')}?next={reverse('contacts:create')}"
    #WHEN:
    response = client.get("/contacts/create/")
    #WHEN:
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == url