def stripNonAlphaNum(text):
    import re
    return re.compile(r'[^A-Za-z0-9_,; ]', re.UNICODE).split(text)


with open("output_1.csv", "r") as input:
    with open("output_2.csv", "wb") as output:
        for line in input:
            stripped_content = stripNonAlphaNum(line)
            stripped_string = "".join(stripped_content)
            output.write(stripped_string)
