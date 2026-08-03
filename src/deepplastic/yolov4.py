"""YOLOv4-tiny training and inference via AlexeyAB's darknet.

Port of Github_Yolov4.ipynb. All functions shell out to the darknet
executable, so build_darknet() (CUDA + OpenCV required) must succeed
before training or inference. Pretrained convolutional weights come
from the darknet releases; the paper's final weights (best.weights)
are linked in the README.
"""

from __future__ import annotations

import subprocess
import urllib.request
from importlib.resources import files
from pathlib import Path

DARKNET_REPO = "https://github.com/AlexeyAB/darknet"
PRETRAINED_WEIGHTS_URL = (
    "https://github.com/AlexeyAB/darknet/releases/download/"
    "darknet_yolo_v3_optimal/yolov4.conv.137"
)
CONFIG_NAME = "custom-yolov4-tiny-detector.cfg"


def _run(args: list[str], cwd: str | Path) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def build_darknet(darknet_dir: str | Path = "darknet") -> Path:
    """Clone darknet and build it with GPU, cuDNN and OpenCV enabled."""
    darknet_dir = Path(darknet_dir)
    if not darknet_dir.exists():
        _run(["git", "clone", DARKNET_REPO, str(darknet_dir)], cwd=".")

    makefile = darknet_dir / "Makefile"
    contents = makefile.read_text()
    for flag in ("OPENCV", "GPU", "CUDNN", "CUDNN_HALF"):
        contents = contents.replace(f"{flag}=0", f"{flag}=1")
    makefile.write_text(contents)

    _run(["make"], cwd=darknet_dir)
    return darknet_dir


def write_config(
    darknet_dir: str | Path,
    num_classes: int,
    max_batches: int = 10000,
) -> Path:
    """Render the custom YOLOv4-tiny config for the given class count.

    max_batches defaults to 10000, the schedule used in the paper's
    notebook. The darknet training instructions suggest classes * 2000
    (but not less than 6000). Steps are set to 80% and 90% of
    max_batches and filter count to (classes + 5) * 3.
    """
    template = files("deepplastic.templates").joinpath("yolov4_tiny.cfg.template").read_text()
    config = template.format(
        num_classes=num_classes,
        num_filters=(num_classes + 5) * 3,
        max_batches=max_batches,
        steps_str=f"{int(0.8 * max_batches)},{int(0.9 * max_batches)}",
    )
    config_path = Path(darknet_dir) / "cfg" / CONFIG_NAME
    config_path.write_text(config)
    return config_path


def download_pretrained_weights(darknet_dir: str | Path) -> Path:
    """Download yolov4.conv.137 pretrained convolutional weights."""
    dest = Path(darknet_dir) / "yolov4.conv.137"
    if not dest.exists():
        urllib.request.urlretrieve(PRETRAINED_WEIGHTS_URL, dest)
    return dest


def train(darknet_dir: str | Path, weights: str | Path, clear: bool = False) -> None:
    """Train the custom detector.

    Pass pretrained conv weights with clear=True for a fresh run, or a
    backup checkpoint with clear=False to resume (matching the notebook's
    fresh-train and resume cells).
    """
    (Path(darknet_dir) / "backup").mkdir(exist_ok=True)
    args = [
        "./darknet", "detector", "train",
        "data/obj.data", f"cfg/{CONFIG_NAME}", str(Path(weights).resolve()),
        "-dont_show", "-map",
    ]
    if clear:
        args.append("-clear")
    _run(args, cwd=darknet_dir)


def evaluate_map(darknet_dir: str | Path, weights: str | Path, thresh: float = 0.5) -> None:
    """Report mean average precision of trained weights on the valid split."""
    _run(
        [
            "./darknet", "detector", "map",
            "data/obj.data", f"cfg/{CONFIG_NAME}", str(Path(weights).resolve()),
            "-thresh", str(thresh),
        ],
        cwd=darknet_dir,
    )


def detect_image(darknet_dir: str | Path, weights: str | Path, image: str | Path) -> Path:
    """Run detection on one image; darknet writes predictions.jpg next to the binary."""
    _run(
        [
            "./darknet", "detector", "test",
            "data/obj.data", f"cfg/{CONFIG_NAME}", str(Path(weights).resolve()),
            str(Path(image).resolve()), "-dont_show",
        ],
        cwd=darknet_dir,
    )
    return Path(darknet_dir) / "predictions.jpg"


def detect_video(
    darknet_dir: str | Path,
    weights: str | Path,
    video: str | Path,
    output: str = "results.avi",
) -> Path:
    """Run detection over a video and save the annotated result."""
    _run(
        [
            "./darknet", "detector", "demo",
            "data/obj.data", f"cfg/{CONFIG_NAME}", str(Path(weights).resolve()),
            "-dont_show", str(Path(video).resolve()), "-i", "0", "-out_filename", output,
        ],
        cwd=darknet_dir,
    )
    return Path(darknet_dir) / output
