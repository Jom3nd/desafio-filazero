from tests.test_provisionamento import test_processar
from tests.test_slug import test_slug
from tests.test_viacep import test_viacep_service


def main():
    testes = [
        ("Processamento", test_processar),
        ("Slug", test_slug),
        ("ViaCEP", test_viacep_service),
    ]

    sucessos = 0

    print("========== EXECUÇÃO DOS TESTES ==========\n")

    for nome, teste in testes:
        try:
            teste()
            print(f"[OK] {nome}")
            sucessos += 1

        except AssertionError as erro:
            print(f"[FALHOU] {nome}")
            if erro:
                print(f"  Motivo: {erro}")

        except Exception as erro:
            print(f"[ERRO] {nome}")
            print(f"  Motivo: {erro}")

    print("\n========== RESUMO ==========")
    print(f"Testes executados: {len(testes)}")
    print(f"Testes aprovados: {sucessos}")
    print(f"Testes com falha: {len(testes) - sucessos}")


if __name__ == "__main__":
    main()