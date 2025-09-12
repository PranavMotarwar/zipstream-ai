import typer
from .stream_reader import ZipStreamReader
from .file_parser import FileParser
from .llm_query_engine import ask

app = typer.Typer()

@app.command()
def browse(archive_path: str):
    reader = ZipStreamReader(archive_path)
    files = reader.list_files()
    for f in files:
        print(f)

@app.command()
def query(archive_path: str, filename: str, question: str):
    reader = ZipStreamReader(archive_path)
    parser = FileParser(reader)
    data = parser.load(filename)
    answer = ask(data, question)
    print(answer)

if __name__ == "__main__":
    app()