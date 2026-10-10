import os

from dotenv import load_dotenv
from openai import OpenAI
from azure_language_analysis import obter_texto_redigido
import re


# Valida se uma variavel obrigatoria existe no arquivo .env ou no ambiente.
def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Defina a variavel de ambiente {name}.")
    return value


# Normaliza o endpoint para o formato esperado pelo SDK da OpenAI.
# O SDK adiciona a rota /responses automaticamente ao chamar responses.create().
def normalize_base_url(endpoint: str) -> str:
    endpoint = endpoint.rstrip("/")
    if endpoint.endswith("/responses"):
        endpoint = endpoint[: -len("/responses")]
    if not endpoint.endswith("/openai/v1"):
        endpoint = f"{endpoint}/openai/v1"
    return f"{endpoint}/"


# Carrega as variaveis definidas no arquivo .env.
load_dotenv()

# Cria o cliente apontando para o endpoint do Microsoft Foundry/Azure OpenAI.
client = OpenAI(
    base_url=normalize_base_url(get_required_env("AZURE_OPENAI_ENDPOINT")),
    api_key=os.getenv("AZURE_OPENAI_API_KEY") or get_required_env("API_KEY"),
)


# Obtém o texto após a detecção de idioma e a anonimização.
texto_cliente = obter_texto_redigido()

# Verificação complementar antes de enviar o texto ao modelo.
def validar_privacidade(texto: str) -> None:
    # Identifica e-mails que possam ter permanecido no texto.
    padrao_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    # Identifica CPFs nos formatos 000.000.000-00 ou 00000000000.
    padrao_cpf = r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b"

    if re.search(padrao_email, texto):
        raise ValueError(
            "Envio bloqueado: foi encontrado um possível e-mail pessoal."
        )

    if re.search(padrao_cpf, texto):
        raise ValueError(
            "Envio bloqueado: foi encontrado um possível CPF."
        )

    print("Validação complementar de privacidade aprovada.")


# A validação precisa ocorrer antes da chamada ao modelo.
validar_privacidade(texto_cliente)


# Instruções para a análise generativa.
instrucao = f"""
Você é um assistente de atendimento ao cliente da Contoso.

Analise o e-mail anonimizado abaixo e responda em português
com as seguintes seções:

1. SENTIMENTO:
Classifique o sentimento como positivo, neutro ou negativo
e explique brevemente o motivo.

2. RESUMO:
Resuma o problema do cliente e o que ele está solicitando.

3. RESPOSTA SUGERIDA:
Escreva uma resposta profissional, empática e objetiva.
Não prometa troca ou reembolso já aprovado.
Informe que a solicitação será analisada pela equipe responsável.

REGRAS DE PRIVACIDADE:
- Não tente descobrir dados que foram ocultados.
- Não invente informações pessoais.
- Trabalhe somente com o texto anonimizado.

E-mail:
{texto_cliente}
"""

# Envia o texto anonimizado ao modelo generativo.
response = client.responses.create(
    model=get_required_env("MODEL_DEPLOYMENT_NAME"),
    input=instrucao,
)

# Exibe o resultado da análise.
print("--- Análise Generativa do E-mail ---")
print(response.output_text)


# Testes de segurança: devem bloquear dados pessoais não redigidos.
print("\n--- Testes de Privacidade ---")

casos_de_teste = [
    "Contato: cliente@exemplo.com",
    "CPF: 123.456.789-00",
]

for caso in casos_de_teste:
    try:
        validar_privacidade(caso)
    except ValueError as erro:
        print(f"Bloqueio confirmado: {erro}")
    else:
        print(f"FALHA: o texto passou pela validação: {caso}")
