from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Pablo"))
    group = random.choice(db.get_group_list())
    contact = random.choice(db.get_contact_list())
    if contact in db.get_contacts_in_group(group):
        app.contact.delete_from_group(contact, group)
    app.contact.add_contact_to_group(contact.id, group.id, group.name)
    assert contact in db.get_contacts_in_group(group)