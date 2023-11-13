import os

# Diretório onde os arquivos .mp4 de entrada estão localizados
diretorio_entrada = 'input'

# Diretório onde os arquivos combinados serão salvos
diretorio_saida = 'output'

# Crie o diretório de saída se não existir
os.makedirs(diretorio_saida, exist_ok=True)

# Lista todos os arquivos .mp4 na pasta de entrada
arquivos_mp4 = [f for f in os.listdir(diretorio_entrada) if f.endswith('.mp4')]

# Itera sobre os arquivos e combina vídeo com áudio
for arquivo in arquivos_mp4:
    # Obtém o número do vídeo
    numero = arquivo.split('.')[0]

    # Caminhos para os arquivos de entrada (input) e saída (output)
    video_path = os.path.join(diretorio_entrada, f"{numero}.mp4")
    audio_path = os.path.join(diretorio_entrada, f"{numero}.1.mp4")
    output_path = os.path.join(diretorio_saida, f"{numero}_combinado.mp4")

    # Usa o comando ffmpeg para combinar vídeo e áudio
    command = f"ffmpeg -i {video_path} -i {audio_path} -c:v libx264 -c:a aac -strict experimental {output_path}"
    os.system(command)
