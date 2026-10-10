# Projeto de Analise de Texto com Microsoft Foundry e Azure Language

Este projeto demonstra duas formas de analisar textos usando servicos da Microsoft/Azure:

- **Azure AI Language / Text Analytics** para identificar entidades e dados pessoais.
- **Microsoft Foundry / Azure OpenAI** para usar um modelo generativo em uma analise de texto.

## Arquivos principais

### `azure_language_analysis.py`

Usa o SDK `azure-ai-textanalytics` para chamar o Azure AI Language.

O script faz:

- Reconhecimento de entidades nomeadas, como pessoas, organizacoes, locais e datas.
- Deteccao de PII, ou seja, dados pessoais/sensiveis.
- Impressao do texto com dados pessoais redigidos.

Exemplo de texto analisado:

```text
Alex e eu participamos de uma conferencia da Microsoft em Las Vegas em 21 de setembro.
```

### `foundry_openai.py`

Usa o pacote oficial `openai` apontando para um endpoint do Microsoft Foundry/Azure OpenAI.

O script faz:

- Envia um texto de cliente para um modelo generativo.
- Pede para o modelo analisar o sentimento do texto.
- Pede para o modelo extrair a cidade citada.

Exemplo de texto analisado:

```text
Atendimento excelente! O produto chegou antes do prazo em Las Vegas.
```

## Requisitos

- Python instalado.
- Ambiente virtual `.venv` criado.
- Pacotes instalados a partir de `requirements.txt`.
- Recurso do Azure AI Language configurado.
- Deployment de modelo no Microsoft Foundry/Azure OpenAI.

## Instalar dependencias

No PowerShell, dentro da pasta do projeto:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuracao do ambiente

Crie um arquivo `.env` baseado no arquivo `.env.example`:

```env
AZURE_OPENAI_ENDPOINT=https://<resource-name>.services.ai.azure.com/openai/v1/
AZURE_OPENAI_API_KEY=<your-key>
MODEL_DEPLOYMENT_NAME=<your-model-deployment-name>
AZURE_LANGUAGE_ENDPOINT=https://<resource-name>.cognitiveservices.azure.com/
AZURE_LANGUAGE_KEY=<your-language-key>
```

Campos:

- `AZURE_OPENAI_ENDPOINT`: endpoint do recurso usado pelo Microsoft Foundry/Azure OpenAI.
- `AZURE_OPENAI_API_KEY`: chave de acesso ao recurso de modelo.
- `MODEL_DEPLOYMENT_NAME`: nome do deployment do modelo criado no Foundry.
- `AZURE_LANGUAGE_ENDPOINT`: endpoint do Azure AI Language.
- `AZURE_LANGUAGE_KEY`: chave do Azure AI Language.

> Importante: nao publique o arquivo `.env`, pois ele contem chaves de acesso.

## Como testar

Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Execute o exemplo com Azure AI Language:

```powershell
python sdk.py
```

Execute o exemplo com Microsoft Foundry/Azure OpenAI:

```powershell
python foundry_openai.py
```

## Saida esperada

Ao executar `sdk.py`, o terminal deve mostrar entidades encontradas no texto e uma versao redigida do texto com dados pessoais.

Ao executar `foundry_openai.py`, o terminal deve mostrar a resposta do modelo generativo com a analise solicitada.

## Observacoes

- O arquivo `foundry_openai.py` normaliza o endpoint caso ele venha com `/responses` no final.
- O arquivo `.gitignore` ignora `.env`, `.venv/` e arquivos temporarios Python.
- Se algum script falhar, confira se os endpoints, chaves e nomes dos deployments estao corretos.
