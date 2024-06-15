from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/analyze', methods=['POST'])
def analyze():
    password = request.form['password']
    result = password_analyzer(password)
    return render_template('index.html', result=result)

def password_analyzer(password):
    # Your password analyzing function here
    weak_criteria = 6
    moderate_criteria = 10
    
    if len(password) < weak_criteria:
        return "Weak"
    elif len(password) < moderate_criteria:
        return "Moderate"
    else:
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in "!@#$%^&*()-_=+{}[]|;:,.<>?/~" for char in password)
        
        if has_upper and has_lower and has_digit and has_special:
            return "Strong"
        else:
            return "Moderate"

if __name__ == '__main__':
    app.run(debug=True)
