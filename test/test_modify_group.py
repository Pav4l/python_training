from model.group import Group
import random

def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = Group(name="group_mod", header="header_mod", footer="footer_mod")
    old_groups = db.get_group_list()
    group_modify = random.choice(old_groups)
    app.group.modify_group_by_id(group, group_modify.id)
    for row in old_groups:
        if row.id == group_modify.id:
            row.name = group.name
            row.header = group.header
            row.footer = group.footer
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)