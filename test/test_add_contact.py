# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    if contact.group == "rand":
        contact.group = random.choice(app.group.get_group_list()).name
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=" ".join(contact.firstname.strip().split()),
                           lastname=" ".join(contact.lastname.strip().split()))
        db_list = list(map(clean, db.get_contact_list()))
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)