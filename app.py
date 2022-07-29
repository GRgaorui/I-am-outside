from flask import Flask, render_template, request,jsonify
import main as OS
import time
app = Flask(__name__)


@app.route('/',methods=['GET'])
def main():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/index',methods=['GET','POST'])
def index():
    task = request.args['interest']
    if task == '1':
        OS.open_in_school()
        OS.check_in(request.args['temperature'])
        return jsonify({'code': 0, 'msg': 'success'})
    elif task == '2':
        OS.open_in_school()
        time.sleep(0.5)
        OS.report(request.args['phonenumber'],request.args['reason'],request.args['direction'])
        return jsonify({'code': 0, 'msg': 'success'})

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9900)