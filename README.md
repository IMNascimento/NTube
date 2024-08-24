<h1 align="center">
  <br>
  <a href="#"><img src="https://github.com/user-attachments/assets/47be0af7-df9a-42b0-8fc5-5e55050bae4f" alt="ntube" width="200"></a>
  <br>
  Ntube
  <br>
</h1>

# NTube - Seu Conversor de Vídeos do YouTube

NTube é uma aplicação Python Flask que permite converter vídeos do YouTube em formatos MP3 e MP4 de forma rápida e fácil. Com NTube, você pode baixar seus vídeos favoritos do YouTube em formato de áudio ou vídeo para ouvir e assistir offline.

## Funcionalidades

- Conversão de vídeos do YouTube para MP3
- Conversão de vídeos do YouTube para MP4
- Interface simples e intuitiva
- Sem necessidade de cadastro

## Como usar

0. Instale a versão 3.10 python ou até a 3.12 foi testado a aplicação.

1. Clone este repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/IMNascimento/NTube.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd NTube
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Inicie o servidor Flask:

    ```bash
    python main.py
    ```

    ou 

    ```bash
    flask --app main run --host=0.0.0.0 --port=80
    ```


5. Acesse o aplicativo em seu navegador da web:

    ```
    http://localhost:80
    ```

6. Cole o link do vídeo do YouTube na caixa de texto e clique em "Buscar" para começar a converter.

## Configuração

Não é necessária nenhuma configuração adicional. Por padrão, o servidor Flask estará configurado para ouvir em todas as interfaces de rede na porta 80.

## Contribuindo

Contribuições são bem-vindas! Se você encontrar um problema ou tiver uma ideia para melhorar o NTube, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

[Nascimento](https://github.com/IMNascimento)

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).