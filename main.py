import os, sys
from src.cli.arguments import config_args
from src.pdf.extractor import extrair_dados
from src.pdf.images import extrair_imagens
from src.llm.summarize import resumo_pdf
from src.utils.relatorio import salvar_em_markdown
from src.utils.logs import logger

def main():

    args = config_args()

    dir_arquivo_pdf = args.pdf_path
    dir_saida = args.output

    if not os.path.exists(dir_arquivo_pdf):
        logger.fatal(f"Erro: O arquivo '{dir_arquivo_pdf}' não foi encontrado.")
        return 

    print("Iniciando análise do arquivo PDF...\n")
    try:
        dados_pdf = extrair_dados(dir_arquivo_pdf)

        logger.info("Relatório do arquivo PDF: \n")

        logger.info(f"Tamanho em disco: {dados_pdf['Tamanho do arquivo']}")
        logger.info(f"Total de páginas do arquivo: {dados_pdf['Numero de paginas']}")
        logger.info(f"Quantidade de palavras: {dados_pdf['Numero total de palavras']}")
        logger.info(f"Vocabulário único: {dados_pdf['Tamanho do vocabulário']}")

        logger.info("Iniciando extração de imagens...")

        qtd_imagens, pasta_saida = extrair_imagens(dir_arquivo_pdf, dir_saida)
        if qtd_imagens > 0:
            logger.info("Imagens extraídas com sucesso!!\n")
            logger.info(f"Foram extraídas {qtd_imagens} imagens")
            logger.info(f"Foram salvas em {pasta_saida}")
        else:
            logger.info("Nenhuma imagem foi encontrada nesse PDF.")

        logger.info("Gerando resumo com o modelo LLM...")
        texto_para_resumir = dados_pdf['Texto completo']

        resumo = resumo_pdf(texto_para_resumir)
        
        logger.info("Resumo gerado pelo modelo: ")
        print("-"*40)
        logger.info(resumo)
        print("-"*40)

        logger.info("Salvando o relatório em um arquivo...")
        relatorio = salvar_em_markdown(dir_arquivo_pdf, dados_pdf, qtd_imagens, pasta_saida, resumo)


    except KeyboardInterrupt:
        logger.warning("Operação cancelada manualmente!")
        sys.exit(0)

    except Exception as erro:
        logger.error(f"Ocorreu um erro inesperado: {erro}")

if __name__ == "__main__":
    main()