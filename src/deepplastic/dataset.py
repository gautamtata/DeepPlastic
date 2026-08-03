"""Dataset download and preparation.

The DeepTrash dataset (1900 train / 637 valid / 637 test images) is
distributed as a Roboflow export: train/, valid/ and test/ directories,
each containing .jpg images with darknet-format .txt label files and a
_darknet.labels class list.

Dataset link: https://drive.google.com/drive/folders/1fsS_u2QpbRGynYkP6-D6cfvq8r0hpjXI
"""

from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

from .utils import list_images


def download_and_extract(url: str, dest: str | Path = ".") -> None:
    """Download a dataset zip (e.g. a Roboflow export link) and extract it into dest."""
    import requests

    dest = Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    archive = dest / "dataset.zip"

    try:
        with requests.get(url, stream=True, timeout=60) as response:
            response.raise_for_status()
            with open(archive, "wb") as f:
                for chunk in response.iter_content(chunk_size=1 << 20):
                    f.write(chunk)

        with zipfile.ZipFile(archive) as zf:
            zf.extractall(dest)
    finally:
        archive.unlink(missing_ok=True)


def prepare_darknet_dataset(dataset_dir: str | Path, darknet_dir: str | Path) -> Path:
    """Lay out a Roboflow darknet export inside a darknet working directory.

    Copies train/valid images and labels into data/obj/, writes obj.names,
    obj.data, train.txt and valid.txt, and returns the path to obj.data.
    The deepplastic.yolov4 helpers expect this layout (data/obj.data
    relative to the darknet directory).
    """
    dataset_dir = Path(dataset_dir)
    data_dir = Path(darknet_dir) / "data"
    obj_dir = data_dir / "obj"
    obj_dir.mkdir(parents=True, exist_ok=True)

    labels_file = dataset_dir / "train" / "_darknet.labels"
    shutil.copy(labels_file, data_dir / "obj.names")
    num_classes = len(labels_file.read_text().splitlines())

    for split in ("train", "valid"):
        split_dir = dataset_dir / split
        for pattern in ("*.jpg", "*.txt"):
            for f in split_dir.glob(pattern):
                shutil.copy(f, obj_dir / f.name)
        image_list = data_dir / f"{split}.txt"
        image_list.write_text(
            "".join(f"data/obj/{img.name}\n" for img in list_images(split_dir))
        )

    obj_data = data_dir / "obj.data"
    obj_data.write_text(
        f"classes = {num_classes}\n"
        "train = data/train.txt\n"
        "valid = data/valid.txt\n"
        "names = data/obj.names\n"
        "backup = backup/"
    )
    return obj_data
