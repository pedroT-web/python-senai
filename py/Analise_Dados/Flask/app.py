# 1. IMPORTAÇÕES:
# - Flask: Classe principal que inicializa a aplicação web.
# - render_template: Função que localiza arquivos HTML na pasta 'templates' e processa variáveis (Jinja2).
# - request: Objeto que contém os dados da requisição HTTP feita pelo usuário (como formulários, parâmetros de URL, etc.).
from flask import Flask, render_template, request

# 2. INSTANCIAÇÃO:
# Cria o objeto da aplicação. O argumento especial '__name__' indica ao Flask onde ele está 
# sendo executado, permitindo que ele localize pastas de arquivos estáticos e templates.
app = Flask(__name__)

# 3. DEFINIÇÃO DE ROTA:
# O decorator '@app.route' mapeia a URL para a função Python logo abaixo.
# "/" significa a raiz do site (página inicial).
# 'methods' define quais verbos HTTP são aceitos:
#   - GET: Quando o usuário apenas acessa a página ou atualiza a tela.
#   - POST: Quando o usuário envia dados (por exemplo, ao clicar no botão 'Enviar' do formulário).
@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = None  # Inicializa a variável como vazia para acessos normais via GET.

    # Verifica se a requisição atual é um envio de formulário (POST)
    if request.method == "POST":
        # 'request.form' funciona como um dicionário Python contendo os campos do formulário HTML.
        # Buscamos o valor pelo atributo 'name' definido na tag <input>: name="nome".
        nome = request.form.get("nome")
        
        # Se o usuário preencheu o campo, montamos a mensagem de resposta
        if nome:
            mensagem = f"Olá, {nome}! Seja bem-vindo ao Flask."

    # 'render_template' carrega o arquivo 'index.html' da pasta 'templates'.
    # Passamos a variável 'mensagem' do Python para o template com a sintaxe chave=valor.
    return render_template("index.html", mensagem=mensagem)

# 4. EXECUÇÃO DO SERVIDOR LOCAL:
# Garante que o servidor só iniciará se este arquivo for executado diretamente (não importado como módulo).
# 'debug=True': Ativa o recarregamento automático ao salvar o código e mostra telas detalhadas de erro.
# OBS: O modo debug deve ser usado apenas em ambiente de desenvolvimento/estudo, nunca em produção.
if __name__ == "__main__":
    app.run(debug=True)