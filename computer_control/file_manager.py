from pathlib import Path
import shutil
import os


class FileManager:

    def create_folder(self, path: str):
        Path(path).mkdir(parents=True, exist_ok=True)

    def create_file(self, path: str, content: str = ""):
        Path(path).write_text(content, encoding="utf-8")

    def read_file(self, path: str):
        return Path(path).read_text(encoding="utf-8")

    def write_file(self, path: str, content: str):
        Path(path).write_text(content, encoding="utf-8")

    def append_file(self, path: str, content: str):
        with open(path, "a", encoding="utf-8") as f:
            f.write(content)

    def exists(self, path: str):
        return Path(path).exists()

    def delete(self, path: str):
        target = Path(path)

        if target.is_file():
            target.unlink()

        elif target.is_dir():
            shutil.rmtree(target)

    def copy(self, source: str, destination: str):
        source = Path(source)
        destination = Path(destination)

        if source.is_dir():
            shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(source, destination)

    def move(self, source: str, destination: str):
        shutil.move(source, destination)

    def rename(self, source: str, destination: str):
        os.rename(source, destination)

    def list_files(self, path: str):
        return [str(item) for item in Path(path).iterdir()]

    def search(self, path: str, pattern: str):
        return [
            str(item)
            for item in Path(path).rglob(pattern)
        ]

    def size(self, path: str):
        return Path(path).stat().st_size


if __name__ == "__main__":

    manager = FileManager()

    print(manager.exists("."))
