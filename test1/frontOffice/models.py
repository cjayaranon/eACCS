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
        verbose_name = 'Account Name',
        max_length = 20,
        blank = False
    )
    lastName = models.CharField(
        verbose_name = 'Last Name',
        max_length = 20,
        blank = False
    )
    firstName = models.CharField(
        verbose_name = 'First Name',
        max_length = 20,
        blank = False
    )
    middleName = models.CharField(
        verbose_name = 'Middle Name',
        max_length = 20,
        blank = False
    )
    suffix = models.CharField(
        verbose_name = 'Suffix',
        max_length = 3,
        blank = True
    )
    birthdate = models.DateField(
        verbose_name = 'Date of Birth',
        blank = False,
        
    )
    sex = models.CharField(
        max_length = 6,
        choices = SEX_CHOICES,
        blank = False
    )
    civilStatus = models.CharField(
        verbose_name = 'Civil Status',
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
        verbose_name = 'Monthly Income',
        max_digits = 8,
        decimal_places = 2,
        blank = False
    )
    profession = models.CharField(
        max_length = 30,
        blank = False
    )
    mailingAddress1 = models.TextField(
        verbose_name = 'Mailing Address 1',
        blank = False
    )
    mailingAddress2 = models.TextField(
        verbose_name = 'Mailing Address 2',
        default = "",
        blank = True
    )
    sameMailingAddress = models.BooleanField(
        default = False
    )
    clientPhoto = models.ImageField(
        verbose_name = 'Client Photo',
        upload_to = 'clients/images/%Y-%m-%d/'
    )
    clientSignature = models.ImageField(
        verbose_name = 'Signature Photo',
        upload_to = 'clients/signatures/%Y-%m-%d/'
    )
    