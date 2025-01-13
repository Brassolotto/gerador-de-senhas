import random

caracteres_mai = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "W", "U", "V", "X", "Y", "Z"]
caracteres_min = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "w", "u", "v", "x", "y", "z"]
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
especiais = ["!", "@", "#", "$", "%", "&", "*"]

def gerar_senha_basica(tamanho):
    return ''.join(random.choice(caracteres_min) for i in range(tamanho))

def gerar_senha_media(tamanho):
    caracteres = caracteres_min + [str(num) for num in numeros]
    return ''.join(random.choice(caracteres) for i in range(tamanho))

def gerar_senha_forte(tamanho):
    todos_caracteres = caracteres_mai + caracteres_min + [str(num) for num in numeros] + especiais
    return ''.join(random.choice(todos_caracteres) for i in range(tamanho))

def main():
    while True:
        print("\nGerador de senhas!")
        print("Digite 'sair' para encerrar")

        entrada1 = input("Digite o tamanho da senha: ")
        if entrada1.lower() == 'sair':
            break
        
        try:
            tamanho_senha = int(entrada1)
            if tamanho_senha < 4:
                print("Erro: A senha deve ter pelo menos 4 caracteres!")
                continue

            tipo_senha = int(input("Escolha o tipo de senha:\n[1] Básica\n[2] Média\n[3] Forte\nSua escolha: "))

            if tipo_senha == 1:
                senha = gerar_senha_basica(tamanho_senha)
                print(f"Sua senha básica é: {senha}")
            elif tipo_senha == 2:
                senha = gerar_senha_media(tamanho_senha)
                print(f"Sua senha média é: {senha}")
            elif tipo_senha == 3:
                senha = gerar_senha_forte(tamanho_senha)
                print(f"Sua senha forte é: {senha}")
            else:
                print("Opção inválida! Escolha 1, 2 ou 3.")


        except ValueError:
            print("Erro: Digite apenas números!")
        except Exception as e:
            print(f"Erro inesperado: {e}")



if __name__ == "__main__":
    main()