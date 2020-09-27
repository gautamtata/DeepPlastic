# Deep Plastic: Detecting of marine plastic in the euphotic zone

## Abstract

The world has a plastic problem. Everyday, we dump millions of tons of trash in our oceans, rivers and lakes. A lot of these plastic are a bit more denser than water and tend to sink right below the surface of the water while the heaviest plastics can sink all the way down. While everything may look great at the surface, the reality of ocean plastic is quite deadly. Plastics interact with algae and phytoplankton to take away the majority of the food for marine dwellers all the while getting caught in their fins or slowly killing them after being lodged in their stomach. The plastic pandemic in our oceans needs a solution. In this project, I propose the use of Deep Learning models which can be incorported with robotics to clean up the plastic mess we have left in our oceans.

## Why the Euphotic Zone

TODO

## INTRODUCTION

Marine Debris poses an immense threat to the health of our planet. Plastic in the ocean not only effect marine animals but humans as well through consumption of sea food. Ocean Plastic has also been linked to Global warming (Sarah-Jeanne Royer paper) — Continue on about why this is bad. There is virtually no place on earth which is unaffected by marine debris which kills, injures and contaminates aquatic life in our oceans. I propose a Deep Learning model to be effectively be used by Robots and ROV's for detection, identification and extraction of marine plastic.

To be useful for the goal of removing those plastics and other trash, these object detection algorithms must be able to run in near real-time on our robotic platform. To gauge their readiness for such a deployment, we tested all of our networks and models on three different devices, approximating the capabilities of an offline data processing machine, a high-powered robotic platform, and a low-powered platform.

TLDR of paper contributions

- Evaluate the accuracy and performance of 3 state-of-the-art object detection algorithms for the purpose of detecting marine trash. Namely: Yolo v5, EfficientDet D5, FasterRCNN detectron2.
- Produce a dataset that best known to me is the first containing annotated images of just ocean plastic.
- Evaluate metric for a single model ie Yolo version 5.

## RELATED WORK

- University of Michigan robotics labs
- <TODO>

## CONSTRUCTING THE DATASET

We open sourced a dataset comprising of over 5000 images of *trash_plastic* in different environments, such as natural marine, synthetic swimming pools and in-air images.

DeepTrash is a dataset comprised of 4500 images of plastic. The dataset contains 80% of the images from underwater scenes and 20% of images from land-based plastic. The dataset is comprised of 1 class for plastic (trash-plastic). The dataset is sourced from natural environmental sources such asJ-EDI (JAMSTEC E-Library of Deep-Sea Images), Images taken from Lake Tahoe and Bodega Bay in California. The dataset also contains images from un-natural sources such as swimming pools. In-air images are collected from TrashVNOI, Google Open Images V6, TrashNet and images collected by annotating videos from YouTube, Unsplash API and ShutterStock. The goal of developing this dataset is to develop efficient and accurate trash detection methods suitable for robot deployment to clean up the plastic. DeepTrash is to the best of my knowledge the only dataset that contains such an extensive directory of images related to underwater plastic. It is my hope that the release of this dataset will further facilitate research on this challenging problem, bring the marine/environmental and computer science community closer to a solution for the much needed solution of autonomous trash detection and removal.  I am open sourcing this dataset in multiple formats such as COCO JSON, .TFRECORD and YOLO format to further make this dataset model agnostic and to faciliate research.

## Data Model

This trash detection model comprises of one class, defined as follows:

- trash_plastic: All plastic materials including but not limited to Bags, Bottles, Styrofoam, utensils etc.

The reason for using reduced number of classes: To improve inference speed as well as improve generality of the detector. Since there are many plastic objects that are present in our environment, they were generalized into one single class called *trash_plastic.*

Other models were tested which included multiple classes (such as ROV, types of fishes/mammals, scuba divers) but were rejected because of lower accuracy

*{write descriptions for each of the models, what kind of format they expect, convolutional layers,*

### Evaluation Models

To evaluate the models, test images which contained the classes from the dataset as well as external images sourced from Google Images, Unsplash were selected. The dataset was split into a 70% training set, 15% test set and 15% validation set. These images contained examples for each class in a variety of environments which were intentionally sected to provide a realistic valuation of of how these detectors would perform in real world field conditions.

### Network architectures

The three network architectures selected for this project were chosen from the most popular and state of the are object detection networks in use today. Each one has own benefits and drawbacks with varying level of accuracy and runtime speeds.

- [ ]  Build charts to show mAP and AP between those selected network architectures.
- Yolo v5
- EfficientDet D5
- FasterRCNN Detectron2

## Data preprocessing

- Images resized to 416x416
- Histogram Equalization (+ add description)
- Augmentation - Flipped Images + Random Crops + Increase/Decrease brightness

## Training

- Tesla V100 and Tesla P6000 — HARDWARE
- Google Colab — HARDWARE
- Xavier Initialization
- ADAM
- Dropouts
- Adaptive Learning Rates from big learning rates to small to fine tune
- Max Pooling
- Batch Normalization
- 1500-2500 Epochs
- Weight Regularization
- Overfitting a small batch

### REFERENCES

SPECIAL THANKS: Nikhil Dev Deshmudre for helping with everything Deep Learning

University of Minnesota Robotics: MD. Jahidul Islam and Michael Fulton

