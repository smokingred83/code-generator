import os
from typing import Generator

from transformers import AutoTokenizer

from code_generator.settings import settings


def flatten(nested_list: list) -> list:
    """Flatten a list of lists into a single list."""

    return [item for sublist in nested_list for item in sublist]


def batch(list_: list, size: int) -> Generator[list, None, None]:
    yield from (list_[i : i + size] for i in range(0, len(list_), size))


def compute_num_tokens(text: str) -> int:
    tokenizer = AutoTokenizer.from_pretrained(settings.HF_MODEL_ID)

    return len(tokenizer.encode(text, add_special_tokens=False))


def on_access_error(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    # Is the error an access error?
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise
