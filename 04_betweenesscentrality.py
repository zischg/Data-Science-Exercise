#script for analysing betweenness centrality in the road network of the Canton of ZH
import numpy as np
import pandas as pd
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt


#general workspace settings
myworkspace="/Users/esthergerber/Desktop/Uni_Bern/Data Science and complex Network/4.12.20_Exercise"

#input data: the csv file for nodes and edges
nodesfile=myworkspace+"/zh_nodes/zh_nodes.shp"
edgesfile=myworkspace+"/zh_roads/zh_roads.shp"
#input data: the roads file
nodesgdf = gpd.read_file(nodesfile)
edgesgdf = gpd.read_file(edgesfile)

#output data: the nodes distances file
nodesbetweennesscentralityfile=open(myworkspace+"/betweennesscentrality_normalsituation.csv","w")
nodesbetweennesscentralityfile.write("nodeid"+";"+"betweennesscentrality"+"\n")  # header of the file, here we write the results of all our computations

#create graph
G = nx.Graph()
#loop through the road shapefile
for index, row in edgesgdf.iterrows():  # loop through edges-table, in edges each has x and y coordinates of Start and End point
    length = row.SHAPE_Leng
    nodeid1=row.nodeid1
    nodeid2 = row.nodeid2
    xcoord1=nodesgdf[nodesgdf["nodeid"]==row.nodeid1].x
    ycoord1 = nodesgdf[nodesgdf["nodeid"] == row.nodeid1].y
    G.add_node(row.nodeid1, pos=(xcoord1, ycoord1))
    xcoord2=nodesgdf[nodesgdf["nodeid"]==row.nodeid2].x
    ycoord2 = nodesgdf[nodesgdf["nodeid"] == row.nodeid2].y
    G.add_node(row.nodeid2, pos=(xcoord2, ycoord2))
    G.add_edge(row.nodeid1, row.nodeid2, weight=length)
print("network graph created ...")

#calculate betweenness centrality for all nodes and write it to the output file
#Betweenness centrality of a node v is the sum of the fraction of all-pairs shortest paths that pass through v.
#parameter k is the number of the sample to safe time, k=1000 --> ca. 1% of the total network is taken as a sample
#if k=None, the full network will be considered. This needs some hours of computation
betweennesscentrality=nx.betweenness_centrality(G, k=1000, normalized=True, endpoints=True)  # output is a dictionnaire
#betweennesscentrality=nx.betweenness_centrality(G, k=None, normalized=True, endpoints=True)
for n in betweennesscentrality:
    nodesbetweennesscentralityfile.write(str(n)+";"+str(betweennesscentrality[n])+"\n")
nodesbetweennesscentralityfile.close()
print("betweenness centrality for nodes in ZH traffic network computed and exported to file ...")


############################
# same for flooded Situation

#script for analysing betweenness centrality in the road network of the Canton of ZH
import numpy as np
import pandas as pd
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt

#general workspace settings
myworkspace="/Users/esthergerber/Desktop/Uni_Bern/Data Science and complex Network/4.12.20_Exercise"

#input data: the csv file for nodes and edges
nodesfile=myworkspace+"/zh_nodes_NOT_flooded/zh_nodes_NOT_flooded.shp"
edgesfile=myworkspace+"/zh_roads_NOT_flooded/zh_roads_NOT_flooded.shp"
#input data: the roads file
nodesgdf = gpd.read_file(nodesfile)
edgesgdf = gpd.read_file(edgesfile)

#output data: the nodes distances file
nodesbetweennesscentralityfile=open(myworkspace+"/betweennesscentrality_floodedsituation.csv","w")
nodesbetweennesscentralityfile.write("nodeid"+";"+"betweennesscentrality"+"\n")  # header of the file, here we write the results of all our computations

#create graph
G = nx.Graph()
#loop through the road shapefile
for index, row in edgesgdf.iterrows():  # loop through edges-table, in edges each has x and y coordinates of Start and End point
    length = row.SHAPE_Leng
    nodeid1=row.nodeid1
    nodeid2 = row.nodeid2
    xcoord1=nodesgdf[nodesgdf["nodeid"]==row.nodeid1].x
    ycoord1 = nodesgdf[nodesgdf["nodeid"] == row.nodeid1].y
    G.add_node(row.nodeid1, pos=(xcoord1, ycoord1))
    xcoord2=nodesgdf[nodesgdf["nodeid"]==row.nodeid2].x
    ycoord2 = nodesgdf[nodesgdf["nodeid"] == row.nodeid2].y
    G.add_node(row.nodeid2, pos=(xcoord2, ycoord2))
    G.add_edge(row.nodeid1, row.nodeid2, weight=length)
print("network graph created ...")

#calculate betweenness centrality for all nodes and write it to the output file
#Betweenness centrality of a node v is the sum of the fraction of all-pairs shortest paths that pass through v.
#parameter k is the number of the sample to safe time, k=1000 --> ca. 1% of the total network is taken as a sample
#if k=None, the full network will be considered. This needs some hours of computation
betweennesscentrality=nx.betweenness_centrality(G, k=1000, normalized=True, endpoints=True)  # output is a dictionnaire
#betweennesscentrality=nx.betweenness_centrality(G, k=None, normalized=True, endpoints=True)
for n in betweennesscentrality:
    nodesbetweennesscentralityfile.write(str(n)+";"+str(betweennesscentrality[n])+"\n")
nodesbetweennesscentralityfile.close()
print("betweenness centrality for nodes in ZH traffic network computed and exported to file ...")

