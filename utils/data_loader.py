import json
import os

def load_test_data():
    # Obtengo la ruta absoluta del directoriio actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Subo un nivel para ir a la raíz y entro a 'data'
    json_path = os.path.join(current_dir, '..', 'data', 'test_data.json')
    
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data