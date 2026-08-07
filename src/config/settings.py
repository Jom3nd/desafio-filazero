import logging
import os

#Configuração da automação
VIACEP_BASE_URL = "https://viacep.com.br/ws"

#Configuração dos diretórios
OUTPUT_DIR = "output"
LOG_DIR = "logs"

os.makedirs(OUTPUT_DIR,exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)


#Configuração dos logs

logging.basicConfig(
    filename=f"{LOG_DIR}/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)