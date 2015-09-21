__author__ = 'Andrew A Campbell'

import networkx as nx
import pandas as pd

#TODO - move all of this to a config file
tmc_ident = r'C:\Users\acampbell\Documents\FCMS\Inrix\San-Francisco-and-San-Mateo-050114-043014\TMC_Identification.csv'
out = r'C:\Users\acampbell\Documents\FCMS\Inrix\San-Francisco-and-San-Mateo-050114-043014\TMC_nodes.csv'

df = pd.read_csv(tmc_ident, sep=',', header=0, index_col=False)

# Get list of unique node locations
node_coords = dict((k, v) for k,v in enumerate(list(set(zip(df.start_latitude, df.start_longitude)
                                                        + zip(df.end_latitude, df.end_longitude)))))
node_lookup = dict((v, k) for k,v in node_coords.items())

# Build the digraph
dg = nx.DiGraph()
# Add the nodes with dummy values for tmcs
for n, c in node_coords.items():
    dg.add_node(n, {'latitude': c[0], 'longitude': c[1], 'in_tmc': [], 'out_tmc': []})

# Add the directed edges (TMCs are edges) and update node attributes.
for row in df.iterrows():
    node_start = node_lookup[(row[1]['start_latitude'], row[1]['start_longitude'])]
    node_end = node_lookup[(row[1]['end_latitude'], row[1]['end_longitude'])]
    dg.add_edge(node_start, node_end, tmc=row[1]['tmc'])
    dg.node[node_start]['out_tmc'].append(row[1]['tmc'])
    dg.node[node_end]['in_tmc'].append(row[1]['tmc'])

# Create a dataframe from the nodes
df_out = pd.DataFrame.from_dict(dict(dg.nodes(data=True)), orient='index')

# Write the output csv
df_out.to_csv(out, sep=',', header=True, index=True, index_label='id')










