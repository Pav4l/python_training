from model.contact import Contact
import random

def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Pablo", lastname="Rodrigez"))
    contact = Contact(firstname="Sidorov")
    old_contacts = db.get_contact_list()
    contact_modify = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact, contact_modify.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    for row in old_contacts:
        if row.id == contact_modify.id:
            row.firstname = contact.firstname
            row.middlename = contact.middlename
            row.lastname = contact.lastname
            row.nickname = contact.nickname
            row.title = contact.title
            row.company = contact.company
            row.address = contact.address
            row.home = contact.home
            row.mobile = contact.mobile
            row.work = contact.work
            row.fax = contact.fax
            row.email = contact.email
            row.email2 = contact.email2
            row.email3 = contact.email3
            row.homepage = contact.homepage
            row.bday = contact.bday
            row.bmonth = contact.bmonth
            row.byear = contact.byear
            row.aday = contact.aday
            row.amonth = contact.amonth
            row.ayear = contact.ayear
            row.group = contact.group
            row.address2 = contact.address2
            row.phone2 = contact.phone2
            row.notes = contact.notes
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)