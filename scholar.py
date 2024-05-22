import networkx as nx
import matplotlib.pyplot as plt
from scholarly import scholarly

# Initial setup
seed_author = 'Aldina Correia'
G = nx.Graph()

# Search for the author
search_query = scholarly.search_author(seed_author)
author = scholarly.fill(next(search_query))

print(len(author))

# Add nodes and edges to the graph
for p in author['publications']:
    print(p)
    publication_filled = scholarly.fill(p)
    bib = publication_filled['bib']
    title = bib['title'].replace(':', ' ')
    title = f"Paper/{title}"
    authors = bib['author'].split(' and ')
    for author in authors:
        author = author.replace('.', '')
        author = ' '.join([n for n in author.split(' ') if len(n) > 1])
        author = f"Author/{author}"
        G.add_edge(author, title)

# Check the nodes to ensure they are correctly formatted
print("Nodes in the graph:")
for node in G.nodes:
    print(node)

# Alternative layout in case of issues with graphviz_layout
try:
    pos = nx.nx_pydot.graphviz_layout(G, prog='sfdp')
except Exception as e:
    print(f"Graphviz layout error: {e}")
    pos = nx.spring_layout(G)

# Calculate maximum length of author names for node size
max_len = max([len(n) for n in G.nodes() if n.startswith('Author/')])

# Plot the graph
plt.figure(figsize=(24, 18))

nx.draw_networkx_nodes(G, pos,
                       nodelist=[n for n in G.nodes() if n.startswith('Author/')],
                       node_size=max_len * 500)

nx.draw_networkx_nodes(G, pos,
                       nodelist=[n for n in G.nodes() if n.startswith('Paper/')],
                       node_color='y',
                       node_size=1000)

nx.draw_networkx_edges(G, pos)

nx.draw_networkx_labels(G, pos,
                        labels={n: n.split('/')[-1].replace(' ', '\n') for n in G.nodes() if n.startswith('Author/')},
                        font_color='w',
                        font_weight='bold')

plt.axis('off')
plt.savefig('sample_plot.png')
plt.show()
