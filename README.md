![status: inactive](https://img.shields.io/badge/status-inactive-red.svg)
# Project Archive Notice
This project has been archived and is no longer actively maintained. This means that no further updates or bug fixes will be provided.

Please note that we will not be accepting any pull requests or requests for updating the code. However, you are free to fork this repository and continue development on your own.

## Can I still use this code?

Yes, you are still free to use this code under the terms of the MIT License. However, please be aware that the code may contain bugs or security vulnerabilities, and we will not be providing any support or updates.

## How do I get help?
If you have any questions about this project or need assistance with using the code, we recommend that you seek help from the community or other resources. However, please note that we will not be providing any support or assistance.

Thank you for your interest in this project.

### Update (August 2026)
While this project remains archived and unmaintained, the two original Colab notebooks have been converted into a modular Python package under `src/deepplastic/` (the notebooks are preserved in `notebooks/`). Dependencies are now managed with [uv](https://docs.astral.sh/uv/) — run `uv sync` to reproduce the locked environment. See "Using the code" below.

============================================================


## Deep Plastic 
- Enhanced Object Detection for Epipelagic Plastic.
- This repository contains source code for the method developed in [DeepPlastic: Identifying Marine Plastic In The Epipelagic Zone using Computer Vision and Deep Learning](https://arxiv.org/abs/2105.01882)

![Inference Test](https://media.giphy.com/media/KCglrSW1FKhkNS6B5G/giphy.gif)

### Information:
- Paper: https://arxiv.org/abs/2105.01882
- Ultralytics case study: https://www.ultralytics.com/blog/case-study-deepplastic-and-yolov5
- YouTube video of Results: https://youtu.be/8zBdFxaK4Os
- Data: [Google Drive](https://drive.google.com/drive/folders/1fsS_u2QpbRGynYkP6-D6cfvq8r0hpjXI?usp=sharing)


### Object Detection Model
- Two models: YOLOv4 and YOLOv5 
- Small efficient and high precision models can be used for real-time object detection.
- Model architecture and implementation details: https://arxiv.org/abs/2105.01882
- Weights for YOLOv4 and YOLOv5 are provided in the model/
	- YOLOv4: best.weights; use [best.weights](https://drive.google.com/file/d/1YOTtZ2cHbqgxHukzLp01OVsUoa2CwwXs/view?usp=sharing)
	- YOLOv5: best.pt; use [best.pt](https://drive.google.com/file/d/14mBOhtLrE2d3hudqjwBZmawKAvTF4zxS/view?usp=sharing)

#### Google Colab Links

#### Note: Click on File and Save Copy in Drive. If you try to edit my file it'll ask you for permissions and send me an email. Please make your own copy.

- YOLOv5: https://colab.research.google.com/drive/1_qzbpBWkNfxQ0ny-DvsKicCeM0aFU4eW?usp=sharing

### DeepTrash DataSet
- 1900 training images, 637 test images, 637 validation images (60, 20, 20 split) 
- Field images taken from Lake Tahoe, San Francisco Bay and Bodega Bay in CA.
- Internet images (<20%) taken by scraping Google Images.
- Deep Sea images are from JAMSTEK JEDI dataset: http://www.godac.jamstec.go.jp/
- Complete DeepTrash dataset can be downloaded from: [Google Drive](https://drive.google.com/drive/folders/1fsS_u2QpbRGynYkP6-D6cfvq8r0hpjXI?usp=sharing)


### Using the code

The original Colab notebooks live in `notebooks/`. The same workflows are available as a Python package:

```
src/deepplastic/
├── utils.py      # shared helpers (image display, file utilities)
├── dataset.py    # dataset download + darknet-format preparation
├── yolov4.py     # darknet-based YOLOv4-tiny training/inference
├── yolov5.py     # ultralytics/yolov5-based training/inference
└── templates/    # the model config templates from the notebooks
```

Install with [uv](https://docs.astral.sh/uv/) (`uv sync`), then for example:

```python
from deepplastic import dataset, yolov4

darknet_dir = yolov4.build_darknet()            # requires CUDA + OpenCV
dataset.download_and_extract("<roboflow export url>")
dataset.prepare_darknet_dataset(".", darknet_dir)
yolov4.write_config(darknet_dir, num_classes=1)
yolov4.train(darknet_dir, yolov4.download_pretrained_weights(darknet_dir), clear=True)
```

```python
from deepplastic import yolov5

repo = yolov5.clone_yolov5()
nc = yolov5.num_classes_from_data_yaml("data.yaml")
yolov5.write_model_config(repo, num_classes=nc)
yolov5.train(repo, "data.yaml", weights="")     # '' = from scratch
yolov5.detect(repo, weights="best.pt", source="test/images")
```

Note: training itself still needs a CUDA GPU, and the YOLOv5 wrapper targets the 2021-era ultralytics/yolov5 scripts the paper used.

### Results
![Results from Inference](https://github.com/gautamtata/DeepPlastic/blob/master/results.png)


#### Bibliography entry:
	
	@misc{tata2021deepplastic,
      title={DeepPlastic: A Novel Approach to Detecting Epipelagic Bound Plastic Using Deep Visual Models}, 
      author={Gautam Tata and Sarah-Jeanne Royer and Olivier Poirion and Jay Lowe},
      year={2021},
      eprint={2105.01882},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
	}

[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)


Feeling Generous? Support our cause on Paypal

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/GautamTata?locale.x=en_US)

