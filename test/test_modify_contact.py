from model.contact import Contact

def test_modify_contact_firstname_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Pablo", lastname="Rodrigez"))
    app.contact.modify_first_contact(Contact(firstname="New_test"))