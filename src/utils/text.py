import re

STOPWORDS = {
    "a", "o", "e", "é", "de", "do", "da", "em", "um", "uma", "para", "com", "não", 
    "que", "os", "as", "dos", "das", "se", "na", "no", "por", "mais", "como", "mas", "ao", "aos"
}

def obter_palavras_válidas(texto: str) -> list[str]:
    """
    Recebe um texto bruto e remove as stopwords e pontuações
    retornando uma lista com as palavras válidas do texto
    """

    if not texto:
        return []

    texto_minusculo = texto.lower()
    lista_palavras = re.findall(r'\b\w+\b', texto_minusculo)

    lista_filtrada = []
    for palavra in lista_palavras:
        if (palavra not in STOPWORDS and not palavra.isdigit() and len(palavra) > 1):
            lista_filtrada.append(palavra)
    
    return lista_filtrada
