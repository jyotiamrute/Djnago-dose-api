# Generated by Django 4.0.6 on 2023-07-06 02:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('machine_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('machine_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=255)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.machine')),
            ],
        ),
        migrations.CreateModel(
            name='Dose',
            fields=[
                ('dose_id', models.AutoField(primary_key=True, serialize=False)),
                ('dose', models.FloatField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
    ]
