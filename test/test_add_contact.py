# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    #app.open_home_page()
    app.contact.open_and_new_contact_page()
    app.contact.create(
        Contact(firstname="Ivan", middlename="123456", lastname="Ivanov", company="test1", address="test2",
                mobile="+799999999999", nickname="122", title="123", home="hjhskadf", work="12132", fax="123132",
                email="112", email2="112", email3="1212", homepage="112", bmonth="January", byear="1970", bday="1",
                amonth="January", ayear="2000", aday="1", new_group="None", address2="123132", phone2="123123",
                notes="123123"))
    app.return_to_home_page()

def test_add_empty_contact(app):
    #app.open_home_page()
    app.contact.open_and_new_contact_page()
    app.contact.create(
        Contact(firstname="", middlename="", lastname="", company="", address="", mobile="", nickname="", title="",
                home="", work="", fax="", email="", email2="", email3="", homepage="", bmonth="February", byear="1978",
                bday="10", amonth="February", ayear="1999", aday="15", new_group="None", address2="", phone2="",
                notes=""))
    app.return_to_home_page()
