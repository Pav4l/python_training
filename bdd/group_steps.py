from pytest_bdd import given, when, then
from model.group import Group

@given('a group list', target_fixture="group_list")
def group_list(db):
    return db.get_group_list()

@given('a group with <name>, <header> and <footer>', target_fixture="new_group")
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add new group with <name>, <header> and <footer>')
def add_new_group(app, new_group):
    app.group.create(new_group)

@then ('the new group list is equal to the old list with the added group')
def verify_group_edit(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)