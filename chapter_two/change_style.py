# use map to call convert_line for each line_list item
def change_bullet_style(document):
    line_list = document.split('\n')
    styled_list = list(map(convert_line, line_list))
    return '\n'.join(styled_list)

def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
