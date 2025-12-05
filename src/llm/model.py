from enum import auto
import torch
from  transformers import pipeline
from src.utils.logs import logger


def carregar_modelo_llm():
    """
    Carrega o modelo Qwen2-1.5B-instruct
    """

    logger.info("Verificando hardware...")

    device = "cuda" if torch.cuda.is_available() else "cpu"

    if device == "cuda":
        logger.info(f"GPU detectada: {torch.cuda.get_device_name(0)}")
    else:
        logger.warning("Não foi encontrada GPU")

    print("carregando modelo...")
    llm_model = "Qwen/Qwen2-1.5B-Instruct"

    gerador_resumo = pipeline(
        "text-generation",
        model = llm_model,
        tokenizer = llm_model,
        dtype = torch.float16 if device == "cuda" else torch.float32,
        device_map = "auto"
    )

    return gerador_resumo