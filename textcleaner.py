def stripNonAlphaNum(text):
    import re
    return re.compile(r'[^A-Za-z0-9_,; ]', re.UNICODE).split(text)

with open('output.csv', 'r') as content_file:
    content = content_file.read()

stripped_content=stripNonAlphaNum(content)
stripped_string="".join(text)

with open("output.csv", "w") as output_file:
    output_file.write(stripped_string)
