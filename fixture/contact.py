from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_and_new_contact_page()
        self.fill_contact_form(contact)
        # submit and_new_contact page
        wd.find_element_by_name("submit").click()
        #wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def select_day(self, add_day, number):
        wd = self.app.wd
        if number is not None:
            Select(wd.find_element(By.NAME, add_day)).select_by_visible_text(number)
            wd.find_element(By.NAME, add_day).click()

    def select_month(self, add_month, month):
        wd = self.app.wd
        if month is not None:
            Select(wd.find_element(By.NAME, add_month)).select_by_visible_text(month)
            wd.find_element(By.NAME, add_month).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

        self.select_day("bday", contact.bday)
        #wd.find_element_by_xpath("//option[@value='1']").click()
        self.select_month("bmonth", contact.bmonth)
        #wd.find_element_by_xpath("//option[@value='January']").click()

        self.change_field_value("byear", contact.byear)

        self.select_day("aday", contact.aday)
        #wd.find_element_by_xpath("(//option[@value='1'])[2]").click()
        self.select_month("amonth", contact.amonth)
        #wd.find_element_by_xpath("(//option[@value='January'])[2]").click()

        self.change_field_value("ayear", contact.ayear)

        #wd.find_element_by_name("new_group").click()
        #Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.new_group)
        #wd.find_element_by_xpath("//option[@value='[none]']").click()

        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def open_and_new_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    #def open_home_page(self):
    #    wd = self.app.wd
    #    wd.get("http://localhost/addressbook/")

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements(By.XPATH, "//form[2]/div[1]/input")) > 0):
            wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contacts_page()

    def edit(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # button "Edit"
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        #edit contact
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # button "Edit"
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        #edit contact
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_contacts_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()