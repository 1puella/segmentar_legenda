import os
import re
from tkinter import Tk, filedialog, messagebox

# Lista de palavras que não devem ficar no final de uma linha
nao_quebrar_apos = {
    "D.", "D.ª", "Dr", "Dr.", "Dr.ª", "Dra.", "Exmo.", "Frei", "Jr.", "Miss",
    "Mna.", "Mno.", "P.", "Pe.", "Prof.", "Prof.ª", "Santa", "Santo", "Sr", "Sr.",
    "Sr.ª", "Sra.", "Srs.", "Srta.", "St.", "a", "antes", "ao", "aos", "as", "assim",
    "até", "com", "como", "conforme", "contra", "contudo", "da", "das", "de", "decr.",
    "desde", "do", "dos", "dr.ª", "e", "em", "enquanto", "entanto", "entre", "essa",
    "essas", "esse", "esses", "exceto", "exmo.", "frei", "gram.", "jr.", "logo", "mas",
    "me", "meu", "meus", "minha", "minhas", "mna.", "mno.", "mr.", "mrs.", "na", "nas",
    "nem", "nessa", "nessas", "nesse", "nesses", "nesta", "nestas", "neste", "nestes",
    "no", "nos", "não", "o", "ora", "os", "ou", "para", "pe.", "pela", "pelas", "pelo",
    "pelos", "pois", "por", "por que", "porque", "porém", "pra", "prof.", "prof.ª",
    "quando", "quanto", "que", "quem", "se", "sem", "seu", "seus", "sim", "sobre",
    "srs.", "sua", "suas", "tanto", "te", "todavia", "tão", "um", "uma", "umas", "uns",
    "vol.", "vols.", "à", "às", "já"
}

# Ajusta a segmentação de legenda entre blocos (e não entre linhas)
def ajustar_blocos_legenda(texto_legenda):
    blocos = texto_legenda.strip().split("\n\n")
    blocos_ajustados = []

    for i, bloco in enumerate(blocos):
        linhas = bloco.splitlines()

        # Ajustar a última palavra do bloco atual para o próximo bloco
        if len(linhas) > 1:
            ultima_palavra = re.search(r'\s(\w+)$', linhas[-1])
            if ultima_palavra:
                palavra = ultima_palavra.group(1)

                if palavra in nao_quebrar_apos or re.search(r'[.,?]\s+' + palavra + '$', linhas[-1]):
                    linhas[-1] = re.sub(r'\s' + palavra + '$', '', linhas[-1])

                    if i + 1 < len(blocos):
                        linhas_proximo = blocos[i + 1].splitlines()
                        linhas_proximo[1] = palavra + " " + linhas_proximo[1] if len(linhas_proximo) > 1 else palavra
                        blocos[i + 1] = "\n".join(linhas_proximo)

        # Ajustar a primeira palavra do bloco atual para o bloco anterior
        if i > 0:
            palavras_primeira_linha = re.split(r'\s+', linhas[1])
            if len(palavras_primeira_linha) > 1:
                primeira_palavra = palavras_primeira_linha[0]
                segunda_palavra = palavras_primeira_linha[1]

                if re.search(r'[,?.]', primeira_palavra[-1]) and (primeira_palavra[-1] != ',' or segunda_palavra[-1] != ','):
                    if primeira_palavra[-1] != ',' or not primeira_palavra[0].isupper():
                        linhas[1] = " ".join(palavras_primeira_linha[1:])

                        bloco_anterior = blocos_ajustados.pop()
                        linhas_anterior = bloco_anterior.splitlines()
                        linhas_anterior[-1] += " " + primeira_palavra
                        blocos_ajustados.append("\n".join(linhas_anterior))

        blocos_ajustados.append("\n".join(linhas))

    return "\n\n".join(blocos_ajustados)

# Processa os arquivos de legenda na pasta selecionada
def processar_arquivos_vtt(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.vtt'):
            caminho_arquivo = os.path.join(pasta, arquivo)
            with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                texto_legenda = file.read()

            texto_ajustado = ajustar_blocos_legenda(texto_legenda)

            caminho_saida = caminho_arquivo.replace('.vtt', '_ajustado.vtt')
            with open(caminho_saida, 'w', encoding='utf-8') as file:
                file.write(texto_ajustado)

    messagebox.showinfo("Concluído", "Todos os arquivos foram processados e salvos com '_ajustado'.")

# Função para selecionar a pasta e iniciar o processamento
def selecionar_pasta():
    root = Tk()
    root.withdraw()
    caminho_pasta = filedialog.askdirectory(initialdir="C:/", title="Escolha um diretório para processar os arquivos de legenda")
    root.destroy()

    if not caminho_pasta:
        messagebox.showwarning("Aviso", "A seleção de diretório foi cancelada.")
    else:
        processar_arquivos_vtt(caminho_pasta)

# Executar a aplicação
if __name__ == "__main__":
    selecionar_pasta()
