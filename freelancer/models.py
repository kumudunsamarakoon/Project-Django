from django.db import models


class SalonOwner(models.Model):

    salon_fName = models.CharField(max_length=30)
    salon_lName = models.CharField(max_length=30)
    salon_address = models.CharField(max_length=200)
    salon_email = models.EmailField(max_length=80)
    salon_password = models.CharField(max_length=20)


class Stylist(models.Model):

    stylist_fName = models.CharField(max_length=30)
    stylist_lName = models.CharField(max_length=30)
    stylist_email = models.EmailField(max_length=80)
    stylist_password = models.CharField(max_length=20)
    stylist_DOB = models.DateField()
    stylist_rate = models.FloatField()
    stylist_proPic = models.ImageField(max_length=100)


class Booking(models.Model):

    salon_id = models.ForeignKey('SalonOwner', on_delete=models.CASCADE)
    Bid = models.ForeignKey('Stylist', on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_session = models.CharField(max_length=50)
    booking_confirm = models.NullBooleanField(null=False)
    booking_doDate = models.DateTimeField()


class Payment(models.Model):

    payment_bookId = models.ForeignKey('Booking', on_delete=models.CASCADE)
    payment_amount = models.FloatField()


class Rating(models.Model):

    rating_bookId = models.ForeignKey('Booking', on_delete=models.CASCADE)
    rating_value = models.IntegerField()
    rating_overall = models.FloatField()


class Schedule(models.Model):

    schedule_stylistId = models.ForeignKey('Stylist', on_delete=models.CASCADE)
    schedule_bookId = models.ForeignKey('Booking', on_delete=models.CASCADE)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    schedule_state = models.CharField(max_length=20)



