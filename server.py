from flask import Flask,render_template,request
import os
from main import calc

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/upload'
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        master = request.files['master']
        today = request.files['today']
        master.save(('A_Master.xlsx'))
        today.save(('A.xlsx'))
        calcA=calc('A')
        os.remove('A_ABSENT.xlsx')
        os.remove('A.xlsx')
        os.remove('A_Master.xlsx')
        return render_template('index.html',calc=calcA)

    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)