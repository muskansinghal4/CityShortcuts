# 🚦 CityShortcuts

**CityShortcuts** is a Data Structures and Algorithms-based project that models a city's road network as a **weighted graph** to compute the most efficient routes between two points. The project leverages **Greedy Algorithms**, such as **Dijkstra’s** and **A\***, to determine optimal paths by minimizing travel distance or time.

---

## Objectives

- Represent real-world road networks using graphs
- Implement Greedy pathfinding algorithms (**Dijkstra**, **A\***)
- Simulate traffic conditions by dynamically updating edge weights
- Provide visual output (text-based or map-based) of the shortest or fastest path

---

## DSA Concepts Used

- **Graphs (Adjacency List):** Represents city roads and intersections
- **Greedy Algorithms:** For optimal path selection
- **Dijkstra's Algorithm:** Finds shortest paths in weighted graphs
- **A\* Search Algorithm:** Heuristic-based greedy search (Euclidean/Manhattan distance)
- **Priority Queue / Min-Heap:** For efficient node selection
- **Hash Maps:** Fast lookups for node and edge metadata
- **Dynamic Weighting:** Adjusts road costs based on simulated traffic

---

## Features

- Compute shortest/fastest path between any two city points
- Handle one-way roads and blocked streets
- Display alternate paths and rerouting suggestions
- Optionally integrate with map data (e.g., **OpenStreetMap**)

---

## Use Cases

- Real-time navigation system for smart cities
- Traffic-aware logistics and delivery routing
- Educational tool for demonstrating graph algorithms in urban contexts

---

## Tech Stack

### 🌐 Frontend
- **React.js**
- **Leaflet.js** or **Mapbox GL JS** (for map rendering)

### Backend
- **Python** with **FastAPI** (for algorithms and APIs)

### Database
- **PostgreSQL** with **PostGIS** (for spatial and geographical queries)

---
