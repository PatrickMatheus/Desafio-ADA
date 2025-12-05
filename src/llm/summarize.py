from src.llm.model import carregar_modelo_llm
from src.utils.logs import logger

def quebrar_texto(texto: str, chunck_size = 4000) :
    """
    Recebe um texto e quebra em pedaços de 4000 caracteres
    """
    pedacos_texto = []
    for i in range(0, len(texto), chunck_size):
        pedaco = texto[i: i + chunck_size]
        pedacos_texto.append(pedaco)
    
    return pedacos_texto

def resumo_pdf(texto: str):
    if not texto.strip():
        logger.error("Não há texto suficiente para o resumo")
        return "Não foi possível gerar resumo (Texto insuficiente ou arquivo corrompido)"

    meu_modelo = carregar_modelo_llm()

    lista_de_pedacos = quebrar_texto(texto, chunck_size=12000)
    logger.info(f"O texto foi dividido em {len(lista_de_pedacos)} partes")

    resumos_parciais = []

    for i, pedaco in enumerate(lista_de_pedacos):
        logger.info(f"processando parte {i+1}")

        mensagem = [
            {"role":"system", "content": "Você é um assistente especialista em resumos. Responda sempre em Português do Brasil."},
            {"role": "user", "content": f"RResuma o seguinte texto de forma direta:\n\n{pedaco}"}
        ]

        try:
            resposta = meu_modelo(
                mensagem,
                max_new_tokens = 300,
                do_sample = False,
            )
            texto_resumido = resposta[0]['generated_text'][-1]['content']
            resumos_parciais.append(texto_resumido)
        
        except Exception as erro:
            logger.error(f"erro na parte {i+1}: {erro}")
    
    texto_intermediario = "\n\n".join(resumos_parciais)

    if len(texto_intermediario) > 25000:
        lista_sub_pedacos = quebrar_texto(texto_intermediario, chunck_size=12000)
        logger.info("Diminuindo o tamanho do texto-resumo")

        sub_resumos = []
        for sub in lista_sub_pedacos:
             mensagem_sub = [
                {"role":"system", "content": "Você é um assistente especialista em resumos. Responda sempre em PT-BR (Português do Braasil)."},
                {"role": "user", "content": f"RResuma o seguinte texto de forma direta:\n\n{pedaco}"}
             ]
             sub_resposta = meu_modelo(
                mensagem_sub,
                max_new_tokens=250,
                do_sample=False
             )
             sub_resumos.append(sub_resposta[0]['generated_text'][-1]['content'])
        
        texto_intermediario = "\n\n ".join(sub_resumos)


    if len(lista_de_pedacos) > 1:
        resumo_final = [
            {"role":"system", "content": "Você é um redator técnico sênior. Sua tarefa é criar um texto final em português."},
            {"role": "user", "content": f"""
            Junte todos esses resumos parciais em um resumo executivo coeso e fluido
            O texto final deve ter no máximo 4 parágrafos e estar em PT-BR
            ----INICIO DOS RESUMOS----
                {texto_intermediario}
            ---- FIM DOS RESUMOS ----

            Resumo final:
            """}
        ]
        try:
            resultado_final = meu_modelo(resumo_final, max_new_tokens=500, do_sample = False)
            resumo_final = resultado_final[0]['generated_text'][-1]['content']
        except Exception as e:
            logger.error(f"Ocorreu um erro na produção do resumo: {e}")
        return resumo_final
    
    return texto_intermediario
