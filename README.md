# Distribution-Routing-System

Developed a logistics routing system using MySQL and Python to compute optimal delivery paths between a warehouse and retail stores. Implemented Dijkstra’s algorithm with real geographic distance (Haversine formula) and dynamic blockage simulation to analyze cost impact.

## 🚀 Key Features

- 📍 Geographic distance calculation using the Haversine formula
- 🗄 Relational database design using MySQL
- 🔗 Graph modeling using NetworkX
- 🧮 Cost modeling including:
  - Distance-based fuel cost
  - Traffic penalty factor
  - Weather impact factor
- 🛣 Dynamic road blockage simulation
- 📊 Cost comparison before and after route blockage
- 📈 Graph visualization using Spring Layout
- 
## 🧠 How It Works

1. Warehouse and store details are stored in the `nodes` table.
2. Routes are generated dynamically using a CROSS JOIN and Haversine formula.
3. Each route is assigned a final weighted cost.
4. The network is modeled as a directed graph.
5. Dijkstra’s algorithm computes the optimal route.
6. If specific roads are blocked, edges are removed dynamically and the system recalculates the optimal path.
7. The system also compares original vs disrupted route cost to estimate additional expenses.

## 🛠 Technologies Used

- Python
- MySQL
- NetworkX
- Matplotlib
- SQL (DDL, DML, Joins, Haversine formula)

## 📂 Project Structure
Distribution-Routing-System/
│
├── route_optimizer.py
├── graph.py
├── database.sql
├── requirements.txt
└── README.md

## ▶ How to Run

1. Create the MySQL database using `database.sql`.
2. Insert node data (warehouse and store locations).
3. Run the route generation query.
4. Execute `route_optimizer.py` to compute optimal routes.
5. Execute `graph.py` to visualize the network.


## 📈 Future Enhancements

- Real-time traffic API integration
- Weather API-based dynamic cost updates
- A* algorithm comparison
- Interactive user interface
- Route prioritization based on delivery urgency
- Real geographic map overlay visualization

This project is continuously evolving and will be updated with new features and improvements as additional optimization ideas are explored.

## 📌 Author

Developed as part of an academic project and extended for practical logistics optimization modeling.

