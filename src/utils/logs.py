import logging
import sys

def config_logger():
    """
    Configura o sistema de logger para salvar os logs em um arquivo
    Além de mostrar no terminal
    """

    logger = logging.getLogger("DesafioADA")
    logger.setLevel(logging.DEBUG)

    #evitando duplicação de logs
    if logger.handlers:
        return logger
    
    #criando um handler especifico para escrever no arquivo.log
    file_handler = logging.FileHandler("ADA.log", encoding='utf-8') #evitar problemas com acentos.
    file_handler.setLevel(logging.DEBUG)

    formato_arquivo = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formato_arquivo)
    
    #logs mostrados também no terminal
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    formato_console = logging.Formatter("%(message)s")
    console_handler.setFormatter(formato_console)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


    return logger


logger = config_logger()