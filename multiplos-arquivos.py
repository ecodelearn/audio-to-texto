import streamlit as st
import openai
import os
import tempfile
from pydub import AudioSegment

# Função para dividir o áudio em chunks
def split_audio(file_path, chunk_length_ms=30000):
    audio = AudioSegment.from_file(file_path)
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk_path = tempfile.mktemp(suffix=".wav")
        chunk.export(chunk_path, format="wav")
        chunks.append(chunk_path)
    return chunks

# Função para enviar áudio para a API Whisper e obter a transcrição
def transcribe_audio(file_path, api_key):
    openai.api_key = api_key
    try:
        with open(file_path, 'rb') as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file,
                response_format="text"  # Usar texto simples para facilitar a depuração
            )
        return response
    except openai.error.OpenAIError as e:
        st.error(f"Erro na API da OpenAI: {e}")
        return None
    except Exception as e:
        st.error(f"Erro ao transcrever o áudio: {e}")
        return None

# Função para salvar a transcrição em um arquivo .txt
def save_transcription(transcription, filename):
    if not os.path.exists('transcricoes'):
        os.makedirs('transcricoes')
    
    filepath = os.path.join('transcricoes', filename)
    with open(filepath, 'w') as f:
        f.write(transcription)
    
    return filepath

# Função para salvar o arquivo temporariamente
def save_temp_file(file):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file.read())
        return temp_file.name

# Criação da barra lateral
st.sidebar.title("Configuração da API")
api_key = st.sidebar.text_input("Insira sua chave API da OpenAI e tecle enter para usar o app. Essa chave vai ser apagada após o uso do app.", type="password")

if api_key:
    # Criação da interface do usuário
    st.title("Transcrição de Áudio com Whisper")
    st.write("Carregue arquivos de áudio para obter a transcrição.")

    # Carregar os arquivos de áudio
    audio_files = st.file_uploader("Escolha arquivos de áudio", type=['wav', 'mp3', 'flac', 'ogg', 'opus'], accept_multiple_files=True)

    # Se arquivos foram carregados, realizar a transcrição
    if audio_files:
        for audio_file in audio_files:
            st.audio(audio_file, format='audio/wav')
            st.write(f"Dividindo o áudio em chunks: {audio_file.name}...")
            
            # Salvar o arquivo temporariamente
            temp_file_path = save_temp_file(audio_file)
            
            # Verificar e converter o formato OPUS para WAV se necessário
            if temp_file_path.endswith(".opus"):
                converted_file_path = tempfile.mktemp(suffix=".wav")
                audio = AudioSegment.from_file(temp_file_path, format="opus")
                audio.export(converted_file_path, format="wav")
                os.remove(temp_file_path)
                temp_file_path = converted_file_path

            # Dividir o áudio em chunks
            chunks = split_audio(temp_file_path)
            
            # Inicializar lista para armazenar os segmentos de transcrição
            all_transcriptions = []
            
            # Transcrever cada chunk
            for chunk in chunks:
                st.write(f"Transcrevendo chunk: {chunk}")
                response = transcribe_audio(chunk, api_key)
                if response is not None:
                    st.write(f"Transcrição do chunk: {response}")
                    all_transcriptions.append(response)
                else:
                    st.error("Erro na transcrição deste chunk.")
                
                # Remover o arquivo temporário
                os.remove(chunk)
            
            # Juntar todas as transcrições
            full_transcription = "\n".join(all_transcriptions)
            
            # Salvar a transcrição em um arquivo e permitir o download
            filename = f'transcricao_{audio_file.name}.txt'
            filepath = save_transcription(full_transcription, filename)
            
            st.write(f"Transcrição completa para {audio_file.name}:")
            with open(filepath, 'rb') as file:
                st.download_button(
                    label=f"Baixar Transcrição de {audio_file.name}",
                    data=file,
                    file_name=filename,
                    mime="text/plain"
                )
            
            # Limpar o arquivo temporário
            os.remove(temp_file_path)
