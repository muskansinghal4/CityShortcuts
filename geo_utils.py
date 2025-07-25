import math
from typing import Tuple

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of earth in kilometers
    return c * r

def find_nearest_node(lat: float, lon: float, nodes: list) -> int:
    """
    Find the nearest node to the given coordinates
    """
    min_distance = float('inf')
    nearest_node_id = None
    
    for node in nodes:
        distance = haversine_distance(lat, lon, node.latitude, node.longitude)
        if distance < min_distance:
            min_distance = distance
            nearest_node_id = node.id
    
    return nearest_node_id