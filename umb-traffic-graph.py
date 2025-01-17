import networkx as nx
import matplotlib.pyplot as plt

# Inisialisasi graph
G = nx.Graph()

# Tambah nodes/vertices (lokasi)
locations = [
    'Gerbang Kampus 1',
    'Pertigaan Utama',
    'Perpustakaan',
    'Gedung Rektorat', 
    'Kantin',
    'Fakultas Teknik'
]

G.add_nodes_from(locations)

# Tambah edges (jalan) dengan bobot jarak dalam meter
edges = [
    ('Gerbang Kampus 1', 'Pertigaan Utama', 100),
    ('Pertigaan Utama', 'Perpustakaan', 150),
    ('Pertigaan Utama', 'Gedung Rektorat', 200),
    ('Perpustakaan', 'Kantin', 100),
    ('Gedung Rektorat', 'Kantin', 150),
    ('Kantin', 'Fakultas Teknik', 100)
]

G.add_weighted_edges_from(edges)

# Atur layout graph
pos = nx.spring_layout(G)

# Gambar nodes
nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                      node_size=2000, alpha=0.6)

# Gambar edges
nx.draw_networkx_edges(G, pos)

# Tambah label nodes
nx.draw_networkx_labels(G, pos, font_size=8)

# Tambah label edges (jarak)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels)

# Atur tampilan
plt.title("Graph Lalu Lintas Kampus 1 UMB ke Fakultas Teknik")
plt.axis('off')

# Cari shortest path dari Gerbang ke Fakultas Teknik
path = nx.shortest_path(G, 'Gerbang Kampus 1', 'Fakultas Teknik', weight='weight')
path_length = nx.shortest_path_length(G, 'Gerbang Kampus 1', 'Fakultas Teknik', weight='weight')

# Print hasil
print("Rute terpendek:", ' -> '.join(path))
print(f"Total jarak: {path_length} meter")

# Tampilkan graph
plt.show()
