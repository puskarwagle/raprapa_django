from django.db import models
from django.contrib import admin

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='unknown')
    role = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiry_date = models.DateField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    photo = models.CharField(max_length=255, blank=True, null=True)
    
    membership_type = models.CharField(max_length=15, blank=True, null=True)
    membership_duration = models.CharField(max_length=15, blank=True, null=True)

    birth_date = models.DateField(blank=True, null=True)
    membership_date = models.DateField(blank=True, null=True)

    citizenship_number = models.IntegerField(blank=True, null=True)
    voter_id = models.IntegerField(blank=True, null=True)
    perm_wardno = models.IntegerField(blank=True, null=True)
    current_wardno = models.IntegerField(blank=True, null=True)
    family_count = models.IntegerField(blank=True, null=True)
    membership_id = models.IntegerField(blank=True, null=True)


    phone = models.CharField(
        blank=True,
        null=True,
        help_text="Enter a valid 10-digit phone number or leave it blank."
    )
    email = models.EmailField(max_length=255)
    perm_province = models.CharField(max_length=100, blank=True, null=True)
    perm_district = models.CharField(max_length=100, blank=True, null=True)
    perm_constituency = models.CharField(max_length=100, blank=True, null=True)
    perm_constituencyB = models.CharField(max_length=100, blank=True, null=True)
    perm_palika = models.CharField(max_length=100, blank=True, null=True)

    

    perm_voting_center = models.CharField(max_length=100, blank=True, null=True)
    current_province = models.CharField(max_length=100, blank=True, null=True)
    current_district = models.CharField(max_length=100, blank=True, null=True)
    current_constituency = models.CharField(max_length=100, blank=True, null=True)
    current_constituencyB = models.CharField(max_length=100, blank=True, null=True)
    current_palika = models.CharField(max_length=100, blank=True, null=True)
    current_voting_center = models.CharField(max_length=100, blank=True, null=True)
    father_mother_name = models.CharField(max_length=255, blank=True, null=True)
    husband_or_wife_name = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=50, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    caste = models.CharField(max_length=20, blank=True, null=True)

    # year_joined = models.IntegerField(blank=True, null=True)
    
    past_responsibility = models.CharField(max_length=255, blank=True, null=True)
    company1 = models.CharField(max_length=255, blank=True, null=True)
    jobtitle1 = models.CharField(max_length=255, blank=True, null=True)
    worktenure1 = models.IntegerField(blank=True, null=True)
    company2 = models.CharField(max_length=255, blank=True, null=True)
    jobtitle2 = models.CharField(max_length=255, blank=True, null=True)
    worktenure2 = models.IntegerField(blank=True, null=True)
    company3 = models.CharField(max_length=255, blank=True, null=True)
    jobtitle3 = models.CharField(max_length=255, blank=True, null=True)
    worktenure3 = models.IntegerField(blank=True, null=True)
    company4 = models.CharField(max_length=255, blank=True, null=True)
    jobtitle4 = models.CharField(max_length=255, blank=True, null=True)
    worktenure4 = models.IntegerField(blank=True, null=True)
    company5 = models.CharField(max_length=255, blank=True, null=True)
    jobtitle5 = models.CharField(max_length=255, blank=True, null=True)
    worktenure5 = models.IntegerField(blank=True, null=True)
    signature_of_approver = models.CharField(max_length=255, blank=True, null=True)
    name_of_approver = models.CharField(max_length=255, blank=True, null=True)
    position_of_approver = models.CharField(max_length=100, blank=True, null=True)
    signature_of_applicant = models.CharField(max_length=255, blank=True, null=True)
    application_date = models.DateField(auto_now_add=True)
    district_president_name = models.CharField(max_length=255, blank=True, null=True)
    district_president_signature = models.CharField(max_length=255, blank=True, null=True)
    district_president_stamp = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'raprapa_members'

# class MemberAdmin(admin.ModelAdmin):
#     model = Member
#     list_filter = ['gender', 'role', 'membership_type']  
#     search_fields = ['name', 'email', 'phone']

# admin.site.unregister(Member)  
# admin.site.register(Member, MemberAdmin)
