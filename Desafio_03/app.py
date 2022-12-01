from flask import Flask, render_template, request, url_for

from flask_mysqldb import MySQL

def create_app():
    from app import routes
    routes.init_app(app)

    return app

app = Flask(__name__)

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL(app)

@app.route('/')
def index(): 
    return render_template('public/index.html')

@app.route('/quem_somos')
def quem_somos():
    return render_template('public/quem_somos.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
       
        mysql.connection.commit()
        
        cur.close()

        return 'Mensagem enviada com sucesso!'
    return render_template('public/contato.html')


if __name__ == '__main__':
    app.run(debug=True)