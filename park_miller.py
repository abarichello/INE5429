# park-miller.py

from time import time


def park_miller(seed, size):
    while True:
        result = 0
        mod = 0
        if size % 32:
            mod = 1

        for i in range(int(size / 32) + mod):
            seed = (16807 * seed) % 0x7FFFFFFF  # 32 bits
            result = (result << 32) + seed

        result = result >> int(mod * (32 - (size % 32)))
        yield result


if __name__ == "__main__":
    # tamanhos listados no enunciado
    sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    seed = 1
    for size in sizes:
        # contabilizando os milissegundos de execucao
        start_time = time()
        generator = park_miller(seed, size)
        res = next(generator)
        end_time = time()

        # tabelas de resultado
        total_time = (end_time - start_time) * 1000  # ms
        time_str = "{0:.5f}".format(total_time)
        print(f"Size: {size}|Time:{time_str}|Number:{res}")
