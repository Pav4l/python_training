from model.contact import Contact
#import random
#import string
#import calendar


testdata = [Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1",
                    title="title1", company="company1", address="address1",
                    home="home", mobile="mobile", work="work", fax="fax",
                    email="email", email2="email2", email3="email3", homepage="homepage",
                    bday="1", bmonth="-", byear="1980", aday="2", amonth="-", ayear="2000", group="[none]",
                    address2="address2", phone2="phone2", notes="notes")]

#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + " "*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#def random_phone(maxlen):
#    symbols = string.digits + "()- "
#    return "".join([random.choice(symbols) for i in range(maxlen)])

#def test_random_group_name(app):
#    return random.choice(app.group.get_group_list()).name

#testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
#                    home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="",
#                    bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", group="[none]", address2="",
#                    phone2="", notes="")] + [
#               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
#                       lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
#                       title=random_string("title", 10), company=random_string("company", 10),
#                       address=random_string("address", 10), home=random_phone(10),
#                       mobile=random_phone(10), work=random_phone(10), fax=random_phone(10),
#                       email=random_string("email1", 10), email2=random_string("email2", 10),
#                       email3=random_string("email3", 10), homepage=random_string("homepage", 10),
#                       bday=str(random.randrange(31)), bmonth=random.choice(calendar.month_name[1:13]),
#                       byear=random.randrange(1900, 2020), aday=str(random.randrange(31)),
#                       amonth=random.choice(calendar.month_name[1:13]), ayear=random.randrange(1900, 2030),
#                       group="rand", address2=random_string("address2", 10), phone2=random_phone(10),
#                       notes=random_string("notes", 10))
#               for i in range(5)
#]