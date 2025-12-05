import os
from queue import Full
import fitz

def extrair_imagens(caminho_pdf: str, saida: str) -> tuple[int, str]:
    """
    Percorre todo o PDF e extrai todas as imagens e as salva em uma pasta.
    Retorna o número total de imagens salvas e o caminho da pasta
    """

    nome_arquivo = os.path.basename(caminho_pdf)
    
    #Pegar o arquivo sem a extensão
    no_extension = os.path.splitext(nome_arquivo)[0]

    pasta_destino = os.path.join(saida, no_extension)

    os.makedirs(pasta_destino, exist_ok=True)

    documento_pdf = fitz.open(caminho_pdf)
    cont_imagens = 0

    for ind_page, pagina in enumerate(documento_pdf):
        
        # pegar a lista de todas as imagens na pagina
        lista_imagens = pagina.get_images(full=True)

        for ind_img, info_image in enumerate(lista_imagens):
            xref = info_image[0]
            dados_imagem = documento_pdf.extract_image(xref)
            bytes_image = dados_imagem["image"]
            extension_image = dados_imagem["ext"]

            nome_salvar = f"pag{ind_page + 1}_img{ind_img + 1}.{extension_image}"
            caminho_salvar = os.path.join(pasta_destino, nome_salvar)

            with open(caminho_salvar, "wb") as arquivo_image:
                arquivo_image.write(bytes_image)
            
            cont_imagens += 1
    
    documento_pdf.close()

    return cont_imagens, pasta_destino
