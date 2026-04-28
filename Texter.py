import json
import os

# Arquivo onde as artes serão salvas
ARQUIVO_ARTES = "artes.json"

# Arquivo onde as configurações serão salvas
ARQUIVO_CONFIGS = "configs.json"

# Função para carregar as artes do arquivo
def carregar_artes():
    if os.path.exists(ARQUIVO_ARTES):
        with open(ARQUIVO_ARTES, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"gato": "teste", "cachorro": "teste 2"}  # Artes padrão

# Função para salvar as artes no arquivo
def salvar_artes(artes):
    with open(ARQUIVO_ARTES, "w", encoding="utf-8") as f:
        json.dump(artes, f, ensure_ascii=False, indent=2)

# Função para carregar as configurações
def carregar_configs():
    if os.path.exists(ARQUIVO_CONFIGS):
        with open(ARQUIVO_CONFIGS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"confirmar_antes_deletar": True}  # Configurações padrão

# Função para salvar as configurações
def salvar_configs(configs):
    with open(ARQUIVO_CONFIGS, "w", encoding="utf-8") as f:
        json.dump(configs, f, ensure_ascii=False, indent=2)

# Carregar artes e configurações no início
artes = carregar_artes()
configs = carregar_configs()

while True:
    print(" ____________  _________  ____  ____  ____________  _________  ____________")
    print("/___    ____/ /   _____/ /   / /   / /___    ____/ /   _____/ /   ____    /")
    print("   /   /     /   /____   |   |/   /     /   /     /   /____  /   /___/   /")
    print("  /   /     /   _____/  /   _    |     /   /     /   _____/ /   _    ___/")
    print(" /   /     /   /____   /   / |   |    /   /     /   /____  / - / \\   \\ ")
    print("/___/     /________/  /___/  |___|   /___/     /________/ /___/   \\___\\ ")
    print(" ")
    print("Olá, seja bem vindo ao texter! Escolha o que quer fazer:")
    print(" ")
    print("ver - Visualizador de artes de texto (apenas leitura)")
    print("edt - Editor de artes de texto (editar/deletar)")
    print("new - Criar nova arte de texto (text art)")
    print("cfg - Configurações")
    print(" ")
    print("exit - Sair do programa")
    print(" ")
    opcao = input("digite a opção desejada:")
    print(" ")
    
    # ======================== VISUALIZADOR ========================
    if opcao == "ver":
        while True:
            print(" ")
            print("qual arte você quer ver?")
            print(" ")
            
            # Mostrar as artes disponíveis dinamicamente
            for i, nome_arte in enumerate(artes.keys(), 1):
                print(f"{i} - {nome_arte}")
            print(" ")
            print("vol - voltar ao menu principal")
            print(" ")
            opcao_ver = input("digite a opção desejada:")
            print(" ")
            
            if opcao_ver == "vol":
                print("voltando ao menu principal\n")
                break
            elif opcao_ver in artes:
                nome_arte = opcao_ver
                print(f"Aqui está a arte de texto: \"{nome_arte}\":")
                print(" ")
                print(artes[nome_arte])
                print(" ")
            else:
                # Tenta como número
                try:
                    idx = int(opcao_ver) - 1
                    nome_arte = list(artes.keys())[idx]
                    print(f"Aqui está a arte de texto: \"{nome_arte}\":")
                    print(artes[nome_arte])
                    print(" ")
                except:
                    print("Opção inválida! Tente novamente.\n")
    
    # ======================== EDITOR ========================
    elif opcao == "edt":
        while True:
            print(" ")
            print("qual arte você quer editar?")
            print(" ")
            
            # Mostrar as artes disponíveis dinamicamente
            for i, nome_arte in enumerate(artes.keys(), 1):
                print(f"{i} - {nome_arte}")
            print(" ")
            print("vol - voltar ao menu principal")
            print(" ")
            opcao_edt = input("digite a opção desejada:")
            print(" ")
            
            if opcao_edt == "vol":
                print("voltando ao menu principal\n")
                break
            elif opcao_edt in artes:
                nome_selecionado = opcao_edt
            else:
                # Tenta como número
                try:
                    idx = int(opcao_edt) - 1
                    nome_selecionado = list(artes.keys())[idx]
                except:
                    print("Opção inválida! Tente novamente.\n")
                    continue
            
            # Submenu para a arte selecionada
            while True:
                print(f"\nArte: \"{nome_selecionado}\"")
                print(f"Conteúdo:\n{artes[nome_selecionado]}")
                print("\n1 - Ver arte")
                print("2 - Editar nome")
                print("3 - Editar conteúdo")
                print("4 - Deletar arte")
                print("5 - Voltar à lista de artes")
                print(" ")
                
                opcao_acao = input("digite a opção desejada:")
                print(" ")
                
                if opcao_acao == "1":
                    print(f"Aqui está a arte de texto: \"{nome_selecionado}\":")
                    print(artes[nome_selecionado])
                    print(" ")
                
                elif opcao_acao == "2":
                    novo_nome = input("Digite o novo nome da arte: ")
                    if novo_nome in artes and novo_nome != nome_selecionado:
                        print("Já existe uma arte com esse nome!\n")
                    else:
                        artes[novo_nome] = artes.pop(nome_selecionado)
                        salvar_artes(artes)
                        print(f"Nome alterado para \"{novo_nome}\" com sucesso!\n")
                        nome_selecionado = novo_nome
                
                elif opcao_acao == "3":
                    print("Digite as linhas do novo conteúdo (digite 'FIM' quando terminar):")
                    linhas = []
                    while True:
                        linha = input()
                        if linha.upper() == "FIM":
                            break
                        linhas.append(linha)
                    
                    novo_conteudo = "\n".join(linhas)
                    artes[nome_selecionado] = novo_conteudo
                    salvar_artes(artes)
                    print("Conteúdo alterado com sucesso!\n")
                
                elif opcao_acao == "4":
                    if configs["confirmar_antes_deletar"]:
                        confirmacao = input(f"Tem certeza que quer deletar a arte \"{nome_selecionado}\"? (s/n): ")
                        if confirmacao.lower() == "s":
                            del artes[nome_selecionado]
                            salvar_artes(artes)
                            print("Arte deletada com sucesso!\n")
                            break
                        else:
                            print("Deleção cancelada.\n")
                    else:
                        del artes[nome_selecionado]
                        salvar_artes(artes)
                        print("Arte deletada com sucesso!\n")
                        break
                
                elif opcao_acao == "5":
                    break
                else:
                    print("Opção inválida! Tente novamente.\n")
    
    # ======================== CRIAR NOVA ARTE ========================
    elif opcao == "new":
        nome_arte = input("Digite o nome da arte de texto: ")
        print("Digite as linhas da arte (digite 'FIM' quando terminar):")
        linhas = []
        while True:
            linha = input()
            if linha.upper() == "FIM":
                break
            linhas.append(linha)
        
        arte = "\n".join(linhas)
        artes[nome_arte] = arte
        salvar_artes(artes)
        print("Arte de texto criada com sucesso!\n")
    
    # ======================== CONFIGURAÇÕES ========================
    elif opcao == "cfg":
        while True:
            print(" ")
            print("Selecione a configuração que deseja alternar:")
            print(" ")
            print("1 - Confirmar antes de deletar:", "SIM" if configs["confirmar_antes_deletar"] else "NÃO")
            print(" ")            
            print("vol - Voltar ao menu principal")
            print(" ")
            
            opcao_cfg = input("Digite a opção desejada: ")
            print(" ")
            
            if opcao_cfg == "1":
                configs["confirmar_antes_deletar"] = not configs["confirmar_antes_deletar"]
                salvar_configs(configs)
                novo_estado = "SIM" if configs["confirmar_antes_deletar"] else "NÃO"
                print(f"Configuração alterada para: {novo_estado}\n")
            
            elif opcao_cfg == "vol":
                print("Voltando ao menu principal\n")
                break
            
            else:
                print("Opção inválida! Tente novamente.\n")
                
    # ======================== CONFIGURAÇÕES ========================
    elif opcao == "exit":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.\n")
