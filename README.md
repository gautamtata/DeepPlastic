[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deepplastic-a-novel-approach-to-detecting/object-detection-on-deeptrash)](https://paperswithcode.com/sota/object-detection-on-deeptrash?p=deepplastic-a-novel-approach-to-detecting)

### Deep Plastic 
- Enhanced Object Detection for Epipelagic Plastic.
- This repository contains source code for the method developed in [DeepPlastic: Identifying Marine Plastic In The Epipelagic Zone using Computer Vision and Deep Learning](https://arxiv.org/pdf/2105.01882.pdf)

![Inference Test](https://media.giphy.com/media/KCglrSW1FKhkNS6B5G/giphy.gif)

### Information:
- Paper: [Coming Soon]
- Preprint: https://arxiv.org/
- YouTube video of Results: https://youtu.be/8zBdFxaK4Os
- Data: [Google Drive](https://drive.google.com/drive/folders/1fsS_u2QpbRGynYkP6-D6cfvq8r0hpjXI?usp=sharing)


### Object Detection Model
- Two models: YOLOv4 and YOLOv5 
- Small efficient and high precision models can be used for real-time object detection.
- Model architecture and implementation details: https://arxiv.org/
- Weights for YOLOv4 and YOLOv5 are provided in the model/
	- YOLOv4: best.weights; use [best.weights](https://drive.google.com/file/d/1YOTtZ2cHbqgxHukzLp01OVsUoa2CwwXs/view?usp=sharing)
	- YOLOv5: best.pt; use [best.pt](https://drive.google.com/file/d/14mBOhtLrE2d3hudqjwBZmawKAvTF4zxS/view?usp=sharing)

#### Google Colab Links

#### Note: Click on File and Save Copy in Drive. If you try to edit my file it'll ask you for permissions and send me an email. Please make your own copy.

- YOLOv5: [![YOLOv5](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gautamtata/DeepPlastic/blob/master/DeepTrash_Yolov5.ipynb)
- 
### DeepTrash DataSet
- 1900 training images, 637 test images, 637 validation images (60, 20, 20 split) 
- Field images taken from Lake Tahoe, San Francisco Bay and Bodega Bay in CA.
- Internet images (<20%) taken by scraping Google Images.
- Deep Sea images are from JAMSTEK JEDI dataset: http://www.godac.jamstec.go.jp/
- Complete DeepTrash dataset can be downloaded from: [Google Drive](https://drive.google.com/drive/folders/1fsS_u2QpbRGynYkP6-D6cfvq8r0hpjXI?usp=sharing)


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

