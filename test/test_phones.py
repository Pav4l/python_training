from random import randrange
import re
from model.contact import Contact

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_on_contact_view_page(app):
    contact_from_home_page = app.contact.get_contact_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home == contact_from_edit_page.home
    assert contact_from_home_page.mobile == contact_from_edit_page.mobile
    assert contact_from_home_page.work == contact_from_edit_page.work
    assert contact_from_home_page.fax == contact_from_edit_page.fax
    assert contact_from_home_page.phone2 == contact_from_edit_page.phone2

def test_compare_some_contact_on_home_and_edit_pages(app):
    contacts_from_home_page = app.contact.get_contact_list()
    index = randrange(len(contacts_from_home_page))
    contact_from_home_page = contacts_from_home_page[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear(contact_from_home_page.firstname) == clear(contact_from_edit_page.firstname)
    assert clear(contact_from_home_page.lastname) == clear(contact_from_edit_page.lastname)
    assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)

def test_compare_contact_on_home_page_and_from_db(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contact_from_home_page)):
        assert clear(contact_from_home_page[i].firstname) == clear(contact_from_db[i].firstname)
        assert clear(contact_from_home_page[i].lastname) == clear(contact_from_db[i].lastname)
        assert clear(contact_from_home_page[i].address) == clear(contact_from_db[i].address)
        assert clear(contact_from_home_page[i].all_phones_from_home_page) == \
               clear(merge_phones_like_on_home_page(contact_from_db[i]))
        assert clear(contact_from_home_page[i].all_email_from_home_page) == \
               clear(merge_email_like_on_home_page(contact_from_db[i]))

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))