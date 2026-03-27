"""FLIRT signatures for binary analysis."""

from importlib.resources import files


def signatures_path() -> str:
    """Return the path to the directory containing FLIRT signature files."""
    return str(files(__package__))