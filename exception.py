import time


while True:
    try:
        value = int(input("Digite um numero natural: "))
        print("O reciproco do", value,"é", 1 / value)
    except ValueError:
        print("Numero invalido!!!")
    except ZeroDivisionError:
        print("Zero não é um divisor!!!")
    except KeyboardInterrupt:
        break
    except:
        print("Algo de errado não está certo!!!")



    time.sleep(2)