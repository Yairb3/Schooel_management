# Generated by Django 3.0.2 on 2020-01-25 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0006_classregistration_name'),
        ('student', '0032_auto_20200125_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=892486, unique=True),
        ),
        migrations.AlterField(
            model_name='enrolledstudent',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.ClassRegistration'),
        ),
        migrations.AlterUniqueTogether(
            name='enrolledstudent',
            unique_together={('class_name', 'roll')},
        ),
    ]