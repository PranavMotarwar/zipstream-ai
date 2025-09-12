import pandas as pd
import json
from io import BytesIO
from PIL import Image

class FileParser:
    def __init__(self, reader):
        self.reader = reader

    def load(self, file_path: str):
        content = self.reader.read_file(file_path)
        if file_path.endswith('.csv'):
            return pd.read_csv(BytesIO(content))
        elif file_path.endswith('.json'):
            return json.loads(content)
        elif file_path.endswith('.txt'):
            return content.decode('utf-8')
        elif file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            return Image.open(BytesIO(content))
        else:
            raise ValueError("Unsupported file type")