from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form['name']
    email = request.form['email']

    
    print(f"Received form data: Name - {name}, Email - {email}")
    if name=="" or email=="":
        return "email and username canot be empty"
    else:

        return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
