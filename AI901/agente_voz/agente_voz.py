import os

import azure.cognitiveservices.speech as speechsdk
from azure.ai.projects import AIProjectClient
from azure.identity import DeviceCodeCredential
from dotenv import find_dotenv, load_dotenv


# Carrega as variáveis do arquivo .env.
load_dotenv(find_dotenv())

speech_key = os.getenv("SPEECH_KEY")
speech_region = os.getenv("SPEECH_REGION")
if not speech_key or not speech_region:
    raise RuntimeError("Configure SPEECH_KEY e SPEECH_REGION no arquivo .env.")

speech_config = speechsdk.SpeechConfig(
    subscription=speech_key,
    region=speech_region,
)
speech_config.speech_recognition_language = "pt-BR"
speech_config.speech_synthesis_voice_name = "pt-BR-AntonioNeural"

project_endpoint = "https://pedro-augusto1-resource.services.ai.azure.com/api/projects/pedro-augusto1"
agent_name = "speech-agent"
comandos_encerramento = {"sair", "encerrar", "tchau", "até mais", "ate mais"}


def ouvir_microfone(recognizer):
    """Captura uma fala e retorna o texto reconhecido, ou uma string vazia."""
    print("🎤 Estou ouvindo... Fale sua mensagem.")
    resultado = recognizer.recognize_once_async().get()

    if resultado.reason == speechsdk.ResultReason.RecognizedSpeech:
        texto = resultado.text.strip()
        if texto:
            print(f"✅ Você disse: {texto}\n")
        return texto

    if resultado.reason == speechsdk.ResultReason.Canceled:
        detalhes = resultado.cancellation_details
        print(f"⚠️ Não consegui reconhecer a fala: {detalhes.reason}.")
        if detalhes.error_details:
            print(detalhes.error_details)
    else:
        print("⚠️ Não detectei uma fala. Tente novamente.")
    return ""


def falar(synthesizer, texto):
    resultado = synthesizer.speak_text_async(texto).get()
    if resultado.reason == speechsdk.ResultReason.Canceled:
        detalhes = resultado.cancellation_details
        print(f"⚠️ Não foi possível reproduzir a resposta: {detalhes.reason}.")
        if detalhes.error_details:
            print(detalhes.error_details)


def main():
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config,
    )
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    print("🎤 Pode falar com o Speech! A conversa continuará até você dizer 'sair' ou 'tchau'.")
    print("⚠️ No primeiro acesso, siga no navegador o código de autenticação exibido no terminal.\n")

    try:
        with AIProjectClient(
            endpoint=project_endpoint,
            credential=DeviceCodeCredential(),
            allow_preview=True,
        ) as project_client:
            openai_client = project_client.get_openai_client(agent_name=agent_name)
            # Reutilizar o mesmo ID mantém o contexto das mensagens durante a sessão.
            conversation = openai_client.conversations.create()

            while True:
                texto_usuario = ouvir_microfone(recognizer)
                if not texto_usuario:
                    continue

                if texto_usuario.casefold().strip(" .,!?") in comandos_encerramento:
                    despedida = "Até mais! Foi um prazer conversar com você."
                    print(f"\n⚽ Speech-Agent: {despedida}\n")
                    falar(synthesizer, despedida)
                    break

                print("🧠 Speech está preparando a resposta...")
                try:
                    resposta = openai_client.responses.create(
                        conversation=conversation.id,
                        input=[{"role": "user", "content": texto_usuario}],
                    )
                    texto_resposta = (resposta.output_text or "").strip()
                    if not texto_resposta:
                        texto_resposta = "Não consegui preparar uma resposta agora. Pode repetir?"
                except Exception as erro:
                    print(f"❌ Erro ao consultar o agente no Foundry: {erro}")
                    texto_resposta = "Tive um problema ao consultar o agente. Pode tentar falar novamente?"

                print(f"\n Speech: {texto_resposta}\n")
                falar(synthesizer, texto_resposta)

    except KeyboardInterrupt:
        print("\nConversa encerrada.")
    except Exception as erro:
        print(f"❌ Erro ao conectar com o agente no Foundry: {erro}")


if __name__ == "__main__":
    main()
