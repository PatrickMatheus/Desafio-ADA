# Analisador de PDF com IA (Desafio ADA)

Ferramenta de linha de comando (CLI) desenvolvida para o processo seletivo ADA. O projeto processa arquivos PDF, extrai metadados, imagens e gera um resumo inteligente utilizando uma LLM (Qwen2-1.5B) rodando localmente com aceleração de GPU.

## Funcionalidades Implementadas

### Obrigatórias
- **Análise Estatística**: Contagem de palavras, páginas, tamanho e vocabulário.
- **Extração de Imagens**: Salva imagens automaticamente em pastas organizadas.
- **Resumo com LLM Local**: Integração com Hugging Face (Qwen2) para gerar resumos em português.

### Extras (Diferenciais)
- **Otimização de GPU**: processamento em "chunks" (pedaços) para suportar PDFs gigantes sem estourar a VRAM.
- **Logs e tratamento de arquivos**: Sistema de logging e tratamento de exceções para arquivos corrompidos ou inválidos.
- **Relatório Unificado**: Geração de um arquivo `.md` final com todas as análises.

## 🛠️ Como rodar o projeto

### Pré-requisitos
- Python 3.11 (Recomendado).
- Placa de Vídeo NVIDIA (Opcional, mas recomendado para performance).

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/PatrickMatheus/Desafio-ADA.git
   cd desafio_ADA

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
3. Instale as depedências:
   ```bash
   pip install -r requirements.txt
obs: As dependências já estão com a vesão com suporta a CUDA para uso de GPU, mas se não funcionar, use:
  ```bash
  pip install torch torchvision --index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)
```
## Uso
1. Para executar o projeto:
   ```bash
   python main.py seu_arquivo.pdF
Opcionalmente, se quiser um caminho de saída diferente:
   ```bash
   python main.py seu_arquivo.pdf --output sua_saida
   ```
```bash
   Exemplo: python main.py teste.pdf --output saida
```

2. Para ver as opções de ajuda:
   ```bash
   python main.py --help

Para a avaliação eu gostaria que levassem em conta o tratamento de erros por log (Logger):
O código foi feito para conseguir lidar com arquivos PDFs grandes, corrompidos, vazios e 
interrupções manuais. Além da modularização do projeto, mostrando uma pequena separação de 
responsabilidades (cli, llm, pdf, utils)


Desenvolvido por Patrick Matheus Freitas de Lima




