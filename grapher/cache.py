import json
from pathlib import Path
import os
from typing import TypeVar
from json.decoder import JSONDecodeError

Response = TypeVar("Response", dict, None)


class CacheControl:
    """
    Naive Cache implementation
    pass in filename to be used for caching
    """

    def __init__(self, filename: str = "data.json") -> None:
        self.file = Path(filename)

    def load_data(self) -> Response:
        if self.file.exists():
            with open(self.file.resolve(), "r") as f:
                try:
                    data = json.load(f)
                    return data
                except JSONDecodeError as e:
                    print(e)
                    self.offload_cache()
        return None

    def cache_data(self, data: dict) -> None:
        with open(self.file.resolve(), "w") as f:
            json.dump(data, f)

    def offload_cache(self) -> None:
        os.remove(self.file.resolve())
