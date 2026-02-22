from flask import Flask, render_template

app = Flask(__name__)

@app.route('/stmt_condition')
def get_stmt_condition():
    user_role = 'member'  # Example: 'admin', 'member', 'guest'
    return render_template('stmt_condition.html', role=user_role)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=31337)