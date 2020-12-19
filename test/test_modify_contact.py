from model.contact import Contact
import random

def test_modify_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Pablo", lastname="Rodrigez"))
    contact = Contact(firstname="Sidorov")
    old_contacts = db.get_contact_list()
    contact_modify = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact, contact_modify.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
#   for row in old_contacts:
#        if row.id == contact_modify.id:
#            row.firstname = contact_modify.firstname
#            row.middlename = contact_modify.middlename
#            row.lastname = contact_modify.lastname
#            row.nickname = contact_modify.nickname
#            row.title = contact_modify.title
#            row.company = contact_modify.company
#            row.address = contact_modify.address
#            row.home = contact_modify.home
#            row.mobile = contact_modify.mobile
#            row.work = contact_modify.work
#            row.fax = contact_modify.fax
#            row.email = contact_modify.email
#            row.email2 = contact_modify.email2
#            row.email3 = contact_modify.email3
#            row.homepage = contact_modify.homepage
#            row.bday = contact_modify.bday
#            row.bmonth = contact_modify.bmonth
#            row.byear = contact_modify.byear
#            row.aday = contact_modify.aday
#            row.amonth = contact_modify.amonth
#            row.ayear = contact_modify.ayear
#            row.group = contact_modify.group
#            row.address2 = contact_modify.address2
#            row.phone2 = contact_modify.phone2
#            row.notes = contact_modify.notes
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)