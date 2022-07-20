# extract first argument
import sys, os

returns_file = sys.argv[1]

clean_returns_file = "clean_" + returns_file
# delete file if it already exists
if os.path.exists(clean_returns_file):
    os.remove(clean_returns_file)

# loop through each line in returns_file
for line in open(returns_file):
    # split by "="
    split_line = line.split("=")
    key_name = split_line[0]
    value = split_line[1]

    # remove all trailing whitespace
    value = value.strip()
    # remove ";" at end of string
    value = value.rstrip(";")

    # remove opening and closing quotes
    value = value.strip('"')

    # write key_name and value to new file
    with open(clean_returns_file, "a") as f:
        f.write(key_name + "=" + value + "\n")


