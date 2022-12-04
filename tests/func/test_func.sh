set -u
set -o pipefail
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_stdout python src/ippsra/rank_images.py --save False --showPlots False --showImages False
assert_stdout

run test_in_stdout python src/ippsra/rank_images.py --save False --showPlots False --showImages False
assert_in_stdout "There are 41 images in this dir"

run test_in_stderr python src/ippsra/rank_images.py --save  --showPlots --showImages
assert_in_stderr "usage: rank_images.py [-h] [--Directory DIRECTORY]"

run test_stdout python src/ippsra/rank_images.py --save True --showPlots False --showImages False
assert_exit_code 0

run test_in_stderr python src/ippsra/rank_images.py --save True --showPlots False  --showImages False
assert_in_stderr "OSError: (OSError): The file sorted_test.csv already exists in the directory ./data/processed_data. Please move or delete the file and try again"

# Checking if the files were created and if they were deleted
if [[ -e data/processed_data/raw_data.csv ]] && [[ -e data/processed_data/sorted_test.csv ]]; then
    rm ./data/processed_data/raw_data.csv
    rm ./data/processed_data/sorted_test.csv
fi

for f in data/processed_data/*.png
do
    if [[ -e $f ]]; then
        rm $f
    fi
done

for f in data/processed_data/*.csv
do
    if [[ -f $f ]]; then
        echo "File $f does exist"; else echo "Files $f do not exist they were deleted"
    fi
done

for f in data/processed_data/*.png
do
    if [[ -f $f ]]; then
        echo "File $f does exist"; else echo "Files $f do not exist they were deleted"
    fi
done


run test_in_stderr python src/ippsra/rank_images.py --save False --showPlots False --showImages False --Directory ./data/FAKE_Directory
assert_in_stderr "No such file or directory: './data/FAKE_Directory'"

mkdir ./data/EMPTY_Directory

run test_in_stderr python src/ippsra/rank_images.py --save False --showPlots False --showImages False --Directory ./data/EMPTY_Directory
assert_in_stderr "The directory ./data/EMPTY_Directory is empty"

rm -r ./data/EMPTY_Directory
