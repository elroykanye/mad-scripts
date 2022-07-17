#!/usr/bin/env bash

SUFFIX=$0
SUFFIX=${SUFFIX##*/}
echo "SUFFIX: $SUFFIX"
function eval_error_extract() {

  FILE="$1"
  RESULT_FILE="$2"

  # reset prefix
  KEY_PREFIX="$3_"
  # remove the .java extension
  FILENAME=${FILE%.java}
  #extract basename
  BASENAME=${FILENAME##*/}
  # convert basename to lowercase with underscore
  KEY_NAME=$(echo $BASENAME | tr '[:upper:]' '[:lower:]' | tr '-' '_')
  KEY_NAME="$KEY_PREFIX$KEY_NAME"
  KEY_VALUE=""

  if [ ! -f "$FILE" ]; then
      echo "File not found: $FILE"
      exit 1
  else
  	python3 eod.py $KEY_NAME $FILE $RESULT_FILE
  fi
}


FOLDER=$1

RESULT_FILE=$(basename $FOLDER)_$SUFFIX.txt

PREFIX=""
BNAME=$(basename $FOLDER)
# get first 3 characters of the folder name
if [ -n "$FOLDER" ]; then
  PREFIX=${BNAME:0:3}
else
  PREFIX=$BNAME
fi

# Check if folder is empty
if [ -z "$FOLDER" ]; then
    echo "Usage: fde.sh <folder>"
    exit 1
fi

if [ -f "$RESULT_FILE" ]; then
    echo "File already exists: $RESULT_FILE"
    # ask to delete
    read -p "Delete file? (y/n) " -n 1 -r
    echo   # (optional) move to a new line
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm $RESULT_FILE
    fi
fi

# loop through all files in folder
for file in $FOLDER/*; do
  # check if file is a directory
  if [ -d "$file" ]; then
    # if it is, recurse into it
    ./eee.sh $file
  else
    # if it is not, check if it is a java file
    if [[ $file == *.java ]]; then
      # if it is, run the checker
      eval_error_extract $file $RESULT_FILE $PREFIX
    fi
  fi
done





