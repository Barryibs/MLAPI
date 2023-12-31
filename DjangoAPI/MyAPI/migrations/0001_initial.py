# Generated by Django 4.2.6 on 2023-10-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="approvals",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Firstname", models.CharField(max_length=15)),
                ("Lastname", models.CharField(max_length=15)),
                ("Dependents", models.IntegerField(default=0)),
                ("ApplicantIncome", models.IntegerField(default=0)),
                ("CoapplicantIncome", models.CharField(max_length=15)),
                ("LoanAmount", models.IntegerField(default=0)),
                ("Loan_Amount", models.IntegerField(default=0)),
                ("Loan_Amount_Term", models.IntegerField(default=0)),
                ("Credit_History", models.IntegerField(default=0)),
                (
                    "Gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=15
                    ),
                ),
                (
                    "Married",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=15
                    ),
                ),
                (
                    "Education",
                    models.CharField(
                        choices=[
                            ("Graduated", "Graduated"),
                            ("Not Graduated", "Not Graduated"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "Self_Employed",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=15
                    ),
                ),
                (
                    "Area",
                    models.CharField(
                        choices=[
                            ("Rural", "Rural"),
                            ("Semi-Urban", "Semi-Urban"),
                            ("Urban", "Urban"),
                        ],
                        max_length=15,
                    ),
                ),
            ],
        ),
    ]
