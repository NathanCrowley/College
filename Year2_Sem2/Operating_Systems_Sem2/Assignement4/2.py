import os
pid = os.fork()
print(pid)
if pid == 0:    #is the child
    print("This is the child.")
elif pid > 0:   #is parent
    print("The child is pid {}.".format(pid))
else:
    print("An error occurred.")