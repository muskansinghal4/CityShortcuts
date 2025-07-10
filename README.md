# CityShortcuts
Description: City Shortcuts is a data structures and algorithms-based project that models a city's road network as a weighted graph to compute the most efficient routes between two points. The project focuses on leveraging Greedy algorithms, such as Dijkstra’s and A*, to determine the optimal path by minimizing travel distance or time.
Using real or simulated traffic data, the system dynamically assigns weights to roads and computes shortcuts across the city — avoiding congested paths and roadblocks intelligently.

Objectives:
Represent real-world road networks using graphs
Implement Greedy pathfinding algorithms (Dijkstra, A*) for route optimization
Simulate traffic conditions by dynamically updating edge weights
Provide visual output (text-based or map-based) of the shortest or fastest path

DSA Concepts Used:
Graphs (Adjacency List) – City roads and intersections
Greedy Algorithms – Dijkstra's algorithm for shortest path
A* Search – Optimized greedy search using heuristics (Euclidean/Manhattan distance)
Priority Queue / Min-Heap – Efficient node selection during traversal
Hash Maps – For node/edge metadata and fast lookup
Dynamic Weighting – Adjust road costs based on simulated traffic

📈 Features:
Compute shortest/fastest path between any two city points
Handle one-way roads and blocked streets
Display alternate paths and rerouting suggestions
Optionally integrate with map data (OpenStreetMap)

Use Cases:
Real-time navigation system for smart cities
Traffic-aware logistics routing
Educational tool for demonstrating graph algorithms in urban contexts

🧩 Future Extensions:
Integrate live traffic data using APIs (e.g., Google Maps)
Add public transport and walking route support
Use historical traffic patterns for predictive routing


Tech Stack: 
FrontEnd: React + Leaflet/Mapbox GL JS
BackEnd: Python(w/ FastAPI)
Database: PostgreSQL with PostGIS
