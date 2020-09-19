from flask import Flask,redirect,url_for,render_template,request

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
        
        return render_template('index.html',calc=calc('A'))

    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)