# Breadth-First Search Using a FIFO Queue
# it look for a node that satisfies a particular condition by exploring the graph in concentric layers or levels.
# Using chosen source node unless the graph is a tree data structure, in which case you typically start at the root node of that tree. 

import networkx as nx
from graph import City, load_graph

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000