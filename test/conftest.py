import pytest
from model.group import Group
from fixture.application import Application
from model.contact import Contact
from fixture.application_contact import Application_Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture