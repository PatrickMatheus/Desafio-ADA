import argparse

def config_args():
    """ 
    Configura e retorna os argumentos
    da linha de comando
    """

    parser = argparse.ArgumentParser(
        description="Ferramenta para análise de PDF"
    )

    parser.add_argument(
        "pdf_path",
        type=str,
        help="Caminho para o PDF que será analisado"
    )

    parser.add_argument(
        "--output",
        type=str,
        default="images",
        help="Onde as imagens extraídas serão salvas (padrão->imagens/)"
    )

    return parser.parse_args()


