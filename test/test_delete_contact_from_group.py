from fixture.orm import ORMFixture
from model.group import Group
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_delete_contact_from_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())
    if len(db.get_contacts_in_group(group)) == 0:
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact.id, group.id, group.name)
    contact = random.choice(db.get_contacts_in_group(group))
    app.contact.delete_contact_from_group(group.id, contact.id)
    assert contact in db.get_contacts_not_in_group(group)