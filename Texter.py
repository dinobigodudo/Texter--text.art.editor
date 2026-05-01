import json
import os

# Arquivo onde as artes serão salvas
ARQUIVO_ARTES = "artes_texter.json"

# Arquivo onde as configurações serão salvas
ARQUIVO_CONFIGS = "configs_texter.json"

# Dicionário de idiomas
IDIOMAS = {
    "pt": {
        "bem_vindo": "Olá, seja bem vindo ao texter! Escolha o que quer fazer:",
        "ver": "ver - Visualizador de artes de texto (apenas leitura)",
        "edt": "edt - Editor de artes de texto (editar/deletar)",
        "new": "new - Criar nova arte de texto (text art)",
        "cfg": "cfg - Configurações e acessibilidade",
        "exit": "exit - Sair do programa",
        "digite_opcao": "digite a opção desejada:",
        "qual_arte_ver": "qual arte você quer ver?",
        "vol": "vol - voltar ao menu principal",
        "arte_texto": "Aqui está a arte de texto:",
        "opcao_invalida": "Opção inválida! Tente novamente.",
        "voltando_menu": "voltando ao menu principal",
        "qual_arte_editar": "qual arte você quer editar?",
        "arte": "Arte:",
        "conteudo": "Conteúdo:",
        "ver_arte": "1 - Ver arte",
        "editar_nome": "2 - Editar nome",
        "editar_conteudo": "3 - Editar conteúdo",
        "deletar_arte": "4 - Deletar arte",
        "voltar_lista": "5 - Voltar à lista de artes",
        "novo_nome": "Digite o novo nome da arte:",
        "nome_existe": "Já existe uma arte com esse nome!",
        "nome_alterado": "Nome alterado para",
        "sucesso": "com sucesso!",
        "digite_linhas": "Digite as linhas do novo conteúdo (digite 'FIM' quando terminar):",
        "conteudo_alterado": "Conteúdo alterado com sucesso!",
        "tem_certeza_deletar": "Tem certeza que quer deletar a arte",
        "deletado_sucesso": "Arte deletada com sucesso!",
        "delecao_cancelada": "Deleção cancelada.",
        "criar_arte": "Digite o nome da arte de texto:",
        "arte_criada": "Arte de texto criada com sucesso!",
        "selecione_config": "Selecione a configuração que deseja alternar:",
        "confirmar_deletar": "1 - Confirmar antes de deletar:",
        "mudar_idioma": "2 - Alterar idioma:",
        "sim": "SIM",
        "nao": "NÃO",
        "alterado_para": "Configuração alterada para:",
        "saindo": "Saindo do programa...",
    },
    "en": {
        "bem_vindo": "Hello, welcome to texter! Choose what you want to do:",
        "ver": "ver - Text art viewer (read-only)",
        "edt": "edt - Text art editor (edit/delete)",
        "new": "new - Create new text art",
        "cfg": "cfg - Settings and accessibility",
        "exit": "exit - Exit program",
        "digite_opcao": "enter desired option:",
        "qual_arte_ver": "which art do you want to see?",
        "vol": "vol - back to main menu",
        "arte_texto": "Here is the text art:",
        "opcao_invalida": "Invalid option! Try again.",
        "voltando_menu": "going back to main menu",
        "qual_arte_editar": "which art do you want to edit?",
        "arte": "Art:",
        "conteudo": "Content:",
        "ver_arte": "1 - View art",
        "editar_nome": "2 - Edit name",
        "editar_conteudo": "3 - Edit content",
        "deletar_arte": "4 - Delete art",
        "voltar_lista": "5 - Back to art list",
        "novo_nome": "Enter the new name for the art:",
        "nome_existe": "An art with this name already exists!",
        "nome_alterado": "Name changed to",
        "sucesso": "successfully!",
        "digite_linhas": "Enter the lines of the new content (type 'END' when done):",
        "conteudo_alterado": "Content changed successfully!",
        "tem_certeza_deletar": "Are you sure you want to delete the art",
        "deletado_sucesso": "Art deleted successfully!",
        "delecao_cancelada": "Deletion cancelled.",
        "criar_arte": "Enter the name of the text art:",
        "arte_criada": "Text art created successfully!",
        "selecione_config": "Select the setting you want to change:",
        "confirmar_deletar": "1 - Confirm before deleting:",
        "mudar_idioma": "2 - Change language:",
        "sim": "YES",
        "nao": "NO",
        "alterado_para": "Setting changed to:",
        "saindo": "Exiting program...",
    }
}

# Função para carregar as artes do arquivo
def carregar_artes():
    if os.path.exists(ARQUIVO_ARTES):
        with open(ARQUIVO_ARTES, "r", encoding="utf-8") as f:
            return json.load(f)
            
    return {"cat": "                           ╱|、\n                          (˚ˎ 。7  \n                           |、˜〵          \n                           じしˍ,)ノ "}  # Arte padrão

# Função para salvar as artes no arquivo
def salvar_artes(artes):
    with open(ARQUIVO_ARTES, "w", encoding="utf-8") as f:
        json.dump(artes, f, ensure_ascii=False, indent=2)

# Função para carregar as configurações
def carregar_configs():
    if os.path.exists(ARQUIVO_CONFIGS):
        with open(ARQUIVO_CONFIGS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"confirmar_antes_deletar": True, "idioma": "pt"}  # Configurações padrão

# Função para salvar as configurações
def salvar_configs(configs):
    with open(ARQUIVO_CONFIGS, "w", encoding="utf-8") as f:
        json.dump(configs, f, ensure_ascii=False, indent=2)

# Carregar artes e configurações no início
artes = carregar_artes()
configs = carregar_configs()

# Função para obter texto traduzido (APÓS carregar configs)
def get_text(key):
    idioma = configs.get("idioma", "pt")
    return IDIOMAS[idioma].get(key, key)

while True:
    print(" ____________  _________  ____  ____  ____________  _________  ____________")
    print("/___    ____/ /   _____/ /   / /   / /___    ____/ /   _____/ /   ____    /")
    print("   /   /     /   /____   |   |/   /     /   /     /   /____  /   /___/   /")
    print("  /   /     /   _____/  /   _    |     /   /     /   _____/ /   _    ___/")
    print(" /   /     /   /____   /   / |   |    /   /     /   /____  / - / \\   \\ ")
    print("/___/     /________/  /___/  |___|   /___/     /________/ /___/   \\___\\ ")
    print(" ")
    print(get_text("bem_vindo"))
    print(" ")
    print(get_text("ver"))
    print(get_text("edt"))
    print(get_text("new"))
    print(get_text("cfg"))
    print(" ")
    print(get_text("exit"))
    print(" ")
    opcao = input(get_text("digite_opcao") + " ")
    print(" ")
    
    # ======================== VISUALIZADOR ========================
    if opcao == "ver":
        while True:
            print(" ")
            print(get_text("qual_arte_ver"))
            print(" ")
            
            # Mostrar as artes disponíveis dinamicamente
            for i, nome_arte in enumerate(artes.keys(), 1):
                print(f"{i} - {nome_arte}")
            print(" ")
            print(get_text("vol"))
            print(" ")
            opcao_ver = input(get_text("digite_opcao") + " ")
            print(" ")
            
            if opcao_ver == "vol":
                print(get_text("voltando_menu") + "\n")
                break
            elif opcao_ver in artes:
                nome_arte = opcao_ver
                print(f"{get_text('arte_texto')} \"{nome_arte}\":")
                print(" ")
                print(artes[nome_arte])
                print(" ")
            else:
                # Tenta como número
                try:
                    idx = int(opcao_ver) - 1
                    nome_arte = list(artes.keys())[idx]
                    print(f"{get_text('arte_texto')} \"{nome_arte}\":")
                    print(artes[nome_arte])
                    print(" ")
                except:
                    print(get_text("opcao_invalida") + "\n")
    
    # ======================== EDITOR ========================
    elif opcao == "edt":
        while True:
            print(" ")
            print(get_text("qual_arte_editar"))
            print(" ")
            
            # Mostrar as artes disponíveis dinamicamente
            for i, nome_arte in enumerate(artes.keys(), 1):
                print(f"{i} - {nome_arte}")
            print(" ")
            print(get_text("vol"))
            print(" ")
            opcao_edt = input(get_text("digite_opcao") + " ")
            print(" ")
            
            if opcao_edt == "vol":
                print(get_text("voltando_menu") + "\n")
                break
            elif opcao_edt in artes:
                nome_selecionado = opcao_edt
            else:
                # Tenta como número
                try:
                    idx = int(opcao_edt) - 1
                    nome_selecionado = list(artes.keys())[idx]
                except:
                    print(get_text("opcao_invalida") + "\n")
                    continue
            
            # Submenu para a arte selecionada
            while True:
                print(f"\n{get_text('arte')} \"{nome_selecionado}\"")
                print(f"{get_text('conteudo')}:\n{artes[nome_selecionado]}")
                print("\n" + get_text("ver_arte"))
                print(get_text("editar_nome"))
                print(get_text("editar_conteudo"))
                print(get_text("deletar_arte"))
                print(get_text("voltar_lista"))
                print(" ")
                
                opcao_acao = input(get_text("digite_opcao") + " ")
                print(" ")
                
                if opcao_acao == "1":
                    print(f"{get_text('arte_texto')} \"{nome_selecionado}\":")
                    print(artes[nome_selecionado])
                    print(" ")
                
                elif opcao_acao == "2":
                    novo_nome = input(get_text("novo_nome") + " ")
                    if novo_nome in artes and novo_nome != nome_selecionado:
                        print(get_text("nome_existe") + "\n")
                    else:
                        artes[novo_nome] = artes.pop(nome_selecionado)
                        salvar_artes(artes)
                        print(f"{get_text('nome_alterado')} \"{novo_nome}\" {get_text('sucesso')}\n")
                        nome_selecionado = novo_nome
                
                elif opcao_acao == "3":
                    idioma = configs.get("idioma", "pt")
                    fim_word = "FIM" if idioma == "pt" else "END"
                    print(get_text("digite_linhas"))
                    linhas = []
                    while True:
                        linha = input()
                        if linha.upper() == fim_word:
                            break
                        linhas.append(linha)
                    
                    novo_conteudo = "\n".join(linhas)
                    artes[nome_selecionado] = novo_conteudo
                    salvar_artes(artes)
                    print(get_text("conteudo_alterado") + "\n")
                
                elif opcao_acao == "4":
                    if configs["confirmar_antes_deletar"]:
                        confirmacao = input(f"{get_text('tem_certeza_deletar')} \"{nome_selecionado}\"? (s/n): ")
                        if confirmacao.lower() == "s":
                            del artes[nome_selecionado]
                            salvar_artes(artes)
                            print(get_text("deletado_sucesso") + "\n")
                            break
                        else:
                            print(get_text("delecao_cancelada") + "\n")
                    else:
                        del artes[nome_selecionado]
                        salvar_artes(artes)
                        print(get_text("deletado_sucesso") + "\n")
                        break
                
                elif opcao_acao == "5":
                    break
                else:
                    print(get_text("opcao_invalida") + "\n")
    
    # ======================== CRIAR NOVA ARTE ========================
    elif opcao == "new":
        nome_arte = input(get_text("criar_arte") + " ")
        idioma = configs.get("idioma", "pt")
        fim_word = "FIM" if idioma == "pt" else "END"
        print(get_text("digite_linhas"))
        linhas = []
        while True:
            linha = input()
            if linha.upper() == fim_word:
                break
            linhas.append(linha)
        
        arte = "\n".join(linhas)
        artes[nome_arte] = arte
        salvar_artes(artes)
        print(get_text("arte_criada") + "\n")
    
    # ======================== CONFIGURAÇÕES ========================
    elif opcao == "cfg":
        while True:
            print(" ")
            print(get_text("selecione_config"))
            print(" ")
            print(f"{get_text('confirmar_deletar')} {get_text('sim') if configs['confirmar_antes_deletar'] else get_text('nao')}")
            idioma_display = "Português" if configs.get("idioma", "pt") == "pt" else "English"
            print(f"{get_text('mudar_idioma')} {idioma_display}")
            print(" ")            
            print(get_text("vol"))
            print(" ")
            
            opcao_cfg = input(get_text("digite_opcao") + " ")
            print(" ")
            
            if opcao_cfg == "1":
                configs["confirmar_antes_deletar"] = not configs["confirmar_antes_deletar"]
                salvar_configs(configs)
                novo_estado = get_text("sim") if configs["confirmar_antes_deletar"] else get_text("nao")
                print(f"{get_text('alterado_para')} {novo_estado}\n")
            
            elif opcao_cfg == "2":
                idioma_atual = configs.get("idioma", "pt")
                novo_idioma = "en" if idioma_atual == "pt" else "pt"
                configs["idioma"] = novo_idioma
                salvar_configs(configs)
                novo_idioma_display = "English" if novo_idioma == "en" else "Português"
                print(f"{get_text('alterado_para')} {novo_idioma_display}\n")
            
            elif opcao_cfg == "vol":
                print(get_text("voltando_menu") + "\n")
                break
            
            else:
                print(get_text("opcao_invalida") + "\n")
                
    # ======================== SAIR ========================
    elif opcao == "exit":
        print(get_text("saindo") + "...")
        break

    else:
        print(get_text("opcao_invalida") + "\n")
