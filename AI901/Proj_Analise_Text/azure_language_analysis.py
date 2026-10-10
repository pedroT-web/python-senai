import os

from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import re


# Valida se uma variavel obrigatoria existe no arquivo .env ou no ambiente.
def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Defina a variavel de ambiente {name}.")
    return value


# Carrega as variaveis definidas no arquivo .env.
load_dotenv()

# Cria a credencial e o cliente usado para chamar o Azure AI Language.
credential = AzureKeyCredential(get_required_env("AZURE_LANGUAGE_KEY"))
client = TextAnalyticsClient(
    endpoint=get_required_env("AZURE_LANGUAGE_ENDPOINT"),
    credential=credential,
)


# E-mail de teste fornecido na atividade.
email_cliente = (
    "Prezados, meu nome é Carlos Eduardo "
    "(CPF 123.456.789-00). Comprei um notebook "
    "no site da Contoso em 15 de setembro, mas "
    "o produto apresentou defeito na tela ao ligar. "
    "Resido na Rua das Flores, 450 - São Paulo/SP, "
    "e meu e-mail de contato é carlos.eduardo@email.com. "
    "Solicito a troca imediata ou o reembolso do valor pago. "
    "Aguardo retorno rápido!"
)


# PASSO 2: Detectar o idioma do e-mail.
# Processa o e-mail: detecta o idioma e redige os dados pessoais.
def processar_email(email: str) -> str:
    # PASSO 2: Detectar o idioma.
    resultado_idioma = client.detect_language(
        documents=[email]
    )

    idioma = resultado_idioma[0]

    print("--- Detecção de Idioma ---")

    if idioma.is_error:
        raise RuntimeError(
            f"Erro na detecção de idioma: {idioma.error.message}"
        )

    codigo_idioma = idioma.primary_language.iso6391_name

    print(f"Idioma: {idioma.primary_language.name}")
    print(f"Código ISO 639-1: {codigo_idioma}")
    print(
        f"Confiança: "
        f"{idioma.primary_language.confidence_score:.2%}"
    )

    # PASSO 3: Reconhecer e redigir dados pessoais.
    resultado_pii = client.recognize_pii_entities(
        documents=[email],
        language=codigo_idioma
    )

    documento_pii = resultado_pii[0]

    print("\n--- Anonimização de Dados Pessoais ---")

    if documento_pii.is_error:
        raise RuntimeError(
            f"Erro no reconhecimento de PII: "
            f"{documento_pii.error.message}"
        )

    texto_redigido = documento_pii.redacted_text

    # Proteção complementar para CPF brasileiro.
    texto_redigido = re.sub(
        r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b",
        "[CPF REDIGIDO]",
        texto_redigido
    )

    print("Entidades pessoais reconhecidas:")

    for entidade in documento_pii.entities:
        print(
            f"- Categoria: {entidade.category} "
            f"| Subcategoria: {entidade.subcategory or 'N/A'}"
        )

    print("\nTexto redigido:")
    print(texto_redigido)

    return texto_redigido


# Mantém a função que o foundry_text_analysis.py já utiliza.
def obter_texto_redigido() -> str:
    return processar_email(email_cliente)
