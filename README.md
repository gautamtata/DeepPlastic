
### Deep Plastic 
- Enhanced Object Detection for Epipelagic Plastic.
- This repository contains source code for the method developed in [DeepPlastic: Identifying Marine Plastic In The Epipelagic Zone using Computer Vision and Deep Learning](https://arxiv.org/)

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

- YOLOv4: [![YOLOv4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Naereen/badges) 

- YOLOv5: [![YOLOv5](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Naereen/badges) 

### DeepTrash DataSet
- 1900 training images, 637 test images, 637 validation images (60, 20, 20 split) 
- Field images taken from Lake Tahoe, San Francisco Bay and Bodega Bay in CA.
- Internet images (<20%) taken by scraping Google Images.
- Deep Sea images are from JAMSTEK JEDI dataset: http://www.godac.jamstec.go.jp/
- Complete DeepTrash dataset can be downloaded from: [Google Drive](https://drive.google.com/drive/folders/1fsS_u2QpbRGynYkP6-D6cfvq8r0hpjXI?usp=sharing)


### Results
![Results from Inference](https://github.com/gautamtata/DeepPlastic/blob/master/results.png)


#### Bibliography entry:
	
	@inproceedings{tata2021deepPlastic,
	    author={Tata, Gautam and Royer, Sarah and Lowe, Jay and Poirion, Olivier},
	   
	}

[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)

