import json
import logging
import os
from src.config.settings import *
from dataclasses import asdict
from src.config.settings import OUTPUT_DIR
from src.services.provisionamento_service import ProvisionamentoService

def configurar_aplicacao():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

def main():

    configurar_aplicacao()
    
    resultado = ProvisionamentoService().processar("data/unidades.csv")

    unidades_json = [
        asdict(unidade)
        for unidade in resultado["unidades"]
    ]

    with open(
        f"{OUTPUT_DIR}/provisionamento.json",
        "w",
        encoding="utf-8"
    ) as arquivo:
        json.dump(unidades_json, arquivo, ensure_ascii=False, indent=4)

    relatorio = {
            "sucesso": len(resultado["unidades"]),
            "falhas": len(resultado["falhas"]),
            "errors": resultado["falhas"]
        }
    
    with open(
        f"{OUTPUT_DIR}/relatorio.json"
        , "w", encoding="utf-8"
    ) as arquivo:
        json.dump(relatorio, arquivo, ensure_ascii=False, indent=4)    

    print("==========RESUMO DO PROVISIONAMENTO==========")
    print(f"Unidades processadas com sucesso: {len(resultado['unidades'])}")
    print(f"Falhas: {len(resultado['falhas'])}")

    if resultado["falhas"]:

        print("\nFalhas encontradas:")

        for falha in resultado["falhas"]:
            print(
                f"- {falha['unidade']}: {falha['erro']}"
            )

    else:
        print("\nTodas as unidades foram processadas com sucesso!")


if __name__ == "__main__":
    main()
