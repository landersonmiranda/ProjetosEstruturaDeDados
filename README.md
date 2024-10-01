Projetos de Estruturas de Dados
Este repositório contém dois projetos que implementam diferentes estruturas de dados para armazenar e manipular palavras de forma eficiente. Ambos os projetos leem comandos da entrada padrão e produzem resultados na saída padrão.

Projeto 1: Armazenamento em Listas Simplesmente Encadeadas
Neste projeto, um programa é implementado para armazenar palavras em listas simplesmente encadeadas, permitindo consultas sobre essas palavras. O programa organiza as palavras em três listas baseadas em seu tamanho:

Lista 1: Armazena palavras com até 5 letras.
Lista 2: Armazena palavras de 6 a 10 letras.
Lista 3: Armazena palavras com mais de 10 letras.
Além disso, uma quarta lista conecta todos os nós das palavras em ordem alfabética crescente. Cada nó contém dois campos de apontadores: um que referencia o próximo elemento de sua lista básica e outro que referencia o próximo nó na lista de palavras ordenadas.

Estrutura do Projeto
Entrada: Conjunto de comandos para executar.
Saída: Resultados das operações realizadas.
Funcionamento
As palavras são lidas e armazenadas nas respectivas listas base.
As listas são mantidas em ordem alfabética.
A lista adicional conecta todos os nós de maneira ordenada.
Projeto 2: Armazenamento em Árvore Binária de Busca
Neste projeto, um programa é implementado para armazenar palavras em uma árvore binária de busca, permitindo operações sobre essa árvore. As palavras são organizadas de acordo com sua ordem alfabética, e os nós da árvore são conectados em duas listas:

Lista 1: Une palavras com até 5 letras.
Lista 2: Une palavras com 6 ou mais letras.
Assim como no primeiro projeto, as listas não são implementadas separadamente dos nós da árvore.

Estrutura do Projeto
Entrada: Conjunto de comandos para executar.
Saída: Resultados das operações realizadas.
Funcionamento
As palavras são inseridas na árvore, seguindo a ordem alfabética.
Cada nó da árvore armazena uma palavra como chave e possui apontadores para seus filhos e para o próximo elemento da lista à qual a palavra pertence.
As listas são mantidas em ordem alfabética.
