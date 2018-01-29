# Generated by Django 2.0.1 on 2018-01-29 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0009_persontoskills_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=70, verbose_name='Certifications')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToCert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CertID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Certifications')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Trainings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=70, verbose_name='Training')),
            ],
        ),
        migrations.AddField(
            model_name='persontotraining',
            name='TrainID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Trainings'),
        ),
    ]
