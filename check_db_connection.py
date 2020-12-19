import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id="256"))
    #l = db.get_contacts_in_group(Group(id="269"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()

#try:
#    contacts = db.get_contact_list()
#    for contact in contacts:
#        print(contact)
#    print(len(contacts))
#finally:
#    db.destroy()