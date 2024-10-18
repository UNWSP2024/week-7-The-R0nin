# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
rounds = 0
x_list = []
y_list = []
z_list = []

while rounds < 2: 
    x = int(input('x-coordinate: '))
    y = int(input('y-coordinate: '))
    z = int(input('z-coordinate: '))
    
    x_list.append(x)
    y_list.append(y)
    z_list.append(z)
    rounds += 1

coordinate_plane1 = [x_list[0],y_list[0],z_list[0]]
coordinate_plane2 = [x_list[1], y_list[1], z_list[1]]
print(coordinate_plane1, coordinate_plane2)
# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
def coordinate_distance(cod1, cod2):
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 
    distance = (x_list[1]-x_list[0])^2 + (y_list[1]-y_list[0])^2 + (z_list[1]-z_list[0])^2
    print("the distance between the points is: ", distance)
coordinate_distance(coordinate_plane1, coordinate_plane2)
