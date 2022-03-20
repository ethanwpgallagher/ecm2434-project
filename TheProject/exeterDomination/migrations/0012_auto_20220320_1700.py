# Generated by Django 4.0.3 on 2022-03-20 17:00

from django.db import migrations

from django.contrib.auth.models import Permission


def apply_migration(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    Group = apps.get_model("auth", "Group")
    Permissions = apps.get_model('auth', 'Permission')
    Group.objects.using(db_alias).bulk_create(
        [Group(name="Game Masters")]
    )
    group2 = Group.objects.get(name="Game Masters")
    print(group2)
    l1 = ["add_locations", "view_locations", "view_users", "add_coords", "view_coords"]
    for l in l1:
        group2.permissions.add(Permissions.objects.get(codename=l))

    group2.save()


def revert_migration(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name="Game Masters").delete()


class Migration(migrations.Migration):
    dependencies = [
        ('exeterDomination', '0011_alter_coords_options_alter_locations_options_and_more'),
    ]

    operations = [
        migrations.RunPython(apply_migration)
    ]
