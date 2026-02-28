import mysql.connector
import networkx as nx

# 1. Establish the connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="distributionsystem"
)

cursor = db.cursor()

# 2. Fetch the "Edges" (Routes) from your database
# We pull source, destination, and the final_cost as the weight
query = "SELECT source_node_id, destination_node_id, final_cost FROM routes"
cursor.execute(query)
rows = cursor.fetchall()

# 3. Initialize the Graph
G = nx.DiGraph() # Directed Graph because routes have a specific direction

# 4. Add edges to the graph using your SQL data
# 4. Add edges
for source, dest, cost in rows:
    G.add_edge(source, dest, weight=float(cost))

# 🔹 Simulate Multiple Blocked Routes
blocked_routes = [
    (1, 11),
    (3, 7),
    (2, 5)
]

for blocked_source, blocked_destination in blocked_routes:
    if G.has_edge(blocked_source, blocked_destination):
        G.remove_edge(blocked_source, blocked_destination)
        print(f"Route {blocked_source} -> {blocked_destination} is blocked and removed.")
    else:
        print(f"Route {blocked_source} -> {blocked_destination} does not exist.")

# 5. Run Dijkstra
# 5. Compare Original and Blocked Routes

source_node = 1
target_node = 5

try:
    # 🔹 ORIGINAL SHORTEST PATH (No Blockage)
    original_path = nx.dijkstra_path(G, source_node, target_node, weight='weight')
    original_cost = nx.dijkstra_path_length(G, source_node, target_node, weight='weight')

    print("\n--- Original Optimal Route (No Blockage) ---")
    print(f"Path: {' -> '.join(map(str, original_path))}")
    print(f"Total Cost: {original_cost:.2f}")

    # 🔹 CREATE COPY OF GRAPH FOR BLOCKAGE SIMULATION
    G_blocked = G.copy()

    # 🔹 Define Blocked Routes
    blocked_routes = [
        (1, 5),
        (3, 7),
        (2, 5)
    ]

    print("\n--- Simulating Blocked Routes ---")
    for blocked_source, blocked_destination in blocked_routes:
        if G_blocked.has_edge(blocked_source, blocked_destination):
            G_blocked.remove_edge(blocked_source, blocked_destination)
            print(f"Blocked: {blocked_source} -> {blocked_destination}")
        else:
            print(f"Route {blocked_source} -> {blocked_destination} does not exist.")

    # 🔹 NEW SHORTEST PATH AFTER BLOCKAGE
    new_path = nx.dijkstra_path(G_blocked, source_node, target_node, weight='weight')
    new_cost = nx.dijkstra_path_length(G_blocked, source_node, target_node, weight='weight')

    print("\n--- New Optimal Route (After Blockage) ---")
    print(f"Path: {' -> '.join(map(str, new_path))}")
    print(f"Total Cost: {new_cost:.2f}")

    # 🔹 COST COMPARISON
    extra_cost = new_cost - original_cost

    print("\n--- Cost Comparison ---")
    print(f"Extra Cost Due to Blockage: {extra_cost:.2f}")

except nx.NetworkXNoPath:
    print("No path exists between the nodes after blockage.")

finally:
    cursor.close()
    db.close()