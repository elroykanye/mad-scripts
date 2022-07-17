import sys

key_name = sys.argv[1]
value_name = ''
java_file = sys.argv[2]
out_file_name = sys.argv[3].replace(".sh", "")

output_file = open(out_file_name, 'a')

def process_operation_desc_brief(lines) -> any:
    desc: str = "".join(lines)
    desc = desc.replace('\n', ' ')
    desc = desc.replace("return", "")
    if desc[-1] == "}":
        desc = desc[:-1]
    if desc[-1] == ";":
        desc = desc[:-1]
    print(desc)
    result = key_name + "=" + desc.strip() + "\n"
    output_file.write(result)

# loop through each line in file
with open(java_file) as f:
    java_filename = java_file.split('/')[-1]
    print(java_filename)
    woi = False
    d_woi = False
    step: int = -1
    lines = []
    for line in f:
        if step == 0 and woi:
            lines.append(line.strip())
        if "getBriefDescription(Project project)" in line:
            woi = True
            if "{" in line:
                step = step + 1
            continue
        if "{" in line and woi:
            step = step + 1
        if "}" in line and woi:
            step = step - 1
            if step == -1:
                woi = False

    process_operation_desc_brief(lines)
    print("\n")
output_file.close()

