"""DeepPlastic: identifying marine plastic in the epipelagic zone.

Source code for the method developed in
"DeepPlastic: Identifying Marine Plastic In The Epipelagic Zone using
Computer Vision and Deep Learning" (https://arxiv.org/abs/2105.01882).

This package is a modular port of the original Colab notebooks
(kept under notebooks/). It provides:

- deepplastic.utils    -- shared helpers (image display, file utilities)
- deepplastic.dataset  -- dataset download and darknet-format preparation
- deepplastic.yolov4   -- darknet-based YOLOv4-tiny training and inference
- deepplastic.yolov5   -- ultralytics/yolov5-based training and inference
"""

__version__ = "1.0.0"
