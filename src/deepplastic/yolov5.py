"""YOLOv5 training and inference via the ultralytics/yolov5 repository.

Port of Github_Yolov5.ipynb. The original notebook targeted the 2021-era
yolov5 repo, whose train.py/test.py/detect.py scripts are invoked here as
subprocesses. The paper's final weights (best.pt) are linked in the README.
"""

from __future__ import annotations

import subprocess
import sys
from importlib.resources import files
from pathlib import Path

YOLOV5_REPO = "https://github.com/ultralytics/yolov5"
CUSTOM_MODEL_NAME = "custom_yolov5s.yaml"


def _run(args: list[str], cwd: str | Path) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def clone_yolov5(yolov5_dir: str | Path = "yolov5") -> Path:
    """Clone the ultralytics/yolov5 repository if not already present."""
    yolov5_dir = Path(yolov5_dir)
    if not yolov5_dir.exists():
        _run(["git", "clone", YOLOV5_REPO, str(yolov5_dir)], cwd=".")
    return yolov5_dir


def num_classes_from_data_yaml(data_yaml: str | Path) -> int:
    """Read the class count (nc) from a Roboflow data.yaml."""
    import yaml

    with open(data_yaml) as stream:
        return int(yaml.safe_load(stream)["nc"])


def write_model_config(yolov5_dir: str | Path, num_classes: int) -> Path:
    """Render the custom yolov5s model yaml for the given class count."""
    template = files("deepplastic.templates").joinpath("yolov5s_custom.yaml.template").read_text()
    config_path = Path(yolov5_dir) / "models" / CUSTOM_MODEL_NAME
    config_path.write_text(template.format(num_classes=num_classes))
    return config_path


def train(
    yolov5_dir: str | Path,
    data_yaml: str | Path,
    weights: str | Path = "",
    img_size: int = 416,
    batch_size: int = 16,
    epochs: int = 500,
    name: str = "deepplastic",
    cache: bool = True,
) -> None:
    """Train a custom YOLOv5s detector (pass weights='' to train from scratch)."""
    args = [
        sys.executable, "train.py",
        "--img", str(img_size),
        "--batch", str(batch_size),
        "--epochs", str(epochs),
        "--data", str(Path(data_yaml).resolve()),
        "--cfg", f"./models/{CUSTOM_MODEL_NAME}",
        "--weights", str(weights),
        "--name", name,
    ]
    if cache:
        args.append("--cache")
    _run(args, cwd=yolov5_dir)


def evaluate(
    yolov5_dir: str | Path,
    data_yaml: str | Path,
    weights: str | Path,
    img_size: int = 416,
    conf_thresh: float = 0.4,
) -> None:
    """Evaluate trained weights (the 2021 repo calls this test.py, later val.py)."""
    script = "test.py" if (Path(yolov5_dir) / "test.py").exists() else "val.py"
    _run(
        [
            sys.executable, script,
            "--data", str(Path(data_yaml).resolve()),
            "--img", str(img_size),
            "--conf", str(conf_thresh),
            "--weights", str(Path(weights).resolve()),
        ],
        cwd=yolov5_dir,
    )


def detect(
    yolov5_dir: str | Path,
    weights: str | Path,
    source: str | Path,
    img_size: int = 416,
) -> None:
    """Run inference on an image, directory or video; results land in runs/detect/."""
    _run(
        [
            sys.executable, "detect.py",
            "--weights", str(Path(weights).resolve()),
            "--img", str(img_size),
            "--source", str(Path(source).resolve()),
        ],
        cwd=yolov5_dir,
    )
