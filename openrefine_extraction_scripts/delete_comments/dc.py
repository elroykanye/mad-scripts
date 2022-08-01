import sys
import os

# deleting lines which were commented out during the extraction process
remove_cases = {
    "eval_error": [False, '// return new EvalError', '//return new EvalError'],
    "op_desc": [True, '// return'],
}

base_folder = sys.argv[1]
remove_case = sys.argv[2]

def remove_comments(filename, sw_excludes, follow_lines):
    print("Removing comments from " + filename)
    try:
        with open(filename, 'r') as fr:
            # read all lines
            lines = fr.readlines()
            # delete commented lines
            with open(filename, 'w') as fw:
                flag = False
                for line in lines:
                    # check if line starts with '// return new EvalError'
                    # if line.strip().startswith('// return new EvalError') or line.strip().startswith('//return new EvalError'):
                    if line.strip().startswith(tuple(sw_excludes)):
                        print("DELETED: " + line)
                        flag = True
                    elif flag and follow_lines and line.strip().startswith("//"):
                        print("DELETED FOLLOING: " + line)
                    else:
                        fw.write(line)
                        flag = False
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
                if remove_case in remove_cases.keys():
                    remove_comments(os.path.join(root, file), remove_cases[remove_case][1:], remove_cases[remove_case][0])
                else:
                    print("remove_case not recognised")