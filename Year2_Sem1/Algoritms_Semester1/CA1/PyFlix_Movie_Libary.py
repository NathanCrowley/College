class Movie:
    def __init__(self,title,director,castList,LenInMins):
        self.__title = title
        self.__director = director
        self.__cast = castList
        self.__len = LenInMins
        self.__rating = -1                  #sets rating to -1 to show no user input.

    def __str__(self):
        return "Title: {}\nDirector: {}".format(self.__title,self.__director)
        #returns a short string of title and director

    def get_info(self):
        return "Title: {}\nDirector: {}\nCast: {}\nLength: {} minutes".format(self.__title,self.__director,self.__cast,self.__len)
        #returns a more detailed account  of all info for each movie

    #RATING---------------------------------------------

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None                    #initialise these to none
        self.prev = None


class Pyflix:
    def __init__(self):
        self.head = None

    def __str__(self):
        m_list = ''                         #create an empty string to act as a list
        for movie in self.data:             #iterate through the list for all movies
            movie = str(movie) + "\n"       #make movie a string and have a newline after each piece of info
            m_list += movie + "\n"          #have a newline between each movie
        return m_list

    def add_movies(self,movie):
        if self.head == None:               #if the DLL is empty
            new_node = Node(movie)          #create a node object
            new_node.prev = None            #make it the first node  by saying before it is null.
            self.head = new_node
        else:
            new_node = Node(movie)
            current = self.head
            while current.next != None:     #keep going until you reach the Null at the end
                current = current.next
            current.next = new_node         #make the next node of the node before null the new node
            new_node.prev = current         #make the previous point back to the old last node
            new_node.next = None            #have the new node pointing to a null to indicate it is the new last node


    def get_current(self):
        current = self.head
        return  "The current movie is --> {}.".format(current.data)

    def next_movie(self):
        cur = self.get_current()
        if cur.next == None:
            print("{} is the final movie.".format(cur.data))




    def print_list(self):
        cur = self.head
        print("List of movies:")
        index = 1
        while cur:
            print("{}. {}\n".format(index,cur.data))
            cur = cur.next
            index += 1




    def prev_movie(self):
        pass

    def reset(self):
        pass

    def rate(self):
        pass

    def info(self):
        pass

    def remove_current(self):
        cur = self.get_current()
        del cur



    def length(self):
        length = 0                          #initialise length counter to 0
        current = self.head                 #start at the first node
        while current != None:              #continue until you reach the final node
            length += 1                     #increment the counter
            current = current.next          #increment the nodes.
        return "The length is: {}.".format(length)

#----------------------------Movie Instances-------------------------------------------
movie1 = Movie("Taxi Driver", "Martin Scorsese","Robert De Niro, Jodie Foster, Harvey Keitel", 114)
movie2 = Movie("Joker","Todd Philips", "Joaquin Phoenix", 122)
movie3 = Movie("Bee Movie", "Simon J.Smith", "Jerry Seinfield", 91)
movie4 = Movie("The Shinning","Stanley Kubrick","Jack Nickolson",113)
#-------------------------------------------------------------------------------------

if __name__ == "__main__":
    '''
    print(movie1)           #uses the '__str__' method.
    print("------------------------------------------------")
    print(movie1.get_info())
    '''

    #x = Pyflix([movie1,movie2,movie3,movie4])
    '''print(x)'''
    x = Pyflix()

    x.add_movies(movie1)
    x.add_movies(movie2)
    x.add_movies(movie3)

    x.print_list()
    print("-"*10)
    print(x.get_current())
    x.next_movie()
    print(x.get_current())
    '''DONT FORGET TO GET __str__ to work NOT .print_list'''
    #x.print_list()
    #print(x.get_current())
    #print(x.length()))

    #print("-------------------------------")
    #print(x.get_current())
    #x.next_movie()
    #print(x.get_current())