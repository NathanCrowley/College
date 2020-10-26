'''
Nathan Crowley - 118429092
'''


class Movie:
    def __init__(self,title,director,castList,LenInMins):
        self.title = title
        self.director = director
        self.cast = castList
        self.len = LenInMins
        self.rating = -1                           #sets rating to -1 to show no user input.

    def __str__(self):                              #returns a short string of title and director
        return "Title: {}\nDirector: {}\n".format(self.title,self.director)


    def get_info(self):                             #returns a more detailed account  of all info for each movie
        return "Title: {}\nDirector: {}\nCast: {}\nLength: {} minutes\nRating: {}\n".format(self.title,self.director,self.cast,self.len,self.rating)


class Node:
    def __init__(self,previous,data,next_n):
        self.prev = previous                        #nodes previous pointer
        self.data = data                            #nodes data
        self.next = next_n                          #nodes next pointer

class Pyflix:
    def __init__(self):
        self.head = Node(None,None,None)            #head is a node with no previous no data and no next(no next can be changed)
        self.tail = Node(self.head,None,None)       #Tail is a node with head as its pointer to start(can be changed) no data and no next.
       # self.head.prev = self.tail                 #the heads previous
        self.size = 0                               #size counter
        self.current = self.head                    #initialises the current to the head
        self.rating = -1                            #initialise rating to -1 to show no rating given

    def __str__(self):
        mov_list = ''                               #create and empty list to later score your movies
        node = self.head.next                       #set a node to the heads next node (aka first node)
        while node.next:                            #keep looping until you reach the last node
            movie = str(node.data) + "\n"           #set a variable called 'movie' to the string of the movie's data and concatinate a \n to seperate by a new line
            if node == self.current:
                movie = "--> " + movie
            mov_list += movie +"\n"                 #since movie is a string representation we can add it to the 'm' list
            node = node.next                        #move onto next node
        return "DLList --->{}".format(mov_list)



    def add_movie(self,movie):
        new_node = Node(None,movie,None)            #create a node for the movie object to be added, it has no next or previous YET.
        new_node.prev = self.tail.prev              #sets the new nodes prev to point to the old last node
        new_node.next = self.tail                   #the new node next points to the tail
        self.tail.prev.next = new_node              #sets the tails previous node's next pointer to the new node
        self.tail.prev = new_node                   #sets tails previous pointer to  the next node
        self.size += 1                              #increment the size of DLL.

    def get_current(self):
        return "Current: --> {}\n".format(self.current.data)       #returns the current movies data

    def next_movie(self):
        self.current = self.current.next                            #increment the current movie
        if self.current == self.tail:                               #if you reach the tail(end of the DLL) loop back to start and begin again.
            self.current = self.head.next                           #set the current as the first node after the head to restart the loop.

    def prev_movie(self):
        self.current = self.current.prev
        if self.current == self.head:                               #if the current reaches the head, loop back around to the tail and continue
            self.current = self.tail.prev

    def reset(self):
        self.current = self.head                                    #reset the current to the head.

    def rate(self):
        if self.current != self.head:
            input_rating = float(input("Enter a rating for {}: >>>".format(self.current.data.title)))
            self.current.data.rating = input_rating
            return "You rated {} as: {}\n".format(self.current.data.title,self.current.data.rating)
        else:
            return "Error no current movie selected.\n"

    def info(self):
        cur = self.current.data.get_info()                          #current get the info of the current movie
        return cur

    def remove_current(self):
        if self.current != self.head:                               #if the current isnt the head
            curr = self.current                                     #set a curr variable as the current
            curr.prev.next = curr.next                              #set the currents previous node' next pointer to the next node
            curr.next.prev = curr.prev                              #set the currents next node's previous pointer to the previous node
            self.size -= 1                                          #decrement the size of the list
            PyFlix_list.next_movie()                                #move current to the next node

    def length(self):
        if self.size >=0:
            return "Length of DLL: {}\n".format(self.size)          #return the counter of the list size.
        else:
            return "Length of DLL: {}\n".format(0)                  #return 0


    def search(self,word):
        stored_cur = self.current                                       #store original current movie incase no match found.
        new_cur = self.head.next                                        #set the new current as the first movie in the list
        self.current = new_cur                                          #the current is now the first movie
        word = word.lower()                                             #make the word input all lower case
        count = self.size                                               #count is set as the number of movies in the DLL
        if len(word) <= 0:                                              #if th4 length of the input is 0 then print error message
            return "No matching movie."
        while count > 0:                                                #while count is greater than 0.
            movie_info = self.current.data                              #set a variable to the data in the current node
            if word in movie_info.title.lower():                        #if the word we are searching for is in the title
                return self.info()                                      #return the movie
            elif word in movie_info.director.lower():                   #if the word is in the director string
                return self.info()                                      #return the movie
            elif word in movie_info.cast.lower():                       #if the word is in the cast string
                return self.info()                                      #return the movie
            PyFlix_list.next_movie()                                    #move current to the next mvoie
            count -= 1                                                  #decrement your counter
        return "No matching movie."                                     #if the word is never found print error message

#------------------------------------------TESTING ----------------------------------
#(i)
PyFlix_list = Pyflix()                                                  #create a lsit

#(ii)--> (iv)
movie1 = Movie("El Camino", "Vince Gilligan", "Aaron Paul", 122)        #create 3 movie objects
movie2 = Movie("Joker", "Todd Phillips", "Joaquin Phoenix", 122)
movie3 = Movie("Midsommar", "An Aster", "Florence Pugh", 138)

PyFlix_list.add_movie(movie1)                                            #add them to the list
PyFlix_list.add_movie(movie2)
PyFlix_list.add_movie(movie3)

#(v)
print(PyFlix_list)                                                      #display the list to the screen (uses the __str__ method)

#(vi)
PyFlix_list.next_movie()                                                 #set current as the next movie(El camino)
print(PyFlix_list)

#(vii)
print(PyFlix_list.info())                                               #display the info for current movie.

#(viii)
PyFlix_list.next_movie()                                                #move current movie to next movie(Joker)
print(PyFlix_list)

#(ix)
print(PyFlix_list.get_current())                                        #report current movie

#(x)
PyFlix_list.rate()                                                       #rate the current movie
print(PyFlix_list.info())

#(xi)
print(PyFlix_list.get_current())                                        #current = Joker
PyFlix_list.prev_movie()                                                #change currenet to
print(PyFlix_list.get_current())                                        #now current = El Camino

#(xii)
PyFlix_list.remove_current()                                            #remove the current movie (El Camino), sets current movie to the previous

#(xiii)
print(PyFlix_list)                                                      #now list has only two movies

#(xiv)
print(PyFlix_list.info())                                               #current is now the previous of the movie you removed

#(xv)
movie4 = Movie("Hustlers", "Lorene Scafaria", "Constance Wu, Jennifer Lopez", 110)
PyFlix_list.add_movie(movie4)

#(xvi)
PyFlix_list.next_movie()

#(xvii)
PyFlix_list.next_movie()

#(xviii)
print(PyFlix_list.info())

#(xix)
print(PyFlix_list)

#(xx)
print(PyFlix_list.search("joker"))


