from flask import Flask, render_template, request
from HelloFlask import app
from datetime import datetime
from werkzeug.utils import secure_filename
import openpyxl


@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    format_date = now.strftime("%A, %d %B, %Y at %X")
    title = "Hello Flask"
    message = "Hello Flask!"
    content = "on " + format_date
    return render_template("index.html", title=title, message=message, content=content)

@app.route('/about')
def about():
    return render_template("about.html",
                           title='About Flask',
                           content='all about flask')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template("upload.html",
                               title="upload file")
    elif request.method == 'POST':
        if 'fileUpload' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['fileUpload']
        file.save("C:\\Users\\chenzige\\source\\repos\\LearningFlask\\BasicProject\\HelloFlask\\tempfiles\\"+secure_filename(file.name)+'.xlsx')
        wb = openpyxl.load_workbook("C:\\Users\\chenzige\\source\\repos\\LearningFlask\\BasicProject\\HelloFlask\\tempfiles\\"+file.name+'.xlsx')
        ws = wb.active
        rows = ws.max_row
        cols = ws.max_column
        data=ws.cell(row=rows,column=cols).value 
        result = (cell.value for cell in row for row in ws[1:4] )
        #values = ' '
        #for cell in row:
        #    values+=cell.value
        return data


