# Controle Digital de Peças

Este protótipo em simula o trabalho diário de um inspetor na linha de montagem. O programa abre um menu simples, onde dá para cadastrar cada peça com ID, peso, cor e comprimento. A lógica confere se a peça passa nos critérios de qualidade (peso entre 95 g e 105 g, cor azul ou verde, comprimento entre 10 cm e 20 cm). Peças aprovadas entram na fila de armazenamento. 

Assim que uma caixa acumula 10 itens, ela é considerada fechada e o sistema inicia outra. Todo o histórico fica acessível pelo menu, incluindo motivos das reprovações e um relatório final com totais e caixas utilizadas.

## Como rodar

1. Instale o Python 3 se ainda não estiver disponível na máquina (https://www.python.org/downloads/).  
2. Abra um terminal ou prompt de comando.  
3. Vá até a pasta do projeto (`cd caminho/Desafio de Automação Digital Gestão de Peças, Qualidade e Armazenamento`).  
4. Execute o script:  
   ```bash
   python gestao_de_pecas.py
   ```  
5. Use as opções do menu digitando o número correspondente:
   - `1` cadastra uma nova peça
   - `2` mostra listas de aprovadas e reprovadas
   - `3` remove um cadastro
   - `4` exibe as caixas fechadas
   - `5` imprime o relatório consolidado
   - `0` encerra o programa

## Exemplos de entradas e saídas

### Exemplo 1 – Cadastro aprovado
Entrada:
```
Id da peça: 001
Peso (g): 100
Cor: azul
Comprimento (cm): 15
```
Saída imediata:
```
Peça aprovada e enviada para armazenamento.
```

### Exemplo 2 – Cadastro reprovado
Entrada:
```
Id da peça: 002
Peso (g): 108
Cor: vermelha
Comprimento (cm): 22
```
Saída:
```
Peça reprovada.
Motivos: peso fora do padrao, cor fora do padrao, comprimento fora do padrao
```

### Exemplo 3 – Relatório final
Após cadastrar várias peças e escolher a opção `5`, o programa mostra algo parecido com:
```
=== Relatorio final ===
Total de peças aprovadas: 10
Total de peças reprovadas: 2

Motivos das reprovações:
- P002: peso fora do padrao, cor fora do padrao, comprimento fora do padrao
- P005: cor fora do padrao

Quantidade de caixas utilizadas: 1
Caixa atual: P011, P012
```# Desafio-de-Automa-o-Digital-Gest-o-de-Pe-as-Qualidade-e-Armazenamento
