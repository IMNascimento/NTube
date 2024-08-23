import datetime
import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from urllib.request import urlretrieve
from core.ntube import YouTube



app = Flask(__name__)


@app.route('/')
def index():
    try:
        ip = request.remote_addr
        port = request.environ.get('REMOTE_PORT')
        with open('visit.txt', 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f'[INDEX] [{timestamp}] Acesso de {ip}:{port}\n')
        return render_template('conversor.html')
    except Exception as e:
        with open('log.txt', 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f'[ERRO] [{timestamp}] Ocorreu um erro: {str(e)}\n')
        return render_template('500.html')

@app.route('/converter', methods=['POST'])
def converter():
    try:
        ip = request.remote_addr
        port = request.environ.get('REMOTE_PORT')
        with open('visit.txt', 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f'[CONVERTER] [{timestamp}] Acesso de {ip}:{port}\n')
        global url
        url = request.form.get('inputURL')
        yt = YouTube(str(request.form.get('inputURL')).strip())
        return render_template('conversor.html', dados=yt)
    except Exception as e:
        with open('log.txt', 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f'[ERRO] [{timestamp}] Ocorreu um erro: {str(e)}\n')
        return render_template('500.html')


    
@app.route('/converter_mp3', methods=['POST'])
def converter_mp3():
    try:
        ip = request.remote_addr
        port = request.environ.get('REMOTE_PORT')
        with open('visit.txt', 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f'[CONVERTER_MP3] [{timestamp}] Acesso de {ip}:{port}\n')

        global url
        yt = YouTube(str(url).strip())
        audio_download = yt.streams.filter(only_audio=True).first()
        filename = yt.title+".mp3"
        out_file = audio_download.download(output_path="download", filename=filename)

        return send_file(out_file, as_attachment=True, download_name=filename)
    except Exception as e:
        with open('log.txt', 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f'[ERRO] [{timestamp}] Ocorreu um erro: {str(e)}\n')
        return render_template('500.html')
    

@app.route('/converter_mp4', methods=['POST'])
def converter_mp4():
    try:
        ip = request.remote_addr
        port = request.environ.get('REMOTE_PORT')
        with open('visit.txt', 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f'[CONVERTER_MP4] [{timestamp}] Acesso de {ip}:{port}\n')
        global url
        yt = YouTube(str(url).strip())
        audio_download = yt.streams.get_highest_resolution()
        filename = yt.title + ".mp4"
        out_file = audio_download.download(output_path="download", filename=filename)
        # Corrigindo o caminho do arquivo para enviar corretamente
        return send_file(os.path.join("download", filename), as_attachment=True, download_name=filename)
    except Exception as e:
        with open('log.txt', 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f'[ERRO] [{timestamp}] Ocorreu um erro: {str(e)}\n')
        return render_template('500.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
