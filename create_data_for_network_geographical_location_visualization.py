import random
import math
import csv

x_list = []
y_list = []

x1_list = []
y1_list = []

def writeFile(file_name,data_list):
    csvfile = file(file_name, 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['x','y'])
    writer.writerows(data_list)
    csvfile.close()

def getDistance(x,y,x1,y1):
    distance = math.sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))
    return distance

num = 0
while num != 50:
    temp_x = random.randint(-7200,7200)
    temp_y = random.randint(-7200,7200)
    if getDistance(temp_x,temp_y,0,0) <= 7200:
        x_list.append(temp_x)
        y_list.append(temp_y)
        num = num + 1

R_list = map(None,x_list,y_list)
R_list = map(lambda x: list(x),R_list)

second_node_num = 0
for i in xrange(50):
    second_node_num = 0
    while second_node_num != 50:
        temp_center_x = x_list[i]
        temp_center_y = y_list[i]
        temp_x1 = random.randint(temp_center_x-1800,temp_center_x+1800)
        temp_y1 = random.randint(temp_center_y-1800,temp_center_y+1800)
        if getDistance(temp_center_x,temp_center_y,temp_x1,temp_y1) <= 1800:
            x1_list.append(temp_x1)
            y1_list.append(temp_y1)
            second_node_num = second_node_num + 1

r_list = map(None,x1_list,y1_list)
r_list = map(lambda x: list(x),r_list)

writeFile('picture_of_center_points.csv',[[0,0]])
writeFile('picture_of_first_edge_points.csv',R_list)
writeFile('picture_of_second_edge_points.csv',r_list)



