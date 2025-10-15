import pandas as pd
import json
import csv
from io import BytesIO
from PIL import Image

class FileParser:
    def __init__(self, reader):
        self.reader = reader

    def _detect_delimiter(self, sample_str: str) -> str:
        sniffer = csv.Sniffer()
        try:
            dialect = sniffer.sniff(sample_str)
            return dialect.delimiter
        except csv.Error:
            return ','

    def load(self, file_path: str):
        content = self.reader.read_file(file_path)

        if file_path.endswith('.csv'):
            sample = content[:1024].decode(errors='ignore')
            delimiter = self._detect_delimiter(sample)
            return pd.read_csv(BytesIO(content), delimiter=delimiter)

        elif file_path.endswith('.json'):
            return json.loads(content)

        elif file_path.endswith('.txt'):
            return content.decode('utf-8')

        elif file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            return Image.open(BytesIO(content))

        elif file_path.endswith('.parquet'):
            try:
                import pyarrow  # noqa: F401
                return pd.read_parquet(BytesIO(content), engine="pyarrow")
            except Exception as e:
                try:
                    import fastparquet  # noqa: F401
                    return pd.read_parquet(BytesIO(content), engine="fastparquet")
                except Exception:
                    raise RuntimeError(
                        "Reading .parquet requires 'pyarrow' or 'fastparquet'. "
                        "Install one, e.g.: pip install pyarrow"
                    ) from e

        else:
            raise ValueError("Unsupported file type")
