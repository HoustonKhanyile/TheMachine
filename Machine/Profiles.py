from itertools import count
from msilib.schema import Feature
from socket import SO_LINGER
from xml.dom.minidom import AttributeList

#commercial profile

class streams():
    def __init__(self, Artist, Artist_streams):
        self.artist = Artist
        self.Artist_streams = 'tidal' + 'spotify' + 'applemusic' + 'amazonmusic' + 'soundclound' + 'youtube'
        self.song = self.song_streams('D12', 'Fight music', 1550 + 500 + 500 + 500 + 500 + 500)

    def counting(self, Artist, Artist_streams):
            self.artist = Artist
            self.Artist_streams = 'tidal' + 'spotify' + 'applemusic' + 'amazonmusic' + 'soundclound' + 'youtube'
            count = Artist_streams * 5
            return Artist, count

    class song_streams():
        def __init__(self, Artist, Song, streams):
                self.artist = Artist
                self.song = Song
                self.streams = 'tidal' + 'spotify' + 'applemusic' + 'amazonmusic' + 'soundclound' + 'youtube'
            
        def counting2(self, Artist, Song, streams):
            self.artist = Artist
            self.song = Song
            self.streams = 'tidal' + 'spotify' + 'applemusic' + 'amazonmusic' + 'soundclound' + 'youtube'
            count = streams * 5
            return Artist, Song, count
    
s1 = streams.song_streams('D12', 'Fight music', 1550 + 500 + 500 + 500 + 500 + 500)
s2 = streams('Eminem', 1000000 + 500000 + 500000 + 500000 + 500000 + 500000)

print(s2.counting('Eminem', 1000000 + 500000 + 500000 + 500000 + 500000 + 500000))
print(s1.counting2('D12', 'Fight music', 1500 + 500 + 500 + 500 + 500 + 500))

#Audience profile

class publicity():
    def __init__(self, Blog, Feature):
        self.Blog = Blog
        self.Feature = Feature

    def Pub_count(self, Blog, Feature):
        self.Blog = 10
        self.Feature = 10
        Blog_Points = self.Blog * 69
        Feature_Points = self.Feature * 44
        Total_Points = Blog_Points + Feature_Points
        return Total_Points

    class engagements():
        def __init__(self, Likes, Retweets, Comments):
            self.Likes = Likes
            self.Retweet = Retweets
            self.Comments = Comments
            self.engage = self.engage_count(5000 + 10000 + 2000 + 20000, 200 + 180 + 2000 + 1000, 500)

        def engage_count(self, Likes, Comments, Retweets):
            self.Likes = 'twitter' + 'instagram' + 'tic tok' + 'facebook'
            self.Comments = 'instagram' + 'tic tok' + 'facebook' + 'twitter'
            self.Retweets = 'twitter'
            count = Likes, Comments, Retweets * 10
            return count

pub1 = publicity('Blog', 'Feature')
pub2 = publicity.engagements(5000 + 10000 + 2000 + 20000, 200 + 180 + 2000 + 1000 , 500)

print(pub1.Pub_count('Blog', 'Feature'))
print(pub2.engage_count(5000 + 10000 + 2000 + 20000, 200 + 180 + 2000 + 1000, 500))

#market profile

class appearence():

    def __init__(self, Performances, Interviews) -> None:
        self.Performance = Performances
        self.Interviews =  Interviews
    
    def appear(self, Performance, Interviews):
        self.Performance = 50
        self.Interviews = 50
        Performance_Points = self.Performance * 20
        Interviews_Points = self.Interviews * 8
        Total_Points = Performance_Points + Interviews_Points
        return Total_Points

app1 = appearence('Performance', 'Interviews')

print(app1.appear('Performance', 'Interviews'))


