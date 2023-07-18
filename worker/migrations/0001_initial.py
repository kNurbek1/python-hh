# Generated by Django 4.2.2 on 2023-07-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=255)),
                ('waiting_salary', models.IntegerField(blank=True, null=True)),
                ('is_searching', models.BooleanField(default=True)),
            ],
        ),
    ]