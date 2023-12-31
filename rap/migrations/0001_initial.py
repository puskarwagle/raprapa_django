# Generated by Django 4.2.4 on 2023-08-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('expiry_date', models.DateField()),
                ('paid', models.BooleanField()),
                ('photo', models.CharField(max_length=255)),
                ('membership_type', models.CharField(max_length=15)),
                ('membership_duration', models.CharField(max_length=15)),
                ('birth_date', models.DateField()),
                ('reg_number', models.IntegerField()),
                ('voter_id', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('perm_province', models.CharField(max_length=100)),
                ('perm_district', models.CharField(max_length=100)),
                ('perm_constituency', models.CharField(max_length=100)),
                ('perm_constituencyB', models.CharField(max_length=100)),
                ('perm_palika', models.CharField(max_length=100)),
                ('perm_wardno', models.IntegerField()),
                ('perm_voting_center', models.CharField(max_length=100)),
                ('current_province', models.CharField(max_length=100)),
                ('current_district', models.CharField(max_length=100)),
                ('current_constituency', models.CharField(max_length=100)),
                ('current_constituencyB', models.CharField(max_length=100)),
                ('current_palika', models.CharField(max_length=100)),
                ('current_wardno', models.IntegerField()),
                ('current_voting_center', models.CharField(max_length=100)),
                ('father_mother_name', models.CharField(max_length=255)),
                ('husband_or_wife_name', models.CharField(max_length=255)),
                ('family_count', models.IntegerField()),
                ('education', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=100)),
                ('marital_status', models.CharField(max_length=20)),
                ('caste', models.CharField(max_length=20)),
                ('year_joined', models.DateField()),
                ('membership_date', models.DateField()),
                ('membership_id', models.IntegerField()),
                ('past_responsibility', models.CharField(max_length=255)),
                ('company1', models.CharField(max_length=255)),
                ('jobtitle1', models.CharField(max_length=255)),
                ('worktenure1', models.IntegerField()),
                ('company2', models.CharField(max_length=255)),
                ('jobtitle2', models.CharField(max_length=255)),
                ('worktenure2', models.IntegerField()),
                ('company3', models.CharField(max_length=255)),
                ('jobtitle3', models.CharField(max_length=255)),
                ('worktenure3', models.IntegerField()),
                ('company4', models.CharField(max_length=255)),
                ('jobtitle4', models.CharField(max_length=255)),
                ('worktenure4', models.IntegerField()),
                ('company5', models.CharField(max_length=255)),
                ('jobtitle5', models.CharField(max_length=255)),
                ('worktenure5', models.IntegerField()),
                ('signature_of_approver', models.CharField(max_length=255)),
                ('name_of_approver', models.CharField(max_length=255)),
                ('position_of_approver', models.CharField(max_length=100)),
                ('signature_of_applicant', models.CharField(max_length=255)),
                ('application_date', models.DateField(auto_now_add=True)),
                ('district_president_name', models.CharField(max_length=255)),
                ('district_president_signature', models.CharField(max_length=255)),
                ('district_president_stamp', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'raprapa_members',
            },
        ),
    ]
