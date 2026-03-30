import subprocess
import os
import sys 
import time

tempo_inicio_teste = time.time()
dir_entradas = "entradas"
dir_esperados = "esperados"

arquivos_entradas = sorted(os.listdir(dir_entradas))
arquivos_esperados = sorted(os.listdir(dir_esperados))

passou = 0

for i in range(len(arquivos_entradas)):
    #Lendo os Arquivos de entrada, e os arquivos de saidas esperadas
    with open(os.path.join(dir_entradas, arquivos_entradas[i]), "r") as f:
        test_entradas = f.read()

    with open(os.path.join(dir_esperados, arquivos_esperados[i]), "r") as f:
        saida_esperada = f.read().strip()
    
    #Rodanto programa em subprocesso
    tempo_inicio = time.time()
    try:
        result = subprocess.run(
            sys.argv[1],
            input = test_entradas,
            text = True,
            capture_output=True,
            timeout=2
        )
    except subprocess.TimeoutExpired:
        print("Teste Falhou: Tempo de execução expirado")
        break

    tempo_fim = time.time()
    tempo_exec = tempo_fim - tempo_inicio

    #printanto os resultados dos testes
    saida = result.stdout.strip()
    print("Rodando:",arquivos_entradas[i])
    if saida == saida_esperada:
        print(f"Teste {i+1}: \033[32mPASSOU\033[0m ({tempo_exec:.3f}s)\n")
        passou += 1

    else:
        print(f"Teste {i+1}: \033[31mFALHOU\033[0m ({tempo_exec:.3f}s)")
        print("\nSaida Esperada: \n", saida_esperada)
        print("\nSaida Obtida: \n", saida,"\n")
        
#Relatório Final
tempo_fim_teste = time.time()
print("--------------------------------------")
print("Total de Testes: ", len(arquivos_entradas))
print("Passaram: ", passou)
print("Falharam", len(arquivos_entradas) - passou)
print(f"Tempo Execucao: {(tempo_fim_teste - tempo_inicio_teste):.3f}s")

#print(f"\n Relatório: {passou}/{len(arquivos_entradas)} testes passaram")