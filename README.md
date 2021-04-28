# Identifying Marine Plastic using Deep Learning and Computer Vision

[![IMAGE ALT TEXT](http://img.youtube.com/vi/rlgrTBghAYQ/0.jpg)](https://www.youtube.com/watch?v=rlgrTBghAYQ "Video Title")


This repository is the official implementation of [Detecting Marine Plastic In The Epipelagic Zone using Computer Vision and Deep Learning](https://arxiv.org/abs/2030.12345). 

>📋  Optional: include a graphic explaining your approach/main result, bibtex entry, link to demos, blog posts and tutorials

## Abstract and Motivation

Quantifying  and  removing  plastic  in  the  epipelagiczone  is  one  of  the  most  pressing  problems  of  our  generation.There  is  an  urgent  need  for  resources  to  mitigate  the  impactof  plastic  pollution  on  the  environment.  Current  methods  ofidentification  and  removal  are  mostly  labor  and  cost-intensive.This  problem  results  in  limited  scalability  to  areas  with  fewresources.  In  this  paper,  we  introduce  an  automated  systemfor  identifying  marine  plastic.  We  identify  plastic  debris  foundunderneath  the  ocean  surface  using  deep  learning  models  alongwith  computer  vision.  The  following  Deep  Learning  models  arecompared  in  this  paper:  YOLOv4-Tiny  and  YOLOv5-S.  Wepresent  a  model  architecture,  pre-processing,  post-processing,data augmentation steps, and inference speed on a GPU for eachmodel.  The  best  performing  model  was  the  YOLOv5  with  anmAP of 0.756 and F1-Score of 0.701. Our results show that deeplearning models can be used to identify plastic with high accuracyand can be used alongside AUVs to quantify and remove marine-plastic.

## Quick use: Google Colab Links

1. [YOLOv5 Colab]()
2. [YOLOv4 Colab]()



## Training

To train the model(s) in the paper, run this command:

Clone the following repositories: [YOLOv5-Pytorch](https://github.com/ultralytics/yolov5) & [YOLOv4-Darknet](https://github.com/AlexeyAB/darknet)

Follow the instructions in the repositories to setup the environment.

```train YOLOv5
python train.py --data data.yaml --cfg yolov5s.yaml --weights /path/to/pretrained/weights --batch-size 64
```

```train yolov4
!./darknet detector train /path/to/data/file /path/to/cfg/file /path/to/pretrained/weights -dont_show -map -clear
```



>📋  Link to ipynb files to train/evaluate the model.

## Inference

To run inference on the models, run the following commands

```Inference YOLOv5
%cd /content/yolov5/
!python detect.py --weights /path/to/weights --img 416 --conf 0.1 --source /path/to/image
```

```Inference YOLOv4
!./darknet detector test data/obj.data /path/to/config/file /path/to/weights /path/to/image
imShow('predictions.jpg')
```

>📋  Describe how to evaluate the trained models on benchmarks reported in the paper, give commands that produce the results (section below).

## Pre-trained Models

You can download pretrained models here:

- [YOLOv5 Pretrained Weights](https://drive.google.com/mymodel.pth) 
- [YOLOv4 Pretrained Weights](https://drive.google.com/mymodel.pth)


## Results

Our model achieves the following performance on :

### [Image Classification on ImageNet](https://paperswithcode.com/sota/image-classification-on-imagenet)

| Model name | mAP  | F1-Score |
| ---------- | ---- | -------- |
| YOLOv5     | 75%  | 71       |
| YOLOv4     | 68%  | 69       |

>📋  Include a table of results from your paper, and link back to the leaderboard for clarity and context. If your main result is a figure, include that figure and link to the command or notebook to reproduce it. 

## Inference Results

//Images and videos

## Contributing

>📋  Pick a licence and describe how to contribute to your code repository. 
