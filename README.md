# Projetos de Estruturas de Dados

Este repositório contém dois projetos que implementam diferentes estruturas de dados para armazenar e manipular palavras de forma eficiente. Ambos os projetos leem comandos da entrada padrão e produzem resultados na saída padrão.

## Projeto 1: Armazenamento em Listas Simplesmente Encadeadas

Neste projeto, um programa é implementado para armazenar palavras em listas simplesmente encadeadas, permitindo consultas sobre essas palavras. O programa organiza as palavras em três listas baseadas em seu tamanho:

- **Lista 1**: Armazena palavras com até 5 letras.
- **Lista 2**: Armazena palavras de 6 a 10 letras.
- **Lista 3**: Armazena palavras com mais de 10 letras.

Além disso, uma quarta lista conecta todos os nós das palavras em ordem alfabética crescente. Cada nó contém dois campos de apontadores: um que referencia o próximo elemento de sua lista básica e outro que referencia o próximo nó na lista de palavras ordenadas.

### Estrutura do Projeto

- **Entrada**: Conjunto de comandos para executar.
- **Saída**: Resultados das operações realizadas.

---

![image](https://github.com/user-attachments/assets/0a59aff8-a8cc-44bc-9467-d9cc0df98082)

---

## Projeto 2: Armazenamento em Árvore Binária de Busca

Neste projeto, um programa é implementado para armazenar palavras em uma árvore binária de busca, permitindo operações sobre essa árvore. As palavras são organizadas de acordo com sua ordem alfabética, e os nós da árvore são conectados em duas listas:

- **Lista 1**: Une palavras com até 5 letras.
- **Lista 2**: Une palavras com 6 ou mais letras.

Assim como no primeiro projeto, as listas não são implementadas separadamente dos nós da árvore.

### Estrutura do Projeto

- **Entrada**: Conjunto de comandos para executar.
- **Saída**: Resultados das operações realizadas.

### Funcionamento

1. As palavras são inseridas na árvore, seguindo a ordem alfabética.
2. Cada nó da árvore armazena uma palavra como chave e possui apontadores para seus filhos e para o próximo elemento da lista à qual a palavra pertence.
3. As listas são mantidas em ordem alfabética.

---

![image](https://github.com/user-attachments/assets/12fb79b9-7a4a-4a69-9c27-edaf9af9c81e)

---
## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, basta fazer um fork do repositório, realizar suas alterações e enviar um pull request.

