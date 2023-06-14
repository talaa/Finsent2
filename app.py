from flask import Flask, render_template,request
from stockdata import get_stock_data
from utilities import fetch

app = Flask(__name__)

@app.route("/")
def hello_world():
    navbar_html = render_template('navbar.html')
    return render_template("index.html", navbar_html=navbar_html,title="Main")


@app.route('/ai-financialnews-sentiment-analysis', methods=['POST'])
def process():
    navbar_html = render_template('navbar.html')
    
    text_input = request.form.get('stock_name')
    slider_input = request.form.get('days_input')
    stock_data=get_stock_data(text_input)[0]
    company_name=get_stock_data(text_input)[1].info['longName']
    company_industry=get_stock_data(text_input)[1].info['industry']
    
    
    # Use the values as needed']
    
    
    # Use the values as needed
    print(f'Text Input: {text_input}')
    print(f'Slider Input: {slider_input}')

    # Perform other operations or return a response if needed

    return render_template("finsent.html",navbar_html=navbar_html,stock_data=stock_data,title=text_input,company_name=company_name,company_industry=company_industry)

    