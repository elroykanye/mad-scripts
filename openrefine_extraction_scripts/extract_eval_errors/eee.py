import sys

key_name = sys.argv[1]
value_name = ''
java_file = sys.argv[2]
output_file_name = sys.argv[3]
# open as append

output_file = open(output_file_name, 'a')


def process_eval_error(eval_err_line: str) -> any:
    print("ERROR LINE ->" + eval_err_line)
    if "return" in eval_err_line and not eval_err_line.strip()[0] == '/':
        eval_err_line = eval_err_line.replace("return", "")
        eval_err_line = eval_err_line.replace(");", "")
        eval_err_line = eval_err_line.replace("new EvalError(", "")
        eval_err_line = eval_err_line.strip()
        
        if "EvalErrorMessage" in eval_err_line:
        	result = "COMPLETED >>> " + key_name + '=' + eval_err_line + '\n'
        else:
        	result = key_name + '=' + eval_err_line + '\n'
        print('\n' + result + '\n')

        # write the key and value to the file as key value pair
        output_file.write(result)


# loop through each line in file
with open(java_file) as f:
    woi = False
    acc: str = ''
    for line in f:

        if woi:
            acc += line.strip()
            if line.strip()[-1] == ';':
                woi = False
                process_eval_error(acc)
                acc = ''

        # find the line which has the word "EvalError"
        if "EvalError" in line:
            # check if last character is semicolon
            if line.strip()[-1] == ';':
                # remove semicolon
                line = line[:-1]
                process_eval_error(line)
            else:
                acc += line.strip()
                woi = True

output_file.close()

