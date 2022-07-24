import sys

key_name = sys.argv[1]
value_name = ''
java_file = sys.argv[2]
out_file_name = sys.argv[3].replace(".sh", "")

output_file_create = open(out_file_name, 'a')


def process_history_entry(lines, brief) -> any:
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
    desc_parts = desc.split(",")
    if len(desc_parts) < 3:
        return
    print(desc_parts)
    desc = desc_parts[2]
    result = key_name + "=" + desc.strip() + "\n"
    if brief:
        output_file_brief.write(result)
    else:
        output_file_create.write(result)


def parse_history_entry():
    with open(java_file) as f:
        java_filename = java_file.split('/')[-1]
        print(java_filename)
        in_method = False
        returning = False
        lines = []
        for line in f:
            if "HistoryEntry createHistoryEntry" in line:
                in_method = True
                continue
            if ("return" in line or returning) and in_method:
                lines.append(line.strip())
                if line.strip()[-1] == ";":
                    returning = False
                    break
                else:
                    returning = True

        process_history_entry(lines, False)
        print("\n")


parse_history_entry()

output_file_create.close()
