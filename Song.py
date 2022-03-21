"""
UMass ECE 241 - Advanced Programming
Project #1     Fall 2018
Song.py - Song class
Isaac Fitts-Sprague
ID: 29312728
Data: 10/23/18
"""


class Song:

    """
    Intial function for Song object. 
    parse a given songRecord string to song object.
    For an example songRecord such as "0,Qing Yi Shi,Leon Lai,203.38893,5237536"
    It contains attributes (ID, title, artist, duration, trackID)

    """

    #MAKE IT SO THIS CAN TAKE A STRING ALSO AND THEN DO THE TO SRING METHOD AND HAVE THIS CLASS WORK WITH THE BUILT IN TEST CASE FROM BELOW
    def __init__(self, listsongRecord):
        #inits all columns from the csv file as self variables
        self.id=listsongRecord[0]
        self.title=listsongRecord[1]
        self.artist=listsongRecord[2]
        self.duration=listsongRecord[3]
        self.trackid=listsongRecord[4]

    def getArtist(self):
        return self.artist


    def toString(self):
        return "Title: " + self.title + ";  Artist: " + self.artist


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':

    sampleSongRecord = "0,Qing Yi Shi,Leon Lai,203.38893,5237536"
    sampleSong = Song(sampleSongRecord)
    print(sampleSong.toString())