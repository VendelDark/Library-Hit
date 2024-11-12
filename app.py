from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
data_file = 'data/livros.txt'

# Rota para a página de cadastro
@app.route('/')
def index():
    return render_template('index.html')

# Rota para salvar o livro
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    titulo = request.form['titulo']
    autor = request.form['autor']
    resumo = request.form['resumo']
    imagem = request.files['imagem']

    if imagem:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], imagem.filename)
        imagem.save(image_path)
    else:
        image_path = ''

    # Salvando os dados no arquivo TXT
    with open(data_file, 'a') as f:
        f.write(f"{titulo},{autor},{resumo},{image_path}\n")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
