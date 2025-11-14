CAPACIDADE_CAIXA = 10


def ler_float(texto):
    while True:
        valor = input(texto).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Valor inválido, tente novamente.")


def avaliar_peca(peso, cor, comprimento):
    motivos = []
    if peso < 95 or peso > 105:
        motivos.append("peso fora do padrao")
    if cor not in ("azul", "verde"):
        motivos.append("cor fora do padrao")
    if comprimento < 10 or comprimento > 20:
        motivos.append("comprimento fora do padrao")
    aprovada = len(motivos) == 0
    return aprovada, motivos


def montar_caixas(pecas):
    caixas_fechadas = []
    caixa_atual = []
    for peca in pecas:
        if peca["aprovada"]:
            caixa_atual.append(peca["id"])
            if len(caixa_atual) == CAPACIDADE_CAIXA:
                caixas_fechadas.append(caixa_atual)
                caixa_atual = []
    return caixas_fechadas, caixa_atual


def cadastrar_peca(pecas):
    print("\n=== Cadastro de peça ===")
    peca_id = input("Id da peça: ").strip()
    if not peca_id:
        print("Id não pode ficar vazio.")
        return False
    for item in pecas:
        if item["id"] == peca_id:
            print("Ja existe uma peça com esse id.")
            return False
    peso = ler_float("Peso (g): ")
    cor = input("Cor: ").strip().lower()
    comprimento = ler_float("Comprimento (cm): ")
    aprovada, motivos = avaliar_peca(peso, cor, comprimento)
    peca = {
        "id": peca_id,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "aprovada": aprovada,
        "motivos": motivos,
    }
    pecas.append(peca)
    if aprovada:
        print("Peça aprovada e enviada para armazenamento.")
    else:
        print("Peça reprovada.")
        if motivos:
            print("Motivos: " + ", ".join(motivos))
    return True


def listar_pecas(pecas):
    if not pecas:
        print("\nNenhuma peça cadastrada.")
        return
    print("\n=== Peças aprovadas ===")
    encontrou = False
    for peca in pecas:
        if peca["aprovada"]:
            encontrou = True
            print(
                f"- {peca['id']} | {peca['peso']}g | {peca['cor']} | {peca['comprimento']}cm"
            )
    if not encontrou:
        print("Nenhuma peça aprovada.")
    print("\n=== Peças reprovadas ===")
    encontrou = False
    for peca in pecas:
        if not peca["aprovada"]:
            encontrou = True
            motivos = ", ".join(peca["motivos"]) if peca["motivos"] else "sem motivo"
            print(f"- {peca['id']} | motivos: {motivos}")
    if not encontrou:
        print("Nenhuma peça reprovada.")


def remover_peca(pecas):
    alvo = input("\nId da peca que deseja remover: ").strip()
    for indice in range(len(pecas)):
        if pecas[indice]["id"] == alvo:
            removida = pecas.pop(indice)
            print(f"Peça {removida['id']} removida.")
            return True
    print("Peça nao encontrada.")
    return False


def listar_caixas(caixas_fechadas):
    print("\n=== Caixas fechadas ===")
    if not caixas_fechadas:
        print("Nenhuma caixa fechada.")
        return
    for numero in range(len(caixas_fechadas)):
        itens = ", ".join(caixas_fechadas[numero])
        print(f"Caixa {numero + 1}: {itens}")


def gerar_relatorio(pecas, caixas_fechadas, caixa_aberta):
    aprovadas = 0
    reprovadas = 0
    for peca in pecas:
        if peca["aprovada"]:
            aprovadas += 1
        else:
            reprovadas += 1
    print("\n=== Relatorio final ===")
    print(f"Total de peças aprovadas: {aprovadas}")
    print(f"Total de peças reprovadas: {reprovadas}")
    if reprovadas > 0:
        print("\nMotivos das reprovacoes:")
        for peca in pecas:
            if not peca["aprovada"]:
                motivos = (
                    ", ".join(peca["motivos"]) if peca["motivos"] else "sem motivo"
                )
                print(f"- {peca['id']}: {motivos}")
    total_caixas = len(caixas_fechadas)
    if len(caixa_aberta) > 0:
        total_caixas += 1
    print(f"\nQuantidade de caixas utilizadas: {total_caixas}")
    if len(caixa_aberta) > 0:
        print("Caixa atual: " + ", ".join(caixa_aberta))


def mostrar_menu():
    print("\n=== Menu ===")
    print("1 - Cadastrar nova peça")
    print("2 - Listar peças aprovadas/reprovadas")
    print("3 - Remover peça cadastrada")
    print("4 - Listar caixas fechadas")
    print("5 - Gerar relatório final")
    print("0 - Sair")


def main():
    peças = []
    caixas_fechadas = []
    caixa_aberta = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ").strip()
        if opcao == "1":
            if cadastrar_peca(peças):
                caixas_fechadas, caixa_aberta = montar_caixas(peças)
        elif opcao == "2":
            listar_pecas(peças)
        elif opcao == "3":
            if remover_peca(peças):
                caixas_fechadas, caixa_aberta = montar_caixas(peças)
        elif opcao == "4":
            listar_caixas(caixas_fechadas)
        elif opcao == "5":
            gerar_relatorio(peças, caixas_fechadas, caixa_aberta)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opcao inválida, tente novamente.")


if __name__ == "__main__":
    main()
