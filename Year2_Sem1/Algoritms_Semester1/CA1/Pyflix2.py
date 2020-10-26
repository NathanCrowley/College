class Movie:
    def __init__(self,title,director,castList,LenInMins):
        self.title = title
        self.director = director
        self.cast = castList
        self.len = LenInMins
        self.rating = -1                           #sets rating to -1 to show no user input.

    def __str__(self):
        return "Title: {}\nDirector: {}".format(self.title,self.director)
        #returns a short string of title and director

    def get_info(self):
        return "Title: {}\nDirector: {}\nCast: {}\nLength: {} minutes\nRating: {}".format(self.title,self.director,self.cast,self.len,self.rating)
        #returns a more detailed account  of all info for each movie

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
        return mov_list



    def add_movie(self,movie):
        new_node = Node(None,movie,None)            #create a node for the movie object to be added, it has no next or previous YET.
        new_node.prev = self.tail.prev              #sets the new nodes prev to point to the old last node
        new_node.next = self.tail                   #the new node next points to the tail
        self.tail.prev.next = new_node              #sets the tails previous node's next pointer to the new node
        self.tail.prev = new_node                   #sets tails previous pointer to  the next node
        self.size += 1                              #increment the size of DLL.


    def rate(self):
        if self.current != self.head:
            input_rating = float(input("Enter a rating for {}: >>>".format(self.current.data.title)))
            self.current.data.rating = input_rating
            return "You rated {} as: {}.".format(self.current.data.title,self.current.data.rating)
        else:
            return "Error no current movie selected."

    def get_current(self):
        return "Current: --> {}.\n".format(self.current.data)       #returns the current movies data

    def next_movie(self):
        self.current = self.current.next                            #increment the current movie
        if self.current == self.tail:                               #if you reach the tail(end of the DLL) loop back to start and begin again.
            self.current = self.head.next                           #set the current as the first node after the head to restart the loop.

    def prev_movie(self):
        self.current = self.current.prev
        if self.current == self.head:                               #if the current reaches the head, loop back around to the tail and continue
            self.current = self.tail.prev


    def remove_current(self):
        if self.current != self.head:
            curr = self.current
            curr.prev.next = curr.next
            curr.next.prev = curr.prev


    def reset(self):
        self.current = self.head                                    #reset the current to the head.

    def info(self):
        cur = self.current.data.get_info()
        return cur

    def length(self):
        return "Length of DLL: {}.".format(self.size)               #return the counter of the list size.


    def search(self,word):
        stored_current = self.current
        count = self.size
        word = word.lower()
        while count >= 0:
            if self.current != self.head:
                if word in self.current.data.title.lower():
                    return self.info()
                elif word in self.current.data.director.lower():
                    return self.info()
                elif word in self.current.data.cast.lower():
                    return self.info()
            self.next_movie()
            count -= 1
        self.current = stored_current
        return "No matching movie."

#------------------------------------------TESTING ----------------------------------
PyFlix_list = Pyflix()                                              #create a lsit

movie1 = Movie("El Camino", "Vince Gilligan", "Aaron Paul", 122)         #create 3 movie objects
movie2 = Movie("Joker", "Todd Phillips", "Joaquin Phoenix", 122)
movie3 = Movie("Midsommar", "An Aster", "Florence Pugh", 138)

PyFlix_list.add_movie(movie1)                                       #add them to the list
PyFlix_list.add_movie(movie2)
PyFlix_list.add_movie(movie3)

PyFlix_list.next_movie()
PyFlix_list.next_movie()
PyFlix_list.next_movie()
PyFlix_list.prev_movie()
PyFlix_list.next_movie()
#print(PyFlix_list.info())
#print("-"*100)

#print(PyFlix_list.search("Todd"))
#print("-"*100)

#print(PyFlix_list.get_current())
#PyFlix_list.rate()
#print(PyFlix_list.info())
print(PyFlix_list.length())
PyFlix_list.next_movie()
#print(PyFlix_list.get_current())
#print(PyFlix_list)
PyFlix_list.next_movie()
#print(PyFlix_list)
PyFlix_list.next_movie()
#print(PyFlix_list)
PyFlix_list.next_movie()
print(PyFlix_list)
print(PyFlix_list.info())