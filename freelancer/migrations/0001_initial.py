# Generated by Django 2.1.3 on 2018-11-23 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('booking_session', models.CharField(max_length=50)),
                ('booking_confirm', models.NullBooleanField()),
                ('booking_doDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.FloatField()),
                ('payment_bookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancer.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_value', models.IntegerField()),
                ('rating_overall', models.FloatField()),
                ('rating_bookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancer.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='SalonOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salon_fName', models.CharField(max_length=30)),
                ('salon_lName', models.CharField(max_length=30)),
                ('salon_address', models.CharField(max_length=200)),
                ('salon_email', models.EmailField(max_length=80)),
                ('salon_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_date', models.DateField()),
                ('schedule_time', models.TimeField()),
                ('schedule_state', models.CharField(max_length=20)),
                ('schedule_bookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancer.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='Stylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stylist_fName', models.CharField(max_length=30)),
                ('stylist_lName', models.CharField(max_length=30)),
                ('stylist_email', models.EmailField(max_length=80)),
                ('stylist_password', models.CharField(max_length=20)),
                ('stylist_DOB', models.DateField()),
                ('stylist_rate', models.FloatField()),
                ('stylist_proPic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='schedule_stylistId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancer.Stylist'),
        ),
        migrations.AddField(
            model_name='booking',
            name='Bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancer.Stylist'),
        ),
        migrations.AddField(
            model_name='booking',
            name='salon_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancer.SalonOwner'),
        ),
    ]
