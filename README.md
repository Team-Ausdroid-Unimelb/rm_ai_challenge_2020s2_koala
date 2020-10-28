# RoboMaster AI Challenge (2.0.0)

## Table of contents

* [Introduction](#introduction)
* [Sample Input Image](#sample-input-image)
* [System Components](#system-components)
* [User Stories](#user-stories)
* [Change Log](#change-logs)
* [Test Cases](#test-cases)
* [User Guide](#user-guide)

## Introduction

This project is to enhance the capabilities of the robot to be competitive in the [RoboMaster AI Challenge](https://www.robomaster.com/en-US/robo/icra). The two main objectives are to enable the robot to locate and identify different types of enemies' armour in the images captured by our robot's camera and the outpost camera. 

According to the [rules of the competition](https://www.robomaster.com/en-US/resource/pages/announcement/1039), robots shoot at enemy robots' armour to score points. Robots score different points depending on which enemy robots' armour they hit: front, side or back. Therefore, granting our robot the capabilities of locating and identifying enemies' armour automatically will significantly increase the chance of winning in the competition. After implementing the two algorithms, An interface displaying the outcome of location and identification will be created to examine the performance of the algorithms. 

## Sample Input Image
### unlabelled image
![Unlabelled image](src/images/sample_unlabeled_image.png)

### unlabelled image (updated for sprint2)
![Unlabelled image](/multiple_colours.png)

### labelled image
![Labelled image](src/images/sample_labelled_image.png)

### labelled image (updated for sprint2)
![labelled image](/prediction.jpg)

## System Components

[YOLO](https://pjreddie.com/darknet/yolo/) (You only look once) is used for both the armour location and identification algorithms. It's a state-of-the-art real-time object detection system, which can process images fast and achieve a high mAP. [CVAT](https://github.com/openvinotoolkit/cvat) is used for labelling images, and Google Colab is used for training. 

## User Stories
### Product Backlog (https://github.com/cchia790411/rm_ai_challenge_2020s2_koala/blob/master/docs/RM-Koala%20Product%20Backlog%20v1.1.pdf)

### Sprint 1 (https://github.com/cchia790411/rm_ai_challenge_2020s2_koala/blob/master/docs/Sprint%201/RM-Koala%20Sprin%201%20Output.pdf)
  1. [US1] locate the opponent robot’s armour in the pictures
  2. [US2] recognize the type of the armour pad the enemy is showing
  
### Sprint 2 (https://github.com/cchia790411/rm_ai_challenge_2020s2_koala/blob/master/docs/Sprint%202/RM-Koala%20Sprint%202%20Planning%20v1.0.pdf)
  1. [US3] to have GUI of softrware to use/evaluate computer vision algorithm more easily 
  2. [US4] to make armour location and armour identification algorithms work in conjunction to make product works faster
  3. [US7] to make product locate multiple armours in the image
  4. [US8] to make product identify types of multiple armours located in the input
  
## Change Logs
## [Released] 
## [v1.0]
### Added
#### Commits on Sep 9
- Update README.md @af-kurniawan

#### Commits on Sep 14, 2020
- Add resource @cchia790411
- Compress dataset @cchia790411

#### Commits on Sep 15, 2020
- Add colab notebook @cchia790411
- Update README.md @cchia790411

#### Commits on Sep 18, 2020
- add files via upload @cchia790411

#### Commits on Sep 24, 2020
- added readme file @Jia Yin
- updated README @jiaywill
- update image paths @jiaywill

#### Commits on Sep 25, 2020
- update notebook
- Add trained weight and update notebook
- update user guide

- Add: red1 200-249 labelled images. @isaacpedroza 

### changed
#### Commits on Sep 18, 2020
- Merge branch 'dev' of https://github.com/cchia790411/rm_ai_challenge_… @cchia790411
- notebook modified @cchia790411

#### commits on Sep 25, 2020
- Refonfigurate for 2 separate model (armour/pose) 
- Merge branch 'develop' of https://github.com/cchia790411/rm_ai_challe…

#### Commits on Sep 26, 2020
- Delete: requirements.txt not needed anymore @isaacpedroza 
#### Commits on Sep 27, 2020
- Merge branch 'feature/us1_us2' into develop @isaacpedroza
- Merge branch 'develop' into master @ isaacpedorza

## [v1.1]
### Added 
#### Commits on Sep 28, 2020
- @isaacpedroza Update README.md
- @isaacpedroza Update README.md

#### Commits on Sep 29, 2020
- @cchia790411 Reconfig network structure & update latest training result
- @cchia790411 Merge pull request #5 from cchia790411/develop … Reconfig network structure & update latest training result
- @cchia790411 Add Sprint 1 product notebook
- @cchia790411 Merge pull request #6 from cchia790411/develop … Add Sprint 1 product notebook
- @s-kim333 s-kim333 released release tag v1.1 29 Sep 

## [v1.2]
### Added
#### Commits 
- @cchia790411 Add test cases
- @cchia790411
- Merge pull request #7 from cchia790411/develop

## Test Cases
### Sprint 1
- test case document for sprint 1 (https://github.com/cchia790411/rm_ai_challenge_2020s2_koala/blob/master/docs/Sprint%201/RM-Koala%20Testing%20Document.pdf)
### Sprint 2 
- test case document for sprint 2 (https://github.com/cchia790411/rm_ai_challenge_2020s2_koala/blob/master/docs/Sprint%202/COMP900822020SM2RMKoala-TestingDocument-Sprint2-291020-0234-2394.pdf)

## Traceability matrix
![traceability matrix](https://user-images.githubusercontent.com/64014524/97461413-1775be00-1981-11eb-9e81-ea2dc05d2d84.PNG)

## User Guide (Release v1.2)
1. Sign in to Google Colab using a Google account (https://colab.research.google.com/)
2. Upload the notebook to Google Colab 
  ``` notebook location: rm_ai_challenge_2020s2_koala/build/colab_notebook/RM_Koala_YOLO_approach.ipynb ```
3. Run all the cells.
4. Scroll down to the bottom of the notebook to view results.
## User Guide (Release 2.0.0)
