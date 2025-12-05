import os
import fitz
from collections import Counter
from src.utils.text import obter_palavras_válidas

def extrair_dados (dir_pdf: str) -> dict:
    """
    Lê o arquivo pdf e retorna um dicionário com estatísticas do texto
    """

    relatorio = {}

    tamanho_em_bytes = os.path.getsize(dir_pdf)
    relatorio["Tamanho do arquivo"] = tamanho_em_bytes

    try:
        documento_pdf = fitz.open(dir_pdf)
    except Exception as erro:
        raise ValueError(f"Erro ao abrir arquivo: {erro}")

    total_pages = documento_pdf.page_count

    texto_pdf_completo = ""

    for pagina in documento_pdf:
        texto_pdf_completo += pagina.get_text() + "\n"

    documento_pdf.close()

    lista_palavras = obter_palavras_válidas(texto_pdf_completo)

    qtd_total_palavras = len(lista_palavras)

    tamanho_vocabulario = len(set(lista_palavras))

    frequencia_palavras = Counter(lista_palavras)

    dez_mais_freq = frequencia_palavras.most_common(10)

    relatorio["Numero de paginas"] = total_pages
    relatorio["Numero total de palavras"] = qtd_total_palavras
    relatorio["10 palavras mais comuns"] = dez_mais_freq
    relatorio["Tamanho do vocabulário"] = tamanho_vocabulario
    relatorio["Texto completo"] = texto_pdf_completo


    return relatorio