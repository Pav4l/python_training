# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    #app.open_home_page()
    app.contact.open_and_new_contact_page()
    app.contact.create(Contact(firstname="Ivan", lastname="Ivanov", company="test1", address="test2", mobile="+799999999999", middlename="123456",
                               nickname="122", title="123", home="hjhskadf",
                               work="12132", fax="123132", email="112", email2="112", email3="1212", homepage="112",
                               bmonth="January", byear="1970", bday="1", aday="1", amonth="January",
                               new_group="asadasd", ayear="2000", address2="123132", phone2="123123", notes="123123"))
    app.return_to_home_page()

def test_add_empty_contact(app):
    #app.open_home_page()
    app.contact.open_and_new_contact_page()
    app.contact.create(Contact(firstname="", lastname="", company="", address="", mobile="", middlename="",
                               nickname="", title="", home="",
                               work="", fax="", email="", email2="", email3="", homepage="",
                               new_group="", address2="", phone2="", notes="", bmonth="February", byear="1978", bday="10", aday="15", amonth="February", ayear="1999"))
    app.return_to_home_page()
