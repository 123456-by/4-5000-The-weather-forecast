import os

from flask import Flask, request, jsonify

from main import *


app = Flask(__name__)

@app.route('/')
def run():
    if send_template_message().get('errcode') == 0:
        return jsonify({
            'ok': True,
            'msg': 'send template message success'
        })
    else:
        return jsonify({
            'ok': False,
            'msg': 'send template message failed'
        })

if __name__ == '__main__':
    # 开启WebAPI
    port = os.environ.get('PORT', 5000) if os.environ.get('PORT') else 5000
    app.run(host='0.0.0.0', port=port)