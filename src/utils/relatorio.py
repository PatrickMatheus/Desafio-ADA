import os
from datetime import datetime
from src.utils.logs import logger

def salvar_em_markdown(caminho_pdf, dados, qtd_img, pasta_img, resumo):
    """
    Salva todas as informações em arquivo .md
    """
    nome_arquivo = os.path.basename(caminho_pdf)
    no_extension = os.path.splitext(nome_arquivo)[0]

    # Adiciona data e hora para não confundir com relatórios antigos
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M")
    nome_relatorio = f"relatorio_{no_extension}_{data_hora}.md"

    conteudo = f"""# Relatório de Análise: {nome_arquivo}
**Data da geração:** {datetime.now().strftime("%d/%m/%Y às %H:%M")}

---

## 1. Estatísticas Gerais
| Métrica | Valor |
| :--- | :--- |
| **Tamanho do Arquivo** | {(dados['Tamanho do arquivo'])} |
| **Total de Páginas** | {dados['Numero de paginas']} |
| **Total de Palavras** | {dados['Numero total de palavras']} |
| **Vocabulário Único** | {dados['Tamanho do vocabulário']} palavras |

### 10 Palavras Mais Frequentes
"""
    for palavra, qtd in dados['10 palavras mais comuns']:
        conteudo += f"- **{palavra}**: {qtd} vezes\n"

    conteudo += f"""
---

## 2. Imagens Extraídas
- **Quantidade encontrada:** {qtd_img}
- **Pasta de destino:** `{pasta_img}`

---

## 3. Resumo Inteligente (IA)
> Resumo gerado automaticamente pelo modelo Qwen2-1.5B (Local).

{resumo}
"""

    try:
        with open(nome_relatorio, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
        return nome_relatorio
    except Exception as e:
        logger.error(f"Erro ao salvar relatório: {e}")
        return None