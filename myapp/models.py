from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import date

# Create your models here.

class register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class mcourse(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class detailcourse(models.Model):
    program = models.ForeignKey(mcourse, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class admission(models.Model):
    formno = models.CharField(max_length=100, null=True)
    usersname = models.CharField(max_length=200, null=True)
    mobile = models.BigIntegerField(null=True)
    #btime = models.CharField(max_length=50, null=True)
    dob = models.CharField(max_length=50, null=True)
    doa = models.CharField(max_length=50, null=True)
    course = models.CharField(max_length=100, null=True)
    batch_time = models.CharField(max_length=20,null=True)
    image = models.ImageField(upload_to='photos', null=True)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))

    admin_photo.allow_tags = True

    def _str__(self):
        return self.usersname



class certificate2(models.Model):
    regno = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=50, null=True)
    main_course = [
        ("BASIC COMPUTER & MS-OFFICE","BASIC COMPUTER & MS-OFFICE"),
        ("DCA (DIPLOMA IN COMPUTER APPLICATION)","DCA (DIPLOMA IN COMPUTER APPLICATION)"),
        ("TALLY PRIME WITH GST ","TALLY PRIME WITH GST "),
        ("TALLY ERP WITH GST ", "TALLY ERP WITH GST "),
        ("DTP (Desktop Publishing)","DTP (Desktop Publishing)"),
        ("Java Programming","Java Programming"),
        ("C Programming", "C Programming"),
        ("C++ Programming", "C++ Programming"),
        ("C & C++ Programming", "C & C++ Programming"),
        ("C , C++ & Java Programming", "C , C++  & Java Programming"),
        ("Website Designing","Website Designing"),
        ("DIT (Diploma in Information Technology)","DIT (Diploma in Information Technology)"),
        ("ADCA (ADVANCE DIPLOMA IN COMPUTER APPLICATION)","ADCA (ADVANCE DIPLOMA IN COMPUTER APPLICATION)"),
        ("ADSE (ADVANCE DIPLOMA IN SOFTWARE ENGINEERING)","ADSE (ADVANCE DIPLOMA IN SOFTWARE ENGINEERING)"),
        ("AUTOCAD 2-D & 3-D","AUTOCAD 2-D & 3-D"),
        ("BASIC COMPUTER & TYPING ( ENGLISH )","BASIC COMPUTER & TYPING ( ENGLISH )"),
        ("BASIC COMPUTER & TYPING ( GUJARATI )","BASIC COMPUTER & TYPING ( GUJARATI )"),
        ("BASIC COMPUTER & TYPING ( ENGLISH & GUJARATI )","BASIC COMPUTER & TYPING (ENGLISH & GUJARATI )"),
        ("CCC (CERTIFICATE IN COMPUTER CONCEPT)","CCC (CERTIFICATE IN COMPUTER CONCEPT)"),
        ("LINUX & SHELL PROGRAMMING","LINUX & SHELL PROGRAMMING"),
        ("PYTHON PROGRAMMING", "PYTHON PROGRAMMING"),
        ("MS-OFFICE & TALLY ", "MS-OFFICE & TALLY "),
        ("DIPLOMA IN HARDWARE","DIPLOMA IN HARDWARE")

    ]
    course = models.CharField(max_length=100,choices=main_course, null=True)
    coudetail = [
        ("(Typing,Word,Excel,Powerpoint,Outlook & Internet etc.)","(Typing,Word,Excel,Powerpoint,Outlook & Internet etc.)"),
        ("(Ms-Office, Tally with GST, DTP & Internet Technologies)","(Ms-Office, Tally with GST, DTP & Internet Technologies)"),
        ("(Accounting, Inventory, Payroll, Banking, GST & TDS etc.)","(Accounting, Inventory, Payroll, Banking, GST & TDS etc.)"),
        ("(Page-Maker, Corel Draw & Photoshop etc..)","(Page-Maker, Corel Draw & Photoshop etc..)"),
        ("HTML, CSS, JAVA-Script,Wordpress,Photoshop,Uploading etc.", "HTML, CSS, JAVA-Script,Wordpress,Photoshop,Uploading etc."),
        ("TYPING IN ENGLISH (40 WPM) & GUJARATI (30 WPM)","TYPING IN ENGLISH (40 WPM) & GUJARATI (30 WPM)"),
        ("TYPING IN ENGLISH (35 WPM) & GUJARATI (30 WPM)","TYPING IN ENGLISH (35 WPM) & GUJARATI (30 WPM)"),
        ("--- ","---")
    ]
    detail = models.CharField(max_length=200,choices=coudetail, null=True)
    enroll = models.CharField(max_length=30, null=True)
    grade = models.CharField(max_length=200, null=True)
    duration = models.CharField(max_length=20, null=True)
    date = models.CharField(max_length=25, null=True)
    image = models.ImageField(upload_to='photos', null=True)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))

    admin_photo.allow_tags = True

    def __str__(self):
        return self.name

class fees(models.Model):
    form_no = models.CharField(max_length=200)
    total = models.BigIntegerField()
    paid = models.BigIntegerField()
    due = models.BigIntegerField()

    def __str__(self):
        return self.form_no

class paid_log(models.Model):
    form_no = models.CharField(max_length=200)
    fee = models.BigIntegerField()
    fee_date = models.CharField(max_length=50, null=True)


    def __str__(self):
        return f'{self.form_no} -- {self.fee_date}'


class Course(models.Model):
    EXAM_MODES = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    ]
    course_name = models.CharField(max_length=125)
    course_alias = models.CharField(max_length=100)
    certificate_name = models.CharField(max_length=150)
    description = models.TextField()
    course_duration = models.CharField(max_length=50)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2)
    techs = models.TextField()
    total_students = models.IntegerField()
    rating = models.FloatField()
    exam_mode = models.CharField(choices=EXAM_MODES, max_length=100, default='Offline')
    exam_duration = models.CharField(max_length=50)
    no_of_questions = models.IntegerField()
    passing_percentage = models.FloatField()
    eligibility = models.TextField()

    def __str__(self):
        return self.course_alias
