# Estruturas de Dados em Python

Este repositório contém implementações básicas de estruturas de dados fundamentais utilizando Python puro. Cada estrutura foi colocada em uma pasta separada para facilitar a organização, compreensão e reutilização do código. O objetivo principal é servir como material de apoio ao aprendizado.

## Estruturas Implementadas
https://github.com/esdras-dev/estrutura_de_dados/settings
### 1. Fila 
Estrutura do tipo FIFO (*First In, First Out*), onde o primeiro a entrar é o primeiro a sair. Utiliza `collections.deque` para melhor performance.

**Principais métodos:**
- `enfileirar(item)`
- `desenfileirar()`
- `frente()`
- `esta_vazia()`
- `tamanho()`

---

### 2. Lista Encadeada
Lista composta por nós que apontam para o próximo elemento. Ideal para inserções/remoções rápidas no início.

**Principais métodos:**
- `inserir_inicio(valor)`
- `exibir()`

---

### 3. Lista Ordenada 
Versão da lista encadeada onde os elementos são inseridos já em ordem crescente.

**Principais métodos:**
- `inserir(valor)`
- `exibir()`

---

### 4. Pilha (stack)
Estrutura do tipo LIFO (*Last In, First Out*), onde o último a entrar é o primeiro a sair.

**Principais métodos:**
- `empilhar(item)`
- `desempilhar()`
- `topo()`
- `esta_vazia()`
- `tamanho()`

---

### 5. Árvore Binária de Busca )
Organiza elementos de forma hierárquica. Elementos à esquerda são menores e à direita, maiores que o nó atual.

**Principais métodos:**
- `inserir(valor)`
- `em_ordem()` – imprime os valores ordenadamente

---  

## Referências

As implementações deste repositório foram baseadas em livros e cursos disponíveis online:

- Curso em Vídeo – Gustavo Guanabara:  
  [Estrutura de Dados em Python – YouTube](https://www.youtube.com/playlist?list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye)
  
- Documentação oficial do Python: python.org
  
- Livro - automatize tarefas maçantes com python programação prática para verdadeiros iniciantes

 - [Python Standard Library](https://docs.python.org/3/library/)


