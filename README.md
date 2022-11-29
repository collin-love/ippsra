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
  - [Change log](#change-log)


### Usage
- This repo is intended to be used from the main directory for this repo ie.
  ```cd ~./ippsra``` then run all commands 
  ```python src/ippsra/rank_images.py``` for example.
- Below is the output from the help argument for the ranking_images.py
<details>
  <summary>Help Output for rank_images.py</summary>
  <br>

```
usage: rank_images.py [-h] [--Directory DIRECTORY]
                      [--Extension {bmp,dib,jpeg,jpg,png,webp,pbm,pgm,ppm,pxm,pnm,sr,ras,tiff,tif,exr,hdr,pic}]
                      [--csvPath CSVPATH] [--csvName CSVNAME] [--save {True,False}]
                      [--imgIdx IMGIDX] [--showImages {True,False}] [--plot {True,False}]

Code for ranking a directory of images on a custom scale that is defined at this following
link https://github.com/collin-love/ippsra/blob/main/README.md

options:
  -h, --help            show this help message and exit
  --Directory DIRECTORY, -D DIRECTORY
                        The PATH to the directory containing the images that are going to be
                        processed (default: ./data/test_data)
  --Extension {bmp,dib,jpeg,jpg,png,webp,pbm,pgm,ppm,pxm,pnm,sr,ras,tiff,tif,exr,hdr,pic}, -ext {bmp,dib,jpeg,jpg,png,webp,pbm,pgm,ppm,pxm,pnm,sr,ras,tiff,tif,exr,hdr,pic}
                        A list of the extensions for the image data that is present in the
                        directory for processing (default: png)
  --csvPath CSVPATH     The PATH to the directory where the CSV file will be saved (default:
                        ./data/processed_data)
  --csvName CSVNAME     Then name of the CSV file that will be created (default:
                        sorted_test.csv)
  --save {True,False}   Boolean for if you want to save the files (default: False)
  --imgIdx IMGIDX       The index of the image that you want to show at the end of the
                        script from a sorted list of images from best to worst. The default
                        is 1 (the best ranked image) (default: 1)
  --showImages {True,False}
                        Boolean for if you want to show images (default: True)
  --plot {True,False}   Boolean for if you want to plot the data (default: True)
```
</details>

### Installation / Setup
- Clone this repository and cd into it
    ```
    git clone https://github.com/collin-love/ippsra.git
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
- For an update to this already created environment from the environment 
  file -- run
  ```
  conda activate ippsra
  conda env update --file environment.yml --prune
  ```
### Example
- The images that are used to test are in the data/test directory. This subset
  of data is a good representation of many cases of normal and outlier images
- Once everything is set up in the repository, the following line can be ran
  from the home directory for the project.
```
python src/ippsra/rank_images.py
```
- The output in the terminal will look like the following and some images will
  be displayed on the screen
<details>
  <summary>The default Terminal Output</summary>
  <br>

```
There are 43 images in this dir
0 images have been ranked
20 images have been ranked
40 images have been ranked
```
</details>
<center><img src="/docs/img/scatter.png" width="100%"/></center>

<center><img src="/docs/img/violin.png" width="100%"/></center>

- This first lunar image is the best image from the ranking
<center><img src="/docs/img/BestLunar.png" width="100%"/></center>

- This second lunar image is the best image from the ranking
<center><img src="/docs/img/WorstLunar.png" width="100%"/></center>

- User defined image showing
<center><img src="/docs/img/originalImage.png" width="100%"/></center>

- A compilation of the top images from each category
<center><img src="/docs/img/compilation.png" width="100%"/></center>


- These *params* can be varied
```
--save {True,False}   Boolean for if you want to save the files (default: False)
  --imgIdx IMGIDX       The index of the image that you want to show at the end of the
                        script from a sorted list of images from best to worst. The
                        default is 1 (the best ranked image) (default: 1)
```
- By specifying True when running 
  ```python src/ippsra/rank_images.py --save True``` a CSV file with the name
  --csvName of the rankings will be provided to the --csvPath directory
- For the defaults this command will create and populate two csv files in 
  this "**./data/processed_data/**" directory called "**sorted_test.csv**" and
  "**raw_data.csv**"
- Also, specifying True or False for saving, plotting, and showing images will
  either do the specified thing or not
- To check this csv the output will look like below
<details>
  <summary>The default Terminal Output</summary>
  <br>

- For sorted_test.csv
```
Image Name,Number of Hazards,Density of Hazards,Hazard Score
test_01.png,6,0.0,1
test_023.png,11,0.0,1
test_034.png,6,0.0,1
test_039.png,3,0.0,1
test_02.png,7,0.0,1
test_027.png,3,0.0,1
test_032.png,2,0.0,1
test_019.png,14,0.0,1
test_041.png,11,0.0,1
test_03.png,10,0.0,1
test_018.png,25,0.01,1
test_05.png,34,0.01,1
test_033.png,24,0.01,1
test_024.png,24,0.01,1
test_040.png,85,0.02,1
test_031.png,28,0.02,1
test_06.png,65,0.02,1
test_07.png,56,0.02,1
test_025.png,9,0.02,1
test_016.png,70,0.02,1
test_030.png,46,0.03,1
test_022.png,35,0.03,1
test_026.png,44,0.03,1
test_04.png,22,0.03,1
test_011.png,121,0.03,1
test_038.png,29,0.04,1
test_020.png,39,0.05,1
test_036.png,32,0.05,1
test_037.png,91,0.07,2
test_029.png,95,0.07,2
test_08.png,1717,0.07,2
test_042.png,127,0.08,2
test_013.png,311,0.08,2
test_021.png,93,0.09,2
test_010.png,343,0.1,2
test_017.png,207,0.14,3
test_043.png,129,0.14,3
test_035.png,223,0.18,3
test_015.png,793,0.19,3
test_012.png,872,0.23,3
test_014.png,976,0.24,3
test_028.png,333,0.34,3
test_09.png,1312,0.41,3
```
- For raw_data.csv
```
Image Name,Number of Hazards,Density of Hazards,Hazard Score
test_01.png,6,0.0,1
test_010.png,343,0.1,2
test_011.png,121,0.03,1
test_012.png,872,0.23,3
test_013.png,311,0.08,2
test_014.png,976,0.24,3
test_015.png,793,0.19,3
test_016.png,70,0.02,1
test_017.png,207,0.14,3
test_018.png,25,0.01,1
test_019.png,14,0.0,1
test_02.png,7,0.0,1
test_020.png,39,0.05,1
test_021.png,93,0.09,2
test_022.png,35,0.03,1
test_023.png,11,0.0,1
test_024.png,24,0.01,1
test_025.png,9,0.02,1
test_026.png,44,0.03,1
test_027.png,3,0.0,1
test_028.png,333,0.34,3
test_029.png,95,0.07,2
test_03.png,10,0.0,1
test_030.png,46,0.03,1
test_031.png,28,0.02,1
test_032.png,2,0.0,1
test_033.png,24,0.01,1
test_034.png,6,0.0,1
test_035.png,223,0.18,3
test_036.png,32,0.05,1
test_037.png,91,0.07,2
test_038.png,29,0.04,1
test_039.png,3,0.0,1
test_04.png,22,0.03,1
test_040.png,85,0.02,1
test_041.png,11,0.0,1
test_042.png,127,0.08,2
test_043.png,129,0.14,3
test_05.png,34,0.01,1
test_06.png,65,0.02,1
test_07.png,56,0.02,1
test_08.png,1717,0.07,2
test_09.png,1312,0.41,3
```

</details>

<!-- ### Example for running new unit and functional test 
- 
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

</details> -->


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
