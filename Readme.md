# Audio-to-Texto

## Descrição
Este projeto é um aplicativo de transcrição de áudio para texto utilizando a API Whisper da OpenAI. Ele permite que os usuários façam upload de arquivos de áudio e obtenham transcrições precisas.

## Pré-requisitos
- Python 3.7 ou superior
- Pip (Python package installer)
- ffmpeg

## Instalação
1. Clone o repositório:
    ```sh
    git clone https://github.com/ecodelearn/audio-to-texto.git
    cd audio-to-texto
    ```
2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
4. Instale o `ffmpeg`:
    - **Para Ubuntu/Debian**:
        ```sh
        sudo apt-get install ffmpeg
        ```
    - **Para macOS (usando Homebrew)**:
        ```sh
        brew install ffmpeg
        ```
    - **Para Windows**:
        [Baixe o executável do site oficial do FFmpeg](https://ffmpeg.org/download.html) e adicione-o ao PATH do sistema.

## Como Usar
1. Execute o aplicativo Streamlit:
    ```sh
    streamlit run app.py
    ```
2. No navegador, insira sua chave API da OpenAI no campo fornecido na barra lateral e pressione Enter.
3. Faça upload de um arquivo de áudio nos formatos suportados (wav, mp3, flac, ogg, opus).
4. Acompanhe o progresso da transcrição na interface.
5. Baixe o arquivo de transcrição clicando no botão de download.

## Contribuição
Sinta-se à vontade para contribuir com o projeto. Para isso, siga os passos:
1. Fork este repositório.
2. Crie uma branch com sua feature: `git checkout -b minha-feature`.
3. Commit suas mudanças: `git commit -m 'Minha nova feature'`.
4. Envie para a branch principal: `git push origin minha-feature`.
5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autores
- [Daniel Dias](https://github.com/ecodelearn)
