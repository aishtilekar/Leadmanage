# Generated by Django 4.1.7 on 2023-06-07 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0004_student_comments_student_follow_up1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lead.student')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]