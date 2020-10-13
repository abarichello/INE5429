# xorshift.py

from time import time

# Xorshift variação xorwow como definido na
# pg 5 de Marsaglia, Xorshift RNGs
def xorwow(size):
    # seed e variavel de contagem
    a = 76901256
    b = 23596367
    c = 39245745
    d = 42425298
    counter = 2575458

    result = 0
    mod = 1
    if size % 32:
        mod = 1

    for i in range(int(size / 32) + mod):
        # logica de mudança dos estados para gerar o numero aleatorio
        t = d
        s = a
        d = c
        c = b

        t ^= t >> 2
        t ^= t << 1
        t ^= s ^ (s << 4)
        t %= 0x7FFFFFFF  # 32 bits
        a = t

        counter += 362437 % 0x7777777
        partial = (t + counter) % 0x7777777
        result = (result << 32) + partial
    # truncagem do resultado final
    return result >> int(mod * (32 - (size % 32)))


if __name__ == "__main__":
    # tamanhos listados no enunciado
    sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    for size in sizes:
        # contabilizando os milissegundos de execucao
        start_time = time()
        res = xorwow(size)
        end_time = time()

        # tabelas de resultado
        total_time = (end_time - start_time) * 1000  # ms
        time_str = "{0:.5f}".format(total_time)
        print(f"Size: {size}|Time:{time_str}|Number:{res}")
