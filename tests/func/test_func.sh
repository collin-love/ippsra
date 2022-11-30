set -u
set -o pipefail
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_stdout python3 src/ippsra/rank_images.py --save False --plot False --showImages False
assert_stdout

run test_in_stderr python3 src/ippsra/rank_images.py --save False --plot False --showImages False
assert_in_stdout "There are 43 images in this dir"

run test_in_stderr python3 src/ippsra/rank_images.py --save  --plot --showImages
assert_in_stderr "usage: rank_images.py [-h] [--Directory DIRECTORY]"

run test_stdout python3 src/ippsra/rank_images.py --save True --plot False --showImages False
assert_exit_code 0

run test_in_stderr python3 src/ippsra/rank_images.py --save True --plot False  --showImages False
assert_in_stderr "OSError: (OSError): The file sorted_test.csv already exists in the directory ./data/processed_data. Please move or delete the file and try again"

rm ./data/processed_data/sorted_test.csv
rm ./data/processed_data/raw_data.csv

run test_in_stderr python3 src/ippsra/rank_images.py --save False --plot False --showImages False --Directory ./data/FAKE_Directory
assert_in_stderr "No such file or directory: './data/FAKE_Directory'"

mkdir ./data/EMPTY_Directory

run test_in_stderr python3 src/ippsra/rank_images.py --save False --plot False --showImages False --Directory ./data/EMPTY_Directory
assert_in_stderr "The directory ./data/EMPTY_Directory is empty"

rm ./data/processed_data/sorted_test.csv
rm ./data/processed_data/raw_data.csv
rm -r ./data/EMPTY_Directory