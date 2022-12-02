set -u
set -o pipefail
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_stdout python src/ippsra/rank_images.py --save False --showPlot False --showImages False
assert_stdout

run test_in_stdout python src/ippsra/rank_images.py --save False --showPlot False --showImages False
assert_in_stdout "There are 43 images in this dir"

run test_in_stderr python src/ippsra/rank_images.py --save  --showPlot --showImages
assert_in_stderr "usage: rank_images.py [-h] [--Directory DIRECTORY]"

run test_stdout python src/ippsra/rank_images.py --save True --showPlot False --showImages False
assert_exit_code 0

run test_in_stderr python src/ippsra/rank_images.py --save True --showPlot False  --showImages False
assert_in_stderr "OSError: (OSError): The file sorted_test.csv already exists in the directory ./data/processed_data. Please move or delete the file and try again"

rm ./data/processed_data/*.csv && rm ./data/processed_data/*.png

run test_in_stderr python src/ippsra/rank_images.py --save False --showPlot False --showImages False --Directory ./data/FAKE_Directory
assert_in_stderr "No such file or directory: './data/FAKE_Directory'"

mkdir ./data/EMPTY_Directory

run test_in_stderr python src/ippsra/rank_images.py --save False --showPlot False --showImages False --Directory ./data/EMPTY_Directory
assert_in_stderr "The directory ./data/EMPTY_Directory is empty"

rm -r ./data/EMPTY_Directory
