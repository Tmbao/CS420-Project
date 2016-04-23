try:
    import matplotlib.pyplot as plt
except:
    raise
import networkx as nx
#import pygraphviz as pg
from networkx.drawing.nx_agraph import graphviz_layout

'''
!!!TODO:
Choose a good looking layout prog
http://www.graphviz.org/
'''

def plot(file_name, graph, source, target, path, weight_tag='len', name_tag='name', color='b', layout_type='neato'):
    pos = graphviz_layout(graph, prog=layout_type) # choose a better prog?

    node_list = [source]

    for edge in path:
        (u, v) = edge
        node_list.append(v)

    # draw nodes
    nx.draw_networkx_nodes(graph, pos, nodelist=[x for x in graph.nodes() if not x == source])
    nx.draw_networkx_nodes(graph, pos, nodelist=node_list, node_color=color)

    # draw edges
    nx.draw_networkx_edges(graph, pos, edgelist=[x for x in graph.edges() if not x in path])
    nx.draw_networkx_edges(graph, pos, edgelist=path, width=1, edge_color=color)

    # draw labels
    node_labels = nx.get_node_attributes(graph, name_tag)
    nx.draw_networkx_labels(graph, pos, labels=node_labels)
    labels = nx.get_edge_attributes(graph, weight_tag)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.axis('off')
    plt.savefig(file_name)
    plt.show()
        
