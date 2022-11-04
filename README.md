![](https://github.com/collin-love/ippsra/blob/main/docs/img/examples/welcome.gif)

## ippsra
> Image Processing Pipeline for Space Robotic Applications

### Table of Contents

- [ippsra](#ippsra)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
  - [Installation / Setup](#installation--setup)
  - [Environment Setup](#environment-setup)
  - [Example](#example)
  - [Example for running new unit and functional test](#example-for-running-new-unit-and-functional-test)
  - [Change log](#change-log)


### Usage
- The default for this project at the moment for the path is "./data/images/
 render/render9327.png"
<details>
  <summary>Help Output</summary>
  <br>

```
usage: bounding.py [-h] [--input INPUT]

Code for Creating Bounding boxes and circles for contours tutorial.

options:
  -h, --help     show this help message and exit
  --input INPUT  Path to input image.
```
</details>

### Installation / Setup
- Clone this repository and cd into it
    ```
    git clone git@github.com:collin-love/ippsra.git
    ```
    ```
    cd ippsra
    ```

### Environment Setup
- ENV setup for this project below
    ```
    conda env create -f environment.yml
    conda activate ippsra
    ```
- Once the environment is created the following terminal commands can be ran

<!-- #### Data Installation
- To install the data do *whatever*
    ```
    wget 
    ```
- To install data do *whatever*
    
    ``` -->

### Example
- The images that ares used to test are in the data/test directory. This subset
  of data is a good representation of many cases of normal and outlier images
- Once everything is set up in the repository, the following line can be ran
 from the home directory for the project.
```
python src/ippsra/bounding.py
```
- The output in the terminal will look like the following

<details>
  <summary>Terminal Output</summary>
  <br>

```
```
<center><img src="/docs/img/bounding_output.png" width="100%"/></center>

</details>

<!-- - These *params* can be varied by *X* -->

### Example for running new unit and functional test 
- To run all of the new function and unit test simply paste this line in your
  terminal from the home directory for the project.
```
for linux systems 
cd ~/ippsra
python -m unittest tests/unit/test_utils.py
```
- The output should like the below block of text. (these are testing CI, so
  they don't mean anything at the moment)

<details>
  <summary> Unit Test Terminal Output</summary>
  <br>

```
Height = 480,  Width = 720
this Utils ran
this tes_utils ran

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
```
</details>

```
for linux systems 
cd ~/ippsra
bash tests/func/test_func.sh
```
- The output should like the below block of text. (these are testing CI, so
  they don't mean anything at the moment)

<details>
  <summary> Function Test Terminal Output</summary>
  <br>

```
this func ran
```

</details>


<!-- ### Example with a *specific variation* specified 
- Once everything is setup in the repository, the following line can be ran 
```
for linux systems 
cd ~/ippsra
bash tests/unit/unittest.sh
```
- The output in the terminal will look like the following

<details>
  <summary>Terminal Output</summary>
  <br>

```
```
<center><img src="/docs/img/Thenvsnow.jpeg" width="100%"/></center>

</details> -->

### Change log
- v1.0
  - This version contains *X*
