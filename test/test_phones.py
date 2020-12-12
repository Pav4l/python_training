from random import randrange
import re

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