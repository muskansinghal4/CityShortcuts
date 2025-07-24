
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import osmnx as ox
import networkx as nx
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

G_delhi = None
G_delhi_proj = None 

def load_delhi_graph():
    """
    Loads the street network graph for Delhi using OSMnx.
    This function will be called once.
    """
    global G_delhi, G_delhi_proj
    if G_delhi is None:
        logger.info("Loading Delhi street network graph... This might take a while.")
        try:
            place_name = 'Delhi, India'
            G_delhi = ox.graph_from_place(place_name, network_type='drive')
            G_delhi_proj = ox.project_graph(G_delhi)
            logger.info("Delhi street network graph loaded and projected successfully.")
            logger.info(f"Graph has {len(G_delhi_proj.nodes)} nodes and {len(G_delhi_proj.edges)} edges.")
        except Exception as e:
            logger.error(f"Failed to load Delhi graph: {e}")
            G_delhi = None 
            G_delhi_proj = None
            raise

def find_shortest_path_backend(start_lat, start_lng, end_lat, end_lng):
    global G_delhi_proj

    if G_delhi_proj is None:
        load_delhi_graph()

    if G_delhi_proj is None:
        raise Exception("Street network graph is not loaded. Cannot find path.")

    orig_node = ox.nearest_nodes(G_delhi_proj, start_lng, start_lat)
    dest_node = ox.nearest_nodes(G_delhi_proj, end_lng, end_lat)

    logger.info(f"Finding path from node {orig_node} to node {dest_node}")

    # Dijkstra's algo
    try:
        path = nx.shortest_path(G_delhi_proj, orig_node, dest_node, weight='length')
    except nx.NetworkXNoPath:
        raise Exception("No path found between the specified locations.")
    except Exception as e:
        raise Exception(f"Error during path calculation: {e}")

    # Convert to cords
    path_coords = []
    for node_id in path:
        node_data = G_delhi_proj.nodes[node_id]
        path_coords.append([node_data['y'], node_data['x']])

    logger.info(f"Path found with {len(path_coords)} points.")
    return path_coords

@app.route('/')
def index():
    return render_template('temp_front.html')

@app.route('/shortest_path', methods=['POST'])
def get_shortest_path_api():

    data = request.get_json()
    start_lat = data.get('start_lat')
    start_lng = data.get('start_lng')
    end_lat = data.get('end_lat')
    end_lng = data.get('end_lng')

    if not all(v is not None for v in [start_lat, start_lng, end_lat, end_lng]):
        return jsonify({"error": "Missing one or more coordinates (start_lat, start_lng, end_lat, end_lng)"}), 400

    try:
        path_coordinates = find_shortest_path_backend(start_lat, start_lng, end_lat, end_lng)
        return jsonify({"path": path_coordinates})
    except Exception as e:
        logger.error(f"API Error: {e}")
        return jsonify({"error": "Failed to calculate path", "details": str(e)}), 500

if __name__ == '__main__':
    try:
        load_delhi_graph()
    except Exception as e:
        logger.error(f"Initial graph loading failed: {e}. The app will attempt to load it on first request.")

    #http://127.0.0.1:5000/
    app.run(debug=True, port=5000)
