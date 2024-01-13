from flask import Flask, request, jsonify,render_template
from flask_mail import Mail, Message
# 支持flask跨域
from flask_cors import CORS 
# 创建flask服务
app = Flask(__name__)
CORS(app, resources=r'/*')  # 注册CORS, "/*" 允许访问域名所有api 
 

books = [
    {
        "id":'1',
        "name":"hello world",
        "author":"迭名",
        "desc": "程序员入门第一本书",
        "status": True
    },
    {
        "id":'2',
        "name":"0基础学it",
        "author":"xx程序员",
        "desc": "某培训机构精心出品教程",
        "status": False
    },
]
app.config['MAIL_SERVER'] = 'smtp.google.com'  
#  to be fix 
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '.google.com'
app.config['MAIL_PASSWARD'] = 'passward'
mail = Mail(app)


@app.route('/Library',methods=['get'])
def index():
    return render_template('index.html',books=books)
 
# trun to rent page
@app.route('/Library/rentbook',methods=['get'])
def rentbook_html():
    return render_template('book/rent.html')

# rent
@app.route('/Library/rentbook',methods=['post'])
def rentbook(): 
    # 获取json数据
    book = request.get_json() 
    book['id']= str(len(book)-1) 
    print(book['id'])
    books.append(book)
    return jsonify({"books":books})

# # mail
# @app.route('/Mail', receiver)
# def mail():

#     return




 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)