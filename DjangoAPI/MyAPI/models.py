from django.db import models

# Create your models here.

class approvals(models.Model):
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    
    MARRIED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    
    GRADUATED_CHOICES = (
        ('Graduated', 'Graduated'),
        ('Not Graduated', 'Not Graduated')
    )
    
    SELFEMPLOYED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    
    PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('Semi-Urban', 'Semi-Urban'),
        ('Urban', 'Urban')
    )
    Firstname = models.CharField(max_length=15)
    Lastname = models.CharField(max_length=15)
    Dependents = models.IntegerField(default=0)
    ApplicantIncome = models.IntegerField(default=0)
    CoapplicantIncome = models.IntegerField(default=15)
    LoanAmount = models.IntegerField(default=0)
    Loan_Amount_Term = models.IntegerField(default=0)
    Credit_History = models.IntegerField(default=0)
    Gender = models.CharField(max_length=15, choices = GENDER_CHOICES)
    Married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    Education = models.CharField(max_length=15, choices=GRADUATED_CHOICES)
    Self_Employed = models.CharField(max_length=15, choices=SELFEMPLOYED_CHOICES)
    Area = models.CharField(max_length=15, choices=PROPERTY_CHOICES)

    
    def __str__(self):
        return '{}, {}'.format(self.Firstname, self.Lastname)