# Texter 🎨

Um editor interativo de arte ASCII (text art) construído em Python.

## Sobre o Projeto

Texter é uma aplicação terminal que permite criar, editar, visualizar e gerenciar artes de texto (ASCII art). As artes são salvas em um arquivo JSON, permitindo que você tenha uma biblioteca persistente de suas criações.

## Recursos

- ✨ **Visualizador**: Veja suas artes criadas anteriormente
- 📝 **Editor**: Edite o nome e conteúdo de artes existentes
- ➕ **Criar**: Crie novas artes de texto facilmente
- ⚙️ **Configurações**: Personalize o comportamento da aplicação
- 💾 **Persistência**: Todas as artes são salvas automaticamente em JSON

## Como Usar

1. Execute o programa:
```bash
python Texter.py
```

2. No menu principal, escolha uma das opções:
   - `ver` - Visualizar artes existentes
   - `edt` - Editar ou deletar artes
   - `new` - Criar uma nova arte
   - `cfg` - Acessar configurações
   - `exit` - Sair do programa

## Estrutura de Arquivos

- `Texter.py` - Arquivo principal da aplicação
- `artes.json` - Banco de dados das artes criadas
- `configs.json` - Configurações da aplicação

## Requisitos

- Python 3.7+

## Configurações

Atualmente, a aplicação possui uma configuração:

- **Confirmar antes de deletar**: Quando ativada, pede confirmação antes de deletar uma arte

## Exemplos

### Criar uma nova arte:
```
Digite o nome da arte de texto: Gato
Digite as linhas da arte (digite 'FIM' quando terminar):
    /\_/\
   ( o.o )
    > ^ <
   /|   |\
  (_|   |_)
FIM
```

## Notas

- As artes são salvas em formato JSON com encoding UTF-8
- Você pode usar qualquer caractere Unicode nas suas artes
- O programa cria automaticamente os arquivos JSON na primeira execução

## Autor

Seu Nome

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
