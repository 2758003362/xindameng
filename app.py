from flask import Flask, jsonify, Response,request

import json
from typing import List, Dict

app = Flask(__name__)

@app.route('/xmlService', methods=['GET', 'POST'])
def get_xml(encoding = "utf-8"):
    if request.method == 'GET':
        # 处理GET请求，从查询参数获取
        param1 = request.args.get('param1')  # request.args.get('param1')
        param2 = request.args.get('param2')
    else:
        # 获取JSON数据
        json_str = request.data or request.get_json() or request.form

        # return json_str
        data = json.loads(json_str)

        # 提取param1和param2
        param1 = data.get('param1', '')
        param2 = data.get('param2', '')

    return "你好" + param1 + "  " + param2

# 启动服务
if __name__ == '__main__':
    # 允许外部访问，端口为5000，开启调试模式
    app.run(host='0.0.0.0', port=5000, debug=True)