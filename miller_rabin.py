# miller-rabin.py

from time import time
from park_miller import park_miller


# teste para verificar se um numero e composto, ou seja
# pode ser descrito como a multiplicacao de dois inteiros
# positivos, o que o impede de ser primo
def composite_number(a, d, random_number, _range):
    if pow(a, d, random_number) == 1:
        return False

    for i in range(_range):
        if pow(a, 2 ** i * d, random_number) == random_number - 1:
            return False
    return True


def miller_rabin(random_number, size, rng_function):
    # n = (2^r)*d+1
    _range = 0
    d = random_number - 1
    while d % 2 == 0:
        d >>= 1
        _range += 1

    # assim como o teste de primalidade de fermat,
    # repetimos o teste 7 vezes, tal numero pode ser
    # modificado o que ira alterar na precisão do
    # resultado final
    for _ in range(8):
        a = next(rng_function)
        if composite_number(a, d, random_number, _range):
            # nao e primo
            return False
    # e primo se passar em todos os testes
    return True


if __name__ == "__main__":
    # tamanhos listados no enunciado
    sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    seed = 1
    for size in sizes:
        # utilizando novamente park miller para gerar os numeros aleatorios
        generator = park_miller(seed, size)
        random_number = next(generator)
        start_time = time()
        # loop infinito até encontrar um numero primo
        while not miller_rabin(random_number, size, generator):
            random_number = next(generator)
        end_time = time()

        # tabelas de resultado
        total_time = (end_time - start_time) * 1000  # ms
        time_str = "{0:.5f}".format(total_time)
        print(f"Size:{size}|Time:{time_str}")
