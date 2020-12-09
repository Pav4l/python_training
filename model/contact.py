from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, company=None, address=None, mobile=None, nickname=None,
                title=None, home=None, work=None, fax=None, email=None, email2=None, email3=None, homepage=None,
                bmonth=None, byear=None, bday=None, amonth=None, ayear=None, aday=None, new_group=None, address2=None,
                phone2=None, notes=None, id = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.company = company
        self.address = address
        self.mobile = mobile
        self.nickname = nickname
        self.title = title
        self.home = home
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bmonth = bmonth
        self.byear = byear
        self.bday = bday
        self.amonth = amonth
        self.ayear = ayear
        self.aday = aday
        self.new_group = new_group
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
                (self.firstname is None or other.firstname is None or self.firstname == other.firstname) and \
                (self.lastname is None or other.lastname is None or self.lastname == other.lastname)
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize