# Generated by Django 4.2.4 on 2023-08-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rap', '0011_remove_member_year_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='membership_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]