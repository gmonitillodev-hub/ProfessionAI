from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ProcessedPath:
    file_path: str
    file_name: str


def check_folder(folder_path: str | Path) -> list["ProcessedPath"]:
    path = Path(folder_path)

    if path.is_file():
        return [
            ProcessedPath(
                file_path=str(path),
                file_name=path.name
            )
        ]

    elif path.is_dir():
        processed_paths: list[ProcessedPath] = []

        documents = [item for item in path.iterdir() if item.is_file()]
        for document in documents:
            processed_paths.append(
                ProcessedPath(
                    file_path=str(document),
                    file_name=document.name
                )
            )

        return processed_paths
    else:
        raise FileNotFoundError("Path inesistente o non valido")
