import sys

key_name = sys.argv[1]
value_name = ''
java_file = sys.argv[2]
out_file_name = sys.argv[3].replace(".sh", "")

output_file_create = open(out_file_name, 'a')
output_file_brief = open("brief_" + out_file_name, 'a')


def process_operation_desc_brief(lines, brief) -> any:
    if len(lines) == 0:
        print("SITUATION EMPTY")
        return
    desc: str = "".join(lines)
    desc = desc.replace('\n', ' ')
    desc = desc.replace("return", "")
    if desc[-1] == "}":
        desc = desc[:-1]
    if desc[-1] == ";":
        desc = desc[:-1]
    print(desc)
    result = key_name + "=" + desc.strip() + "\n"
    if brief:
        output_file_brief.write(result)
    else:
        output_file_create.write(result)


def parse_brief_desc():
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
        process_operation_desc_brief(lines, True)
        print("\n")


def parse_create_desc():
    with open(java_file) as f:
        java_filename = java_file.split('/')[-1]
        print(java_filename)
        in_method = False
        returning = False
        lines = []
        for line in f:
            if "createDescription" in line:
                in_method = True
                continue
            if ("return" in line or returning) and in_method:
                lines.append(line.strip())
                if line.strip()[-1] == ";":
                    returning = False
                    break
                else:
                    returning = True



        process_operation_desc_brief(lines, False)
        print("\n")


parse_brief_desc()
parse_create_desc()

output_file_create.close()
output_file_brief.close()
