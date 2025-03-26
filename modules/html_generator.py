from modules.api_caller.get_esv_html import get_esv_html
import re

def clean_html(html):
    # replace
    html_replacer = {'“' : '"',
                     '”': '"',
                     '–': '-'
                     }

    for key, value in html_replacer.items():
        html = html.replace(key, value)

    return html

# audio를 임베딩으로
def transform_html(input_html):
    # Use regex to replace the <a> tag with <audio> tag
    transformed_html = re.sub(
        r'\(<a class="mp3link" href="(.*?)" title="(.*?)" type="audio/mpeg">(.*?)</a>\)',
        r'<audio src="\1" autoplay loop controls type="audio/mpeg" id="esv audio"></audio>',
        input_html
    )
    # Add <br></br> tag after the Genesis text
    transformed_html = transformed_html.replace('<small class="audio extra_text">',
                                                '<br></br><small class="audio extra_text">')

    return transformed_html


def get_html(passage):
    # get html code
    html = get_esv_html(passage)
    html = clean_html(html)

    return html