from django.db import models


Media_Choices = (
        ("TV", "TV"),
        ("Radio", "Radio"),
        ("Youtube", "Youtube"),
        ("Podcast", "Podcast"),
    )

Media_Types = (
    ('Social Media', 'Social Media'),
    ('Magazine', 'Magazine'),
    ('Online Mag', 'Online Mag'),
)

Event_Types = (
    ('Festival', 'Festival'),
    ('Mini Tour', 'Mini Tour'),
    ('Corporate Event', 'Corporate Event'),
    ('Club Performance', 'Club Performance'),
    ('Paid Appearence', 'Paid Appearence')
)

class Appear(models.Model):
    Show = models.CharField(max_length=100)
    Media = models.CharField(max_length=30, blank=True, null=True, choices=Media_Choices)
    Episode = models.IntegerField()
    Date = models.DateField(max_length=100)
    Time = models.TimeField(auto_now=False, auto_now_add=False)
    Producer = models.CharField(max_length=100)
    Producer_Email = models.EmailField(max_length=254)

    def __str__(self):
        return self.Show + ' ' + self.Producer_Email

class Performance(models.Model):
    Event = models.CharField(max_length=100)
    Date = models.DateField(max_length=100)
    Start_Time = models.TimeField(auto_now=False, auto_now_add=False)
    Time_Slot = models.TimeField(auto_now=False, auto_now_add=False)
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Venue = models.CharField(max_length=100)

    def __str__(self):
        return self.Event + ' ' + self.Venue

class Publicity(models.Model):
    Name = models.CharField(max_length=100)
    Media = models.CharField(max_length=30, blank=True, null=True, choices=Media_Types)
    Country = models.CharField(max_length=100)
    Date = models.DateTimeField(max_length=100)
    Link = models.URLField(max_length=200)

    def __str__(self):
        return self.Name + ' ' + self.Link

class Bookings(models.Model):
    Artist = models.CharField(max_length=100)
    Event = models.CharField(max_length=100, blank=True, null=True, choices=Event_Types)
    Name_of_Event = models.CharField(max_length=100)
    Date = models.DateField(max_length=100)
    Time_Slot = models.TimeField()
    Set_Time = models.IntegerField()
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Venue = models.CharField(max_length=100)
    Promoter = models.CharField(max_length=100)
    Promoter_Email = models.EmailField(max_length=100)

    def __str__(self):
        return self.Artist + ' ' + self.Promoter_Email

class Profile(models.Model):
    Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Address_Line_1 = models.CharField(max_length=300)
    Address_Line_2 = models.CharField(max_length=300)
    Postcode = models.IntegerField()
    State = models.CharField(max_length=100)
    Area = models.IntegerField()
    Email = models.EmailField()
    Country = models.CharField(max_length=300)
    State_Region = models.CharField(max_length=100)

    def __str__(self):
        return self.Name + ' ' + self.State_Region





    