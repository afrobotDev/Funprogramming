def file_to_prompt(file, to_string):

    prompt = to_string(file)

    return f"```\n{prompt}\n```"


