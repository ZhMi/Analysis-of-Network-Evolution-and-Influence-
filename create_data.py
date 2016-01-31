# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import csv
import random

# <codecell>

def writeFile(file_name,data_list):
    csvfile = file(file_name, 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['source','target','weight'])
    writer.writerows(data_list)
    csvfile.close()

# <codecell>

def createNode(node_num,node_min_value):
    node_list = []
    for i in xrange(node_num):
        node_list.append(i+node_min_value)
    return node_list

# <codecell>

def createNeighborSide(source_node_list,node_branch_num,weight):
    edge_list = []
    last_node_list = source_node_list[:]
    for i in xrange(len(last_node_list)): 
        last_node = last_node_list[i]
        next_node_branch_list = createNode(node_branch_num,min(last_node_list)+node_branch_num*i)
        new_edge_list = map(lambda x: (last_node,x,weight),next_node_branch_list)
        edge_list.append(new_edge_list)
    edge_list = sum(edge_list,[])
    return edge_list

# <codecell>

def craeteEdgeBasedNodes(source_node_list,branch_num,weight):
    edge_list = []
    random_list = []
    next_branch_node_list = []
    
    last_node_list = source_node_list[:]
    for i in xrange(len(last_node_list)):
        last_node  = last_node_list[i]
        next_branch_node_list = []
        
        for j in xrange(branch_num): 
            temp_num = random.randint(min(last_node_list), max(last_node_list))
            # print temp_num
            next_branch_node_list.append(temp_num)
                  
        # print "next_branch_node_list:",next_branch_node_list
        new_edge_list = map(lambda x: (last_node,x,weight),next_branch_node_list)
        # print "new_edge_list:",new_edge_list
        
        edge_list.append(new_edge_list)
    edge_list = sum(edge_list,[])
    return edge_list

# <codecell>

def createSameWeightOrNode(node_value,node_num):
    list = []
    for i in xrange(node_num):
        list.append(node_value)
    return list 

# <codecell>

def deleteRepeatedEdge(data_list):
    
    edge_list = data_list[:]
    func = lambda x,y:x if y in x or y[::-1] in x else x + [y]
    
    print "before delete repeated item:",len(edge_list)
    edge_list = reduce(func, [[], ] + edge_list)
    edge_list = filter(lambda x: x[0] != x[1],edge_list)
    print "after delete repeated item:",len(edge_list)
    return edge_list

# <codecell>

def deleteRepeatedNode(node_list):
    node_list_copy = node_list[:]
    func = lambda x,y:x if y in x else x + [y]
    node_list_copy = reduce(func, [[], ] + node_list_copy)
    return node_list_copy

# <codecell>

def findNeigborNode(source_node,total_edge_list):
    edge_list = filter(lambda x: x[0] == source_node,total_edge_list)
    return edge_list

# <codecell>

def calcuteSpeed(information_center,total_edge_list,cover_rate):
    temp_queue = []
    num = 0
    total_edge_num = len(total_edge_list)
    spread_node_num = int(cover_rate*total_edge_num)
    min_weight = 0
    edge_list = total_edge_list[:]
    #edge_list = map(lambda x: list(x),edge_list)
    #print "change type:",edge_list
    for i in xrange(len(information_center)):
        node_neighbor_edge_list = findNeigborNode(information_center[i],edge_list)
        temp_queue = temp_queue + node_neighbor_edge_list
        time = 0
    
    while num != spread_node_num or len(temp_queue)== 0:
        for j in xrange(len(temp_queue)):
            # print temp_queue 
            weight_list = map(lambda x: x[2],temp_queue)
            weight_list = filter(lambda x: x!=0,weight_list)
            # print "weigt_list:",weight_list
            min_weight = min(weight_list)
            # print "min weight:",min_weight
            min_weight_node = filter(lambda x: x[2] == min_weight ,temp_queue)[0:1]
            time = time + min_weight_node[0][2]
            print "j:",j
            print "time:",time

            temp_queue = map(lambda x : (x[0],x[1],x[2]-min_weight),temp_queue)
            need_delete_edge = filter(lambda x: x[2] == 0,temp_queue)
            print "need_delete_edge:",need_delete_edge

            temp_queue = filter(lambda x: x[2] != 0,temp_queue)
            edge_list = filter(lambda x: x[2] != 0,edge_list)

            print "temp_queue:",temp_queue
            edge_queue = [ i for i in edge_list if i not in need_delete_edge]
            
            num = num + len(need_delete_edge) 
            
            # print "i:temp_queue:",i,temp_queue
            
            # + neighbor
            for k in xrange(len(need_delete_edge)):
                temp_queue = temp_queue + findNeigborNode(need_delete_edge[k][0],edge_list)
        
    return time
        

# <codecell>

# create centralized network 

center_node = [0]
first_node_list = createNode(30,1)

# [test part]
print "first node list value:",first_node_list
print "length of first node list:",len(first_node_list)

# add weight for the first lever edge
first_edge_list = createNeighborSide(center_node,30,5)
second_edge_list = createNeighborSide(first_node_list,3,10)

print "first edge list:",first_edge_list

print "second_edge_list value:",second_edge_list
print "second edge_list length:",len(second_edge_list)

second_node_list = map(lambda x: x[0],second_edge_list)
second_node_list = deleteRepeatedNode(second_node_list)
print "second_node_list:",second_node_list

center_network_list = []
center_network_list = first_edge_list + second_edge_list
print "length of center_network_list:",len(center_network_list)

center_network_list = deleteRepeatedEdge(center_network_list)

writeFile("center_network",center_network_list)

# <codecell>

# create decentralized network data
source_list = second_node_list[:]
add_edge_list = craeteEdgeBasedNodes(source_list,3,5)

print "add edge list:",add_edge_list
add_edge_list = deleteRepeatedEdge(add_edge_list)

decentrail_network_data = add_edge_list + second_edge_list
print "decentrail_network_data:",decentrail_network_data
writeFile("decentrail_network",decentrail_network_data)
print "length of decentrail network:",len(decentrail_network_data)

# <codecell>

# create Distributer network
node_list = createNode(30,1)
distributed_network_data = craeteEdgeBasedNodes(node_list,8,10)
writeFile("distributed_network",distributed_network_data)

# <codecell>

# calcute speed of centralized network

information_center = [0]
speed = calcuteSpeed(information_center,center_network_list,0.97)
print speed

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>

list = [[(1,2)],[3,4]]
sum(list,[])

# <codecell>


# <codecell>


