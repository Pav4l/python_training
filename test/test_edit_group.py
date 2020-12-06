from model.group import Group

def test_edit_group(app):
    old_groups = app.group.get_group_list()
    app.group.edit(Group(name="group_new", header="header_new", footer="footer_new"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
