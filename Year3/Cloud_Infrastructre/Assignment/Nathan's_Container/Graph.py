import matplotlib.pyplot as plt


def read_data_from_file(file):
    with open(file, "r") as textfile:
        contents = textfile.read().split()
        data = contents[5::]
        return data


'''read data in from the file - Careful it will be string format!
x-axis - values for x axis (0,10,20,30,40,...)
convert all elements to integers as they are strings when read in.
y-axis - values for y axis (0.0000,0.07323,0.4396,...)
plot the points
name the axis's
give graph a title
show the graph

'''
data = read_data_from_file("Execution_Times")
x = data[1::2]
# convert to ints
for i in range(0, len(x)):
    x[i] = int(x[i])
y = data[::2]
# convert all to floats
for j in range(0, len(y)):
    y[j] = float(y[j])
plt.plot(x, y)
plt.xlabel("Iterations")
plt.ylabel("Execution Time")
plt.title("Execution Time Graph")
plt.show()
