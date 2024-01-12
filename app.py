# flask创建http接口
from flask import Flask, request, jsonify,render_template
# 支持flask跨域
from flask_cors import CORS 
# 创建flask服务
app = Flask(__name__)
CORS(app, resources=r'/*')  # 注册CORS, "/*" 允许访问域名所有api 
 
# 暂时代替数据库
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

# 首页
@app.route('/Library',methods=['get'])
def index():
    # 自动在templates里找对应名称的文件
    return render_template('index.html',books=books)
 
# trun to rent page
@app.route('/Library/rentbook',methods=['get'])
def rentbook_html():
    # 自动在templates里找对应名称的文件
    return render_template('book/rent.html')

# rent
@app.route('/Library/rentbook',methods=['post'])
def rentbook(): 
    # 获取json数据
    book = request.get_json() 
    # 用数组下标表示id
    book['id']= str(len(book)-1) 
    print(book['id'])
    # 添加到books末尾
    books.append(book)
    return jsonify({"books":books})


 
if __name__ == "__main__":
    # 运行web服务
    app.run(host='0.0.0.0', port=5000)