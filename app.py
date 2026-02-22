from flask import Flask, render_template

app = Flask(__name__)

@app.route('/stmt_iteration')
def get_stmt_iteration():
    fruits = ['Apple', 'Banana', 'Cherry', 'Melon', 'Lemon']
    return render_template('stmt_iteration.html', l=fruits)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=31337)