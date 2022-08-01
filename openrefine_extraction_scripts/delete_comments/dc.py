import sys
import os

# deleting lines which were commented out during the extraction process

base_folder = sys.argv[1]

def remove_comments(filename):
    print("Removing comments from " + filename)
    try:
        with open(filename, 'r') as fr:
            # read all lines
            lines = fr.readlines()
            # delete commented lines
            with open(filename, 'w') as fw:
                for line in lines:
                    # check if line starts with '// return new EvalError'
                    if line.strip().startswith('// return new EvalError') or line.strip().startswith('//return new EvalError'):
                        print("DELETED: " + line)
                    else:
                        fw.write(line)
    except IOError:
        print('File not found')
        sys.exit(1)
    print("-----------------------Done-----------------------")

     
# check if base_folder is a directory
if base_folder.endswith('/') or base_folder.endswith('\\'):
    # recursively search for .java files in base_folder
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith('.java'):
                remove_comments(os.path.join(root, file))