from flask import Flask, request
app = Flask(__name__)

@app.route("/account/", methods=['POST', 'GET'])
def account():
  if request.method == 'POST':
    print request.form
    name = request.form['name']
    return "Hello %s" % name
  else:
    page = '''
    <html><body>
      <form action="" method="post" name="form">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name"/>
        <input type="submit" name="submit" id="submit"/>
      </form>
    </body></html>'''
      
    return page

@app.route("/hello/")
def hello():
  # parameter supply
  name = request.args.get('name', '')
  if name == '':
    return "no params"
  else:
    return "Hello %s" % name

@app.route("/upload/", methods=['POST', 'GET'])
def upload():
  if request.method == 'POST':
    f = request.files['datafiles']
    f.save('static/uploads/upload.png')
    return "File uploaded"
  else:
    page='''
    <html><body>
     <form action="" method="POST" name="form" enctype="multipart/form-data">
       <input type="file" name="datafile" />
       <input type="submit" name="submit" id="submit" />
    </form>
    </body></form>
    '''
    return page, 200


    
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
    
      
