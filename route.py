from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def root():
  return "The defalut route...."
  
@app.route("/account/", methods=['GET', 'POST'])
def account():
  if request.method == 'POST':
    return "POST method\n"  
  else:
    return "GET method"
    
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
    
      
