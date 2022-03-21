"""
UMass ECE 241 - Advanced Programming
Project #1     Fall 2018
SongLibrary.py - SongLibrary class
Isaac Fitts-Sprague
ID: 29312728
Date: 10/23/18
"""

from Song import Song
import random
import time
import csv


# this class is used when building and searching the balanced BST
class BSTNode:
    def __init__(self, currentsongobj,parent=None):
        if currentsongobj == None:
            return
        else:
            #the key is the song title
            self.key = currentsongobj.title
            self.payload = currentsongobj
            self.leftChild = None
            self.rightChild = None
            self.parent=parent


class SongLibrary:
    """
    Intialize your Song library here.
    You can initialize an empty songArray, empty BST and
    other attributes such as size and whether the array is sorted or not
    """

    def __init__(self):
        self.songArray = list()
        self.songBST = None
        self.isSorted = False
        self.size = 0
        self.linearfound = 0

        # Balanced BST init
        self.BSTfound = None  # for the balanced BST search
        self.root = None
        self.startedBST=0
        self.bstbuilt=False

    """
    load your Song library from a given file. 
    It takes an inputFilename and store the songs in songArray
    """

    def loadLibrary(self, inputFilename):
        tempfile = open(inputFilename)
        csv_tempfile = csv.reader(tempfile)

        for file in csv_tempfile:
            self.songArray.append(Song(file))
        self.size = len(self.songArray)

    def linearSearch(self, query, attribute):
        """
        Linear search function.
        It takes a query string and attibute name (can be 'title' or 'artist')
        and return the number of songs found in the library.
        Return -1 if no songs is found.
        Note that, Each song name is unique in the database,
        but each artist can have several songs.
        """
        self.linearfound = 0

        # if we are searching for a artist
        if attribute == "artist":
            # iterate over the length of the songArray
            for currentsong in self.songArray:
                # if the current song matches the query
                if currentsong.artist == query:
                    self.linearfound += 1

        # if we are searching for a title
        if attribute == "title":
            # iterate over the length of the songArray
            for currentsong in self.songArray:
                # if the current song matches the query
                if currentsong.title == query:
                    self.linearfound += 1

        return self.linearfound

    """
    Build a BST from your Song library based on the song title. 
    Store the BST in songBST variable
    """

    def buildBST(self):
        # if the song array is not already alphabetically sorted by song title this calls the quick sort function to
        # sort it
        if self.isSorted == False:
            self.quickSort()
        self._buildBST(self.songArray,None)
        self.songBST = BSTNode(None)
        self.songBST.root = self.root
        self.bstbuilt=True

    # recursive private function that makes a balanced BST from the pre ordered song library
    # CHECK HOW MANY ELEMENTS IN THE BALANCED BST
    def _buildBST(self, buildarray,parent):

        #breaks the recursive call
        if len(buildarray) == 0:
            return

        #calculates the middle index of the ordered list
        middleindex = len(buildarray) // 2

        #creates a root node from the middle list song
        recursiveroot = BSTNode(buildarray[middleindex], parent=parent)

        #recersivly calls this function for the lists on the left and right side of the middle index value
        recursiveroot.leftChild = self._buildBST(buildarray[:middleindex],recursiveroot)
        recursiveroot.rightChild = self._buildBST(buildarray[middleindex + 1:],recursiveroot)

        self.songBST = recursiveroot
        self.root = recursiveroot
        return recursiveroot

    # function to get the max height of the balanced BST
    # this function was helpful when checking my work
    def BSTGetHeight(self):
        self.height = self._BSTGetHeight(self.songBST.root)
        return self.height

    # private recursive function to be called to get the max height of the balanced BST
    def _BSTGetHeight(self, node):
        # if the node passed in has a left and right Child then it recursivly calls each sub tree to find the one
        # with the greatest height
        if node.leftChild and node.rightChild:
            return max(self._BSTGetHeight(node.leftChild), self._BSTGetHeight(node.leftChild)) + 1
        # if the current node only has a right Child
        if node.rightChild:
            return self._BSTGetHeight(node.rightChild) + 1
        # if the current node only has a left Child
        if node.leftChild:
            return self._BSTGetHeight(node.leftChild) + 1
        # if the current node has no Children then it is a leaf node so 1 is returned
        else:
            return 1

    """
    Implement a search function for a query song (title) in the songBST.
    Return the song information string
    (After you find the song object, call the toString function)
    or None if no such song is found.
    """
    #this searchBST function calls teh private _searchBST function to recursivly search for the deisred song
    def searchBST(self, query):
        #if the bst is not already built this calls the builder function
        if self.bstbuilt == False:
            self.buildBST()

        self.BSTfound = None
        return self._searchBST(query, self.root)

    # recursive private function that searches the BST for the query variable in a songs title
    def _searchBST(self, query, curnode):

        # breaks the recursion if there is no current node
        if curnode == None:
            return self.BSTfound

        # if the current node has the song we are looking for
        # saves the song object using the toString function from the Song class
        elif curnode.key == query:
            self.BSTfound = curnode.payload.toString()
            return self.BSTfound

        # if the curent node title comes before the query in the alphabet
        # then the right Child is recursivly searched
        elif curnode.key < query:
            # calls the search function on the left Child
            return self._searchBST(query, curnode.rightChild)

        # if the current node title comes after the query in the alphabet
        # then the left Child is recursivly searched
        elif curnode.key > query:
            # calls the search function on the right Child
            return self._searchBST(query, curnode.leftChild)

        #    """

    #    Return song libary information
    #    """
    def libraryInfo(self):
        return "Size: " + str(self.size) + ";  isSorted: " + str(self.isSorted)

    def quickSort(self):
        """
        Sort the songArray using QuickSort algorithm based on the song title.
        The sorted array should be stored in the same songArray.
        Remember to change the isSorted variable after sorted
        """
        # calls the recursive quickSortHelper function to do the sorting
        self.quickSortHelperFunction(0, self.size - 1)

        # once the sorting is over isSorted is set to true
        self.isSorted = True

    def quickSortHelperFunction(self, first, last):
        if first < last:
            # calls the splitpoint method to generate a splitpoint
            splitpoint = self.splitter(first, last)

            # calls the quicksort method on the left then right half
            self.quickSortHelperFunction(first, splitpoint - 1)
            self.quickSortHelperFunction(splitpoint + 1, last)

    def splitter(self, first, last):

        # sets the pivotvalue as the first element in the array
        pivotvalue = self.songArray[first].title

        leftindex = first + 1
        rightindex = last
        done = False

        # while not sorted
        while not done:

            # while the left index < right index AND the song title at songArray[leftindex] comes before the pivot value in the alphabet
            while leftindex <= rightindex and str(self.songArray[leftindex].title) < str(pivotvalue):
                leftindex += 1

            # while right index > left index AND the song title at songArray[rightindex] comes after the pivot value in the alphabet
            while rightindex >= leftindex and str(self.songArray[rightindex].title) > str(pivotvalue):
                rightindex -= 1

            if rightindex < leftindex:
                done = True
            # if the right index>left index
            else:
                # swap the values at the right and left index
                temp = self.songArray[leftindex]
                self.songArray[leftindex] = self.songArray[rightindex]
                self.songArray[rightindex] = temp

        temp = self.songArray[first]
        self.songArray[first] = self.songArray[rightindex]
        self.songArray[rightindex] = temp

        return rightindex


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    songLib = SongLibrary()
    songLib.loadLibrary("TenKsongs.csv")
    print(songLib.libraryInfo())
    print(songLib.songArray[0].toString())
    print(songLib.songArray[1].toString())
    print(songLib.songArray[2].toString())
    print(songLib.songArray[3].toString())


    print(songLib.searchBST("Thriller"))