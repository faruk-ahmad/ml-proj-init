# ML-PROJ-INIT
----------------------------------------------

#### A lightweight tool to create machine learning project structure and add neaty code snipt quickly to your project

-----------------------------------------------


<p align= "justify">
  
__ml-proj-init__ is a python package to help you to do your machine learning experiment in python in a faster way by creating well defined project structure just by a few commands that works out of the box for most of the machine learning projects. You can focus on building the solution of your problem rather writing all the basic stuffs that are tedious but can be added to your project easily and in a faster way.
</p>

--------------------------------------------------


## 2. Installation

### 2.1 Install in Linux, MacOS and Windows

The installation process is OS independent. If you have a working python 3.5 or newer version in your computer and pip3 as the package manager, you can easilty install the package just by following instructions.

#### 2.1.0 Dependency

* <b>Python 3.x</b>

#### 2.1.1 Installation

* Install using the following command-

```bash
pip install ml-proj-init
```


#### 2.1.2 Uninstallation

* Uninstall using the following command

```bash
pip uninstall ml-proj-init
```

* Provide "y" if you are prompt for approval to remove some config files.

--------------------------------------------------

See more info here:
[ml-proj-init in pypi.org](https://pypi.org/project/ml-proj-init/)

## 4. Getting Started



ML-PROJ-INIT has two mode

1. Create structure mode
2. Add class/code snipt mode


#### 4.1 Creating project structure

------------------------------------------------------

In create mode, you can create a well defined project structure for your machine learning or deep learning project by passing few arguments. The create structure mode supports the following parameters - 

#### Creation mode parameters:

| Parameter | Accepted Values | Format | Usage | Default Values |
|--------------|--------------------|----------|---------------|---------------------|
| ```-m```  or  ```--mode``` | ```c``` | ```-m=c```  or  ``` --mode=c```  or ```-m c```  or  ``` --mode c``` | c for creating structure | Required, no default |
| ```-n```  or  ```--name``` | string, a valid project name | ```-n=proj_name``` or ```--name=proj_name``` or ```-n proj_name``` or ```--name proj_name``` | Provide the project name | Required, no default |
| ```-p``` or ```--path``` | string, a valid path | ```-p path``` or ```--path path``` | Path to create the project | Optional, if not given use the current working directory as the path |
| ```-t``` or ```--type``` |  ```ml``` or ```dl``` | ```-t=ml``` or ```--type=ml``` or ```-t dl``` or ```--type dl``` | project type to create ml project or dl project structure | Optional, if not given use "ml" as the default value |


#### Example:
-----------------------------------------------------
To create project strucure for a project named ```hello-world``` in ```/home/user/Desktop/``` location and if the project type is ```deep learning``` , then run the following command - 

```bash
ml-proj-init -m=c -n=hello-world -p=/home/user/Desktop/ -t=dl
```

or

```bash
ml-proj-init -m c -n hello-world -p /home/user/Desktop/ -t dl
```

-----------------------------------------------------

#### 4.2 Appending class/code snipt

-------------------------------------------------------------------------

In append mode, you can easily generate required class implementation or code snipt for loading different data source or building few common machine learning or deep learning model architecture.

#### Append mode parameters:

| Parameter | Accepted Values | Format | Usage | Default Values |
|--------------|--------------------|----------|---------------|---------------------|
| ```-m```  or  ```--mode``` | ```a``` | ```-m=a```  or  ``` --mode=a```  or ```-m a```  or  ``` --mode a``` | a for appending required class or code snipt | Required, no default |
| ```-p``` or ```--path``` | string, a valid path | ```-p path``` or ```--path path``` | Path to create the project | Optional, if not given use the current working directory as the path |
| ```-l``` or ```--loader``` | ```img``` or ```text``` or ```csv``` | ```-l=img``` or ```--loader=img``` or ```-l text``` or ```--loader csv``` | Data loader type to generate instant code snipt | Optional, no default |
| ```-net``` or ```--network``` | ```cnn``` or ```lstm``` or ```nn``` | ```-net=cnn``` or ```--network=lstm``` or ```-net nn``` | Network type to generate code snipt for common architecture | Optional, no default |


#### Example:
-----------------------------------------------------
To add a data loader for ```image``` type data and or a simple ```cnn``` architecture to classify the image run the following command-

```bash
ml-proj-init -m=a -l=img -net=cnn -p=/home/user/Desktop/
```

or

```bash
ml-proj-init -m a -l img -net cnn -p /home/user/Desktop/
```
--------------------------------------------------------------------------

## 5. Features
--------------------------------------------------

#### 5.1 Features avaiable

* Creating machine learning project structure based on popular ml library scikit-learn and others.
* Creating deep learning project structure using popular dl library tensorflow, keras and others.
* Adding necessary code snipts for data loader class like image data loader or text data loader.
* Adding different neural network implementation skeleton in popular deep learning library TF/KERAS.

#### 5.2 Features in Queue

* Adding frequently used data vizualization code snipts
* Adding feature to generate quick documentation for project, like tables, visualizations etc.
* Adding more frequently used implementation for quick experiment
* Adding more implementatioin of NN architecture for experiment
* Adding more flexible and dynamic code snipt generation.

## 6. Report Issues

--------------------------------------------------
Before you report an issue in github, please make sure you are in the same pace with the up to date commit in our github repo and the latest release from pypi. 


## 7. How to Contribute

--------------------------------------------------

You can contribute in the one or either way of the following-

#### 7.1 Bug Reporting
	-- You can report a bug by adding issue in github
	-- Or you can contribute by sharing how you solved an issue

#### 7.2 Requesting a Feature
	-- If you came accross any new idea that can be added as feature

#### 7.3 Adding Feature, Pull Request
	-- If you come with new idea of a feature and add it
	-- Send us pull request

#### 7.4 Adding Nofification Resource
	-- Adding latest neural network architecture to make available for use
	-- Adding more frequently used code snipt for machine learning and deep learning project.
