# fermat-test.py

from time import time
from park_miller import park_miller

# n e um numero aleatorio gerado usando park miller
# size e o tamanho a ser passado pra este algoritmo
# e rng_function e nossa função de números aleatorios
# a ser chamada através da função next, como e feito com
# 'generators' em Python que foi utilizado para a implementacao
def fermat_test(n, size, rng_function):
    # repetimos o teste 7 vezes, tal numero pode ser
    # modificado o que ira alterar na precisão do
    # resultado final
    for _ in range(7):
        # numero aleatorio usado no teste
        random_number = next(rng_function)
        a = (abs(random_number) + 1) % n - 1

        # teste de número composto
        if pow(a, n - 1, n) != 1:
            # retorna falso para numeros compostos
            return False
    # é primo se passa em todos os testes
    return True


if __name__ == "__main__":
    # tamanhos listados no enunciado
    sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    seed = 1
    for size in sizes:
        generator = park_miller(seed, size)
        random_number = next(generator)
        start_time = time()
        while not fermat_test(random_number, size, generator):
            random_number = next(generator)
        end_time = time()

        # tabelas de resultado
        total_time = (end_time - start_time) * 1000  # ms
        time_str = "{0:.5f}".format(total_time)
        print(f"Size: {size}|Time:{time_str}")
