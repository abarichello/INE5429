// Linear congruential generator usando a fórmula de BSD
class LCG {
    var seed = 0;

    // Inicializa a classe com a seed (r0)
    public function new(seed = 0) {
        this.seed = seed;
    }

    // Esta função define a fórmula recuresiva do LCG:
    // rn+1 = a x rn + c (mod m)
    public function lcg(a, c, m) {
        var r = this.seed;
        return function () {
            r = (a*r + c) % m;
            return r;
        }
    }

    public static function main() {
        // Utilizando estes valores de a, c e m conseguimos o mesmo
        // resultado desta demonstração do algoritmo:
        // en.wikipedia.org/wiki/File:Linear_congruential_generator_visualisation.svg
        var a = 4;
        var c = 1;
        var m = 9;

        trace('Seed 0');
        var seed = 0;
        var bsd = new LCG(seed).lcg(a, c, m);

        for (i in 0...5) {
            trace(bsd());
        }

        trace('Seed 1');
        seed = 1;
        var bsd = new LCG(seed).lcg(a, c, m);
        for (i in 0...5) {
            trace(bsd());
        }
    }
}