import mysql.connector
import networkx as nx
import matplotlib.pyplot as plt

# 1️⃣ Connect to Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="distributionsystem"
)

cursor = db.cursor()

# 2️⃣ Fetch Routes
query = "SELECT source_node_id, destination_node_id, final_cost FROM routes"
cursor.execute(query)
rows = cursor.fetchall()

# 3️⃣ Create Graph
G = nx.DiGraph()

for source, dest, cost in rows:
    G.add_edge(source, dest, weight=float(cost))

cursor.close()
db.close()

# 4️⃣ Draw Graph
plt.figure(figsize=(10, 8))

pos = nx.spring_layout(G) # Layout positioning

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=700,
    node_color="lightblue",
    font_size=8,
    arrows=True
)

# Draw edge labels (cost)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

plt.title("Distribution Routing Network Graph")
plt.show()