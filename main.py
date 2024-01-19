import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from urllib.request import urlretrieve
from pytube import YouTube



app = Flask(__name__)

# Senha para autenticação
senha_correta = "igor"
senha = None
url = None

def definir_permissao_pasta(caminho_pasta, permissao):
    # O argumento 'permissao' deve ser uma string representando as permissões desejadas, por exemplo, '755'
    try:
        os.chmod(caminho_pasta, int(permissao, 8))
        print(f'Permissões da pasta {caminho_pasta} alteradas para {permissao}')
    except OSError as e:
        print(f"Erro ao definir permissões: {e}")



def verifica_senha():
    if senha == senha_correta:
        return True
    else:
        return False
    

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/conversor', methods=['POST'])
def conversor():
    global senha
    senha = request.form.get('senha')
    if verifica_senha():
        return render_template('conversor.html')
    else:
        return redirect(url_for('index'))

@app.route('/converter', methods=['POST'])
def converter():
    if verifica_senha():
        global url
        url = request.form.get('inputURL')
        yt = YouTube(str(request.form.get('inputURL')).strip())
        return render_template('conversor.html', dados=yt)
    else:
        return redirect(url_for('index'))
# tem que verificar a possibilidade de usar a imagem não esta utilizando para não sobrecarrergar o servidor
    
@app.route('/converter_mp3', methods=['POST'])
def converter_mp3():
    if verifica_senha():
        global url
        yt = YouTube(str(url).strip())
        audio_download = yt.streams.filter(only_audio=True).first()
        filename = yt.title+".mp3"
        out_file = audio_download.download(filename)

        return send_file(out_file, as_attachment=True, download_name=filename)
        #metodo funcionando corretamente
    else:
        return redirect(url_for('index'))
    
@app.route('/converter_mp4', methods=['POST'])
def converter_mp4():
    if verifica_senha():
        global url
        yt = YouTube(str(url).strip())
        audio_download = yt.streams.get_highest_resolution()
        filename = yt.title+".mp4"
        audio_download.download(filename)
        definir_permissao_pasta(filename, '755')
        return send_file(filename, as_attachment=True, download_name=filename)
        #termina de realizar o download ele so está fazendo download no servidor e não no cliente
        # erro : PermissionError: [Errno 13] Permission denied: 'C:\\xampp\\htdocs\\python\\NTube\\Super Mario World Game Over LoFi Hip Hop Remix.mp4'
    else:
        return redirect(url_for('index'))





if __name__ == '__main__':
    app.run(debug=True)
