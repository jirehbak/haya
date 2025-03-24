from modules import html_generator

import sys
import os

print(os.getcwd())

# append path
sys.path.append('../modules')

def test_html_generator():
    # save .html
    with open(f"test/html/{passage}.html", "w") as file:
        file.write(html)

    return html


if __name__ == '__main__':

    passage = ' '.join(sys.argv[1:])

    if passage:
        html = test_html_generator(passage)
        print(html)