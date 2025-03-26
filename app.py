import sys
import os

# modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from flask import Flask, render_template, request
from modules.html_generator import get_html, transform_html

app = Flask(__name__)

# 기본 페이지 라우트
@app.route('/')
def index():
    return render_template('index.html')

# 폼 데이터 처리 라우트
@app.route('/generate', methods=['POST'])
def generate_html():
    # 사용자가 입력한 텍스트를 받아옵니다.
    user_input = request.form['user_input']

    # 텍스트를 기반으로 HTML 코드 생성
    generated_html = get_html(user_input)
    # Transform the HTML
    transformed_html = transform_html(generated_html)
    output_html = f"<p>{transformed_html}</p>"

    # 결과 페이지로 생성된 HTML을 전달하여 렌더링
    return render_template('index.html', user_input=user_input, generated_html=output_html)

if __name__ == '__main__':
    app.run(debug=True)
