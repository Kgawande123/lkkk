from django.db import models
from django. core import validators
# Create your models here.
class Voter(models.Model):
    gen = [("female","female"),("male","male"), ("other","other")]
    vid = models.AutoField(primary_key=True,auto_created=True)
    f_name = models.CharField(max_length=23, validators=[validators.RegexValidator('^[A-Za-z]{2,}$',
                                                        message="Enter a First LetterCapital")])
    l_name = models.CharField(max_length=23,validators=[validators.RegexValidator('^[A-Za-z]{2,}$',
                                                                                  message="First Letter Capital")])
    gender = models.CharField(max_length=23,choices=gen)
    pincode = models.IntegerField(validators=[validators.RegexValidator('^[1-9]{1}[0-9]{2}[0-9]{3}$',message="add 6 digit code")])
    contact = models.BigIntegerField()
    address = models.CharField(max_length=23)
    city = models.CharField(max_length=23)
    state = models.CharField(max_length=23)
