from django.db import models

# Create your models here.

class Client(models.Model):
    
    SINGLE = 'SI'
    MARRIED = 'MA'
    WIDOWED = 'WI'
    LEGALLY_SEPARATED = 'LS'
    
    CIVIL_STATUS_CHOICES = [
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (WIDOWED, 'Widowed'),
        (LEGALLY_SEPARATED, 'Legally Separated')
    ]
    
    MALE = 'M'
    FEMALE = 'F'
    NEUTRAL = 'NE'
    
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NEUTRAL, 'N/A')
    ]
    
    accountName = models.CharField(
        max_length = 20,
        blank = False
    )
    lastName = models.CharField(
        max_length = 20,
        blank = False
    )
    firstName = models.CharField(
        max_length = 20,
        blank = False
    )
    middleName = models.CharField(
        max_length = 20,
        blank = False
    )
    suffix = models.CharField(
        max_length = 3,
        blank = True
    )
    birthdate = models.DateField(
        blank = False,
        
    )
    sex = models.CharField(
        max_length = 6,
        choices = SEX_CHOICES,
        blank = False
    )
    civilStatus = models.CharField(
        max_length = 20,
        choices = CIVIL_STATUS_CHOICES,
        blank = False
    )
    weight = models.DecimalField(
        max_digits = 4,
        decimal_places = 2,
        blank = False
    )
    height = models.CharField(
        max_length = 4,
        blank = False
    )
    monthlyIncome = models.DecimalField(
        max_digits = 8,
        decimal_places = 2,
        blank = False
    )
    profession = models.CharField(
        max_length = 30,
        blank = False
    )
    mailingAddress1 = models.TextField(
        blank = False
    )
    mailingAddress2 = models.TextField(
        default = "",
        blank = True
    )
    sameMailingAddress = models.BooleanField(
        default = False
    )
    clientPhoto = models.ImageField(
        upload_to = 'clients/images/%Y-%m-%d/'
    )
    clientSignature = models.ImageField(
        upload_to = 'clients/signatures/%Y-%m-%d/'
    )