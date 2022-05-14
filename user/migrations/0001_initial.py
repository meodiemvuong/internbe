# Generated by Django 4.0.4 on 2022-05-13 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.employee')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.level')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
