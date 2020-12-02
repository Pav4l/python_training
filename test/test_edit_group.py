from model.group import Group

def test_edit_group(app):
    app.group.edit(Group(name="group_new", header="header_new", footer="footer_new"))
