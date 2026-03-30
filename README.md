# PROG TEST AUTOMATIZADO

Uma Ferramenta simples para executar testes automatizados em programa C (ou qualquer outro executavel) utilizando arquivos de entrada e saída esperada.
O objetivo desse projeto é executar uma comparação e validação de programas de forma automatica, conferindo os resultados obtidos com os resultados corretos.

Esse projeto foi desenvolvido como uma primeira versão funcional do sistema de teste

---
## Ideia do Projeto

O script executa um programa várias vezes, utilizando diferentes arquivos de entrada, e compara a saída gerada com a saída esperada.

Fluxo de funcionamento:

1. O usuário informa qual programa deseja testar.
2. O sistema lê os arquivos da pasta entradas.
3. Executa o programa com cada entrada.
4. Compara com os arquivos da pasta esperados.
5. Mostra quais testes passaram ou falharam.
6. Gera um relatório final.

---
## Estrutura do Projeto
```
prog-test-automatizado
│
├── prog_test_automa.py
├── exemplos
│   └── sistema_notas.c
│
├── entradas
│   ├── input1.txt
│   └── input2.txt
│
└── esperados
    ├── output1.txt
    └── output2.txt
```
---
## Requisitos 
  - Python 3  
  - GCC (para compilar o programa em C)

## Compilação e Execução
Primeiro compilar o programa que quer fazer os testes.
Exemplo:
```
gcc sistema_notas.c -o programa
```

Depois rodar o script:
```
python prog_test_automa.py programa.exe
```

E o teste será aplicado para o programa compilado, retornando uma saida como:

```
Teste 1: PASSOU  
Teste 2: PASSOU

Relatório: 2/2 testes passaram
```
