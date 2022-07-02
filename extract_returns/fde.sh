#!/usr/bin/env bash


function return_extractor() {
  # extract method of a java class called getDescription()
  FILE="$1"
  RESULT_FILE="$2"

  # reset prefix
  KEY_PREFIX="$3_"
  # remove the .java extension
  FILENAME=${FILE%.java}
  #extract basename
  BASENAME=${FILENAME##*/}
  echo "Extracting method of class $BASENAME"
  # convert basename to lowercase with underscore
  KEY_NAME=$(echo $BASENAME | tr '[:upper:]' '[:lower:]' | tr '-' '_')
  KEY_NAME="$KEY_PREFIX$KEY_NAME"
  KEY_VALUE=""

  if [ ! -f "$FILE" ]; then
      echo "File not found: $FILE"
      exit 1
  fi

  # loop through all methods in the file
  while read -r line; do
      if [[ $line =~ "public" ]]; then
          if [[ $line =~ "getDescription" ]]; then
            # start reading the method
            while read -r line; do
              if [[ $line =~ "return" ]]; then
                # extract the return value without quote into a variable
                RETURN_VALUE=${line#*return }
                break
              fi
            done
          fi
      fi
  done < "$FILE"

  echo "$KEY_NAME=$RETURN_VALUE" >> $RESULT_FILE
}


FOLDER=$1

RESULT_FILE=$(basename $FOLDER)_fde.txt

PREFIX=""
BNAME=$(basename $FOLDER)
# get first 3 characters of the folder name
if [ -n "$FOLDER" ]; then
  PREFIX=${BNAME:0:3}
  echo $PREFIX
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
    ./fde.sh $file
  else
    # if it is not, check if it is a java file
    if [[ $file == *.java ]]; then
      # if it is, run the checker
      echo "Checking $file"
      return_extractor $file $RESULT_FILE $PREFIX
    fi
  fi
done




