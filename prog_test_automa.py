import subprocess
import os

dir_entradas = "entradas"
dir_esperados = "esperados"

programa = input("Programa para testar: ")

arquivos_entradas = sorted(os.listdir(dir_entradas))
arquivos_esperados = sorted(os.listdir(dir_esperados))

passou = 0

for i in range(len(arquivos_entradas)):
    with open(os.path.join(dir_entradas, arquivos_entradas[i]), "r") as f:
        test_entradas = f.read()

    with open(os.path.join(dir_esperados, arquivos_esperados[i]), "r") as f:
        saida_esperada = f.read().strip()
    
    result = subprocess.run(
        programa,
        input = test_entradas,
        text = True,
        capture_output=True
    )

    saida = result.stdout.strip()

    if saida == saida_esperada:
        print(f"Teste {i+1}: PASSOU")
        passou += 1

    else:
        print(f"Teste {i+1}: FALHOU")
        print("\nSaida Esperada: \n", saida_esperada)
        print("\nSaida Obtida: \n", saida,"\n")
        

print(f"\n Relatório: {passou}/{len(arquivos_entradas)} testes passaram")