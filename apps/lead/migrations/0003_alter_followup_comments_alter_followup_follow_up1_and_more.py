# Generated by Django 4.1.7 on 2023-06-01 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0002_student_followup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='comments',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='follow_up1',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='follow_up2',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='follow_up3',
            field=models.DateField(null=True),
        ),
    ]