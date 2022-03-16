import re

regex = r"m{1,2}|\n|^P"

test_str = ("THis is demo of Regex.\n"
            "Python is a beautiful programming language.")

subst = "*"

# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 0, re.MULTILINE)

if result:
    print(result)
