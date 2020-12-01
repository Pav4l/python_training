from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="group_new", header="header_new", footer="footer_new"))
    app.session.logout()