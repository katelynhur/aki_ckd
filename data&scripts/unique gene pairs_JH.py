import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read the Excel files
all_AKI_genes = pd.read_excel('./AMIA2024/AKI gene pairs.xlsx', dtype=str)
all_CKD_genes = pd.read_excel('./AMIA2024/CKD gene pairs.xlsx', dtype=str)

# Create a graph
G = nx.Graph()

# Function to add edges to the graph
def add_edges(df, color, unique_set):
    for i in range(len(df)):
        gene1 = df.iloc[i, 1]
        gene2 = df.iloc[i, 2]
        weight = float(df.iloc[i, 3].replace(' hits', ''))  # Extract numeric value
        G.add_edge(gene1, gene2, color=color, weight=weight, unique=unique_set)

# Add edges for AKI and CKD
add_edges(all_AKI_genes, 'red', 'AKI')
add_edges(all_CKD_genes, 'blue', 'CKD')

# Add common edges with average weights
common_pairs = set(tuple(sorted([all_AKI_genes.iloc[i, 1], all_AKI_genes.iloc[i, 2]])) for i in range(len(all_AKI_genes))) & \
               set(tuple(sorted([all_CKD_genes.iloc[i, 1], all_CKD_genes.iloc[i, 2]])) for i in range(len(all_CKD_genes)))

# Calculate unique pairs for AKI and CKD
unique_AKI_pairs = set(tuple(sorted([all_AKI_genes.iloc[i, 1], all_AKI_genes.iloc[i, 2]])) for i in range(len(all_AKI_genes))) - common_pairs
unique_CKD_pairs = set(tuple(sorted([all_CKD_genes.iloc[i, 1], all_CKD_genes.iloc[i, 2]])) for i in range(len(all_CKD_genes))) - common_pairs

# Print the counts
print(f"Number of common pairs: {len(common_pairs)}")
print(f"Number of unique AKI pairs: {len(unique_AKI_pairs)}")
print(f"Number of unique CKD pairs: {len(unique_CKD_pairs)}")

for pair in common_pairs:
    gene1, gene2 = pair
    weight_AKI = float(all_AKI_genes[(all_AKI_genes.iloc[:, 1] == gene1) & (all_AKI_genes.iloc[:, 2] == gene2)].iloc[0, 3].replace(' hits', ''))
    weight_CKD = float(all_CKD_genes[(all_CKD_genes.iloc[:, 1] == gene1) & (all_CKD_genes.iloc[:, 2] == gene2)].iloc[0, 3].replace(' hits', ''))
    avg_weight = (weight_AKI + weight_CKD) / 2
    G.add_edge(gene1, gene2, color='green', weight=avg_weight, unique='common')

# Centrality analysis
degree_dict = dict(G.degree())
nx.set_node_attributes(G, degree_dict, 'degree')

# Draw the network
pos = nx.spring_layout(G)
node_sizes = [v * 100 for v in degree_dict.values()]  # Scale node sizes
edge_colors = [G[u][v]['color'] for u, v in G.edges()]

# Draw nodes and edges
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='lightgray')
nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
nx.draw_networkx_labels(G, pos)

# Save the network as an image
plt.title("Gene Interaction Network")
plt.axis('off')
plt.savefig('./AMIA2024/gene_network.png', format='png')
plt.close()

# Save the graph to an XML file
nx.write_graphml(G, './AMIA2024/gene_network.graphml')