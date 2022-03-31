from pyexpat import model
from sqlite3 import Date, Timestamp
from django.db import models
from numpy import mod
from phonenumber_field.modelfields import PhoneNumberField

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


#MARKET PROFILE

class Appear(models.Model):
    Show = models.CharField(max_length=100)
    Media = models.CharField(max_length=30, blank=True, null=True, choices=Media_Choices)
    Date = models.DateField(auto_now=False, auto_now_add=False)
    Time = models.TimeField(auto_now=False, auto_now_add=False)
    Episode = models.IntegerField()
    Producer = models.CharField(max_length=100)
    Producer_Email = models.EmailField(max_length=254)

    def __str__(self):
        return self.Show + ' ' + self.Producer_Email

class Performance(models.Model):
    Event = models.CharField(max_length=100)
    Date = models.DateField(auto_now=False, auto_now_add=False)
    Start_Time = models.TimeField(auto_now=False, auto_now_add=False)
    Time_Slot = models.TimeField(auto_now=False, auto_now_add=False)
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Venue = models.CharField(max_length=100)

    def __str__(self):
        return self.Event + ' ' + self.Venue

#AUDIENCE PROFILE

class Twitter(models.Model):
    Tweet = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    Timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    Replys = models.IntegerField()
    Retweets = models.IntegerField()
    Likes = models.IntegerField()

    def __str__(self):
        return self.Tweet + ' ' + self.Likes

class Instagram(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    caption = models.TextField()
    Timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    comments = models.BigIntegerField()
    Likes = models.BigIntegerField()

    def __str__(self):
            return self.content + ' ' + self.Likes

class Tic_Tok(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    caption = models.TextField()
    Timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    comments = models.BigIntegerField()
    Likes = models.BigIntegerField()

    def __str__(self):
            return self.content + ' ' + self.Likes

class Facebook(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    caption = models.TextField()
    Timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    Comments = models. BigIntegerField()
    Likes = models.BigIntegerField()

    def __str__(self):
            return self.content + ' ' + self.Likes

class Publicity(models.Model):
    Name = models.CharField(max_length=100)
    Media = models.CharField(max_length=30, blank=True, null=True, choices=Media_Types)
    Country = models.CharField(max_length=100)
    Date = models.DateField(auto_now=False, auto_now_add=False)
    Link = models.URLField(max_length=200)

    def __str__(self):
        return self.Name + ' ' + self.Link

#COMMERCIAL PROFILE

class Spotify(models.Model):
    Artist = models.CharField(max_length=100)
    Song = models.CharField(max_length=100)
    Duration = models.DurationField()
    Plays = models.BigIntegerField()

    def __str__(self):
        return self.Artist + ' ' + self.Plays

class Apple_music(models.Model):
    Artist = models.CharField(max_length=100)
    Song = models.CharField(max_length=100)
    Duration = models.DurationField()
    Plays = models.BigIntegerField()

    def __str__(self):
        return self.Artist + ' ' + self.Plays

class Soundcloud(models.Model):
    Artist = models.CharField(max_length=100)
    Song = models.CharField(max_length=100)
    Duration = models.DurationField()
    Plays = models.BigIntegerField()

    def __str__(self):
        return self.Artist + ' ' + self.Plays

class Youtube_music(models.Model):
    Artist = models.CharField(max_length=100)
    Song = models.CharField(max_length=100)
    Duration = models.DurationField()
    Plays = models.BigIntegerField()

    def __str__(self):
        return self.Artist + ' ' + self.Plays

class TIDAL(models.Model):
    Artist = models.CharField(max_length=100)
    Song = models.CharField(max_length=100)
    Duration = models.DurationField()
    Plays = models.BigIntegerField()

    def __str__(self):
        return self.Artist + ' ' + self.Plays

class Deezer(models.Model):
    Artist = models.CharField(max_length=100)
    Song = models.CharField(max_length=100)
    Duration = models.DurationField()
    Plays = models.BigIntegerField()

    def __str__(self):
        return self.Artist + ' ' + self.Plays

class Amazon_Music(models.Model):
    Artist = models.CharField(max_length=100)
    Song = models.CharField(max_length=100)
    Duration = models.DurationField()
    Plays = models.BigIntegerField()

    def __str__(self):
        return self.Artist + ' ' + self.Plays

class Youtube(models.Model):
    Artist = models.CharField(max_length=100)
    Song = models.CharField(max_length=100)
    Duration = models.DurationField()
    Plays = models.BigIntegerField()

    def __str__(self):
        return self.Artist + ' ' + self.Plays

#ARTIST BOOKING

class Bookings(models.Model):
    Artist = models.CharField(max_length=100)
    Event = models.CharField(max_length=100, blank=True, null=True, choices=Event_Types)
    Name_of_Event = models.CharField(max_length=100)
    Date = models.DateField(auto_now=False, auto_now_add=False)
    Time_Slot = models.TimeField(auto_now=False, auto_now_add=False)
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Venue = models.CharField(max_length=100)
    Promoter = models.CharField(max_length=100)
    Promoter_Email = models.EmailField(max_length=100)

    def __str__(self):
        return self.Artist + ' ' + self.Promoter_Email

#ARTIST BIO

class Profile(models.Model):
    Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Stage_Name = models.CharField(max_length=100)
    Phone_number = PhoneNumberField()
    Address_Line_1 = models.CharField(max_length=300)
    Address_Line_2 = models.CharField(max_length=300)
    Postcode = models.IntegerField()
    State = models.CharField(max_length=100)
    Area = models.IntegerField()
    Email = models.EmailField(max_length=254)
    Country = models.CharField(max_length=300)
    State_Region = models.CharField(max_length=100)

    def __str__(self):
        return self.Name + ' ' + self.State_Region

class Profile2(models.Model):
    Spotify = models.URLField(max_length=200)
    Apple_music = models.URLField(max_length=200)
    Soundcloud = models.URLField(max_length=200)
    Tidal = models.URLField(max_length=200)
    Deezer = models.URLField(max_length=200)
    Amazon_Music = models.URLField(max_length=200)
    Youtube_music = models.URLField(max_length=200)
    Youtube = models.URLField(max_length=200)
    Twitter = models.URLField(max_length=200)
    Instagram = models.URLField(max_length=200)
    Tic_Tok = models.URLField(max_length=200)
    Facebook = models.URLField(max_length=200)

    def __str__(self):
        return self.Spotify + ' ' + self.Facebook





    