def format_line(line):
  strip_line = line.strip()
  print(strip_line)
  cap_line = strip_line.upper()
  print(cap_line)
  replace_line = cap_line.replace('.', '')
  print(replace_line)
  return f"{replace_line}..."
