from modules.api_caller.get_esv_html import get_esv_html

def clean_html(html):
    # replace
    html_replacer = {'“' : '"',
                     '”': '"',
                     '–': '-'
                     }

    for key, value in html_replacer.items():
        html = html.replace(key, value)

    return html

def get_html(passage):
    # get html code
    html = get_esv_html(passage)
    html = clean_html(html)

    return html