# Audio-to-Texto

## Descrição
Este projeto é um aplicativo de transcrição de áudio para texto utilizando a API Whisper da OpenAI. Ele permite que os usuários façam upload de arquivos de áudio e obtenham transcrições precisas.

## Pré-requisitos
- Python 3.7 ou superior
- Pip (Python package installer)

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

## Como Usar
1. Crie um arquivo `.env` na raiz do projeto e adicione sua chave API da OpenAI:
    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```
2. Execute o aplicativo Streamlit:
    ```sh
    streamlit run app.py
    ```
3. No navegador, insira sua chave API no campo fornecido na barra lateral, faça upload de um arquivo de áudio e obtenha a transcrição.

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
