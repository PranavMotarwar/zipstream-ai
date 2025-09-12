import zipfile
import tarfile
from typing import List

class ZipStreamReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        if file_path.endswith('.zip'):
            self.archive = zipfile.ZipFile(file_path, 'r')
            self.type = 'zip'
        elif file_path.endswith('.tar.gz') or file_path.endswith('.tgz'):
            self.archive = tarfile.open(file_path, 'r:gz')
            self.type = 'tar'
        else:
            raise ValueError("Unsupported archive type")

    def list_files(self) -> List[str]:
        if self.type == 'zip':
            return self.archive.namelist()
        elif self.type == 'tar':
            return [member.name for member in self.archive.getmembers()]

    def read_file(self, file_name: str) -> bytes:
        if self.type == 'zip':
            with self.archive.open(file_name) as f:
                return f.read()
        elif self.type == 'tar':
            member = self.archive.getmember(file_name)
            return self.archive.extractfile(member).read()