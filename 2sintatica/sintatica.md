# Análise Sintática

O Analisador sintático também conhecido como parser tem como tarefa principal determinar se o programa de entrada representado pelo fluxo de tokens possui as sentenças válidas para a linguagem de programação.

A analise sintática e a segunda etapa do processo de compilação e na maioria dos casos utiliza gramáticas livres de contexto para especificar a sintaxe de uma linguagem de programação.

## Visão geral

A sintaxe é a parte da gramática que estuda a disposição das palavras na frase e das frases em um discurso. Essa etapa no processo de compilação deve reconhecer as forma do programa fonte e determinar se ele é valido ou não.

Esse modelo pode ser definido utilizando gramáticas livres de contexto que representam uma gramática formal e pode ser escrita através de algoritmos fazem a derivação de todas as possíveis construções da linguagem.

As derivações tem como objetivo determinar se um fluxo de palavras se encaixa na sintaxe da linguagem de programação.

Alguns termos utilizados na definição de linguagens de programação.

**Símbolo**: são os elementos mínimos que compõe uma linguagem. Na linguagem humana são as letras.

**Sentença**: É um conjunto ordenado de símbolos que forma uma cadeia ou string. Na linguagem humana são as palavras.

**Alfabeto**: É um conjunto de símbolos. Na linguagem humana é o conjunto de letras {a, b, c, d, ...}

**Linguagem**: É o conjunto de sentenças, Na linguagem humana são os conjuntos de palavras {compiladores, linguagem, ...}

**Gramática**: É uma forma de representar as regras para formação de uma linguagem.

Trazendo esse conceito para linguagem de programação temos:

**Alfabeto**: {w, h, i, l, e, +, 1, 2, 3}

**Símbolos**: 1, 5, +, w

**Sentença**: while, 123, +1

**Linguagem**: {while, 123, +1}

Dada uma gramática G e uma sentença s o objetivo do analisador sintático é verificar se a sentença s pertence a linguagem G. O analisador sintático recebe do analisador léxico a sequência de tokens que constitui a sentença s e produz uma arvore de derivação se a sentença é válida ou emite um erro se a sentença é inválida.

O analisador léxico é desenvolvido para reconhecer cadeias de caracteres fazendo uma leitura dos caracteres e obtendo a sequência de tokens, esse analisador vê o texto como uma sequência de palavras de uma linguagem regular e reconhece ele através de autômatos finitos determinísticos e não determinísticos.

Já o analisador sintático vê o mesmo texto como uma sequência de sentenças que deve satisfazer as regras gramaticais. É através da gramática que podemos validar expressões criadas na linguagem de programação.

## Gramática Livre de Contexto - GLC

As linguagens de programação em geral pertencem a uma categoria chamada de Linguagens Livres de Contexto. Umas das formas de representar essas linguagens é através de Gramáticas Livres de Contexto que são a base para a construção de analisadores sintáticos. Elas são utilizadas para especificar as regras sintáticas de uma linguagem de programação, uma linguagem regular pode ser reconhecida por automatos finitos determinísticos e não determinísticos, já uma Gramatica Livre de Contexto pode ser reconhecida por um automato de pilha.

Outra aplicação de GLC são os DTD - Definição de Tipos de Documentos - utilizados por arquivos XML que descreve as tags de uma forma natural, as tags deve estar aninhadas afim de lidar com o significado do texto.

Veja o exemplo:


```XML
    <produto><codigo></codigo></produto>
```

Uma gramática descreve naturalmente como é possível fazer construções no programa. Veja o exemplo de um comando if-else em Pascal que deve ter a seguinte forma.


```PASCAL
    if (expressão) then declaração else declaração ;
```

Essa mesma forma em uma Gramática Livre de Contexto pode ser expressada da seguinte maneira:


```
    declaração → if ( expressão ) then declaração else declaração ;
```

A definição formal de uma gramática livre de contexto pode ser representada através dos seguintes componentes:



**G = (N, T, P, S)**


Onde:

- **N** – Conjunto finito de símbolos não terminais.
- **T** – Conjunto finito de símbolos terminais.
- **P** – Conjunto de regras de produções.
- **S** – Símbolo inicial da gramática.


### Terminologias:

**Símbolos terminais**: Conjunto finito de símbolos básicos que formam as palavras da linguagens, são representadas pelo tokens reconhecidos pelo analisador lexico.

**Símbolos não terminais**: Conjunto finito de variáveis utilizadas para representar os conjuntos da linguagem, são formadas pelos terminais e pelos próprios símbolos não terminais.

**Símbolo inicial**: É a variável, simbolo não terminal, que representa o inicio da definição da linguagem.

**Regras de produções**: Representa um conjunto de regras sintáticas que representam a definição da linguagem, indicam como símbolos terminais e não terminais podem ser combinados.

As regras de produção são representadas da seguinte forma:

    {A} → {α}

Onde:

- A é uma variável - simbolo não terminal.
- -> simbolo de produção .
- α é a combinação símbolos terminais e não terminais que representam a forma como uma string vai ser formada.

Veja o exemplo de uma Gramatica Livre de Contexto.

````
G = ({S}, {a, b}, P, S)

P = {   
        S → aSb
        S → λ  
    }
````
Essa gramatica é formada pelas terminais a e b, que são os tokens da linguagem, como regras de produção nos temos aSb que obriga ter um a e b nas extremidades da palavras, o simbolo λ que significa vazio.