"""Shared helpers used by both the YOLOv4 and YOLOv5 workflows."""

from __future__ import annotations

from pathlib import Path


def show_image(path: str | Path, scale: int = 3, figsize: tuple[int, int] = (18, 10)) -> None:
    """Display an image upscaled with matplotlib (port of the notebooks' imShow)."""
    import cv2
    import matplotlib.pyplot as plt

    image = cv2.imread(str(path))
    if image is None:
        raise FileNotFoundError(f"Could not read image: {path}")
    height, width = image.shape[:2]
    resized = cv2.resize(image, (scale * width, scale * height), interpolation=cv2.INTER_CUBIC)

    fig = plt.gcf()
    fig.set_size_inches(*figsize)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
    plt.show()


def count_lines(path: str | Path) -> int:
    """Number of lines in a file (port of the notebooks' file_len)."""
    with open(path) as f:
        return sum(1 for _ in f)


def list_images(directory: str | Path, suffix: str = ".jpg") -> list[Path]:
    """All images with the given suffix in a directory, sorted by name."""
    return sorted(p for p in Path(directory).iterdir() if p.suffix == suffix)
