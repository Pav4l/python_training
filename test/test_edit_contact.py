from model.contact import Contact

def test_edit_contact(app):
    #app.open_home_page()
    app.contact.open_and_new_contact_page()
    app.contact.edit(
        Contact(firstname="Petr", lastname="Petrov", company="new_company", address="address2", mobile="+78888888888",
                middlename="middlename",
                nickname="new1", title="new2", home="new_home1",
                work="work1", fax="work2", email="email1", email2="email2", email3="email3", homepage="234",
                new_group="", bmonth="February", byear="1971", bday="2", amonth="February",
                ayear="2005", aday="17", address2="address_new", phone2="333222333", notes="no123"))
    app.return_to_home_page()