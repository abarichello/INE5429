import Utils;

class XorShift {
    var state = {a: 0, b: 0, c: 0, d: 0, e: 0};
    var counter = 0;

    public function new() {
    }

    public function seed(a, b, c, d, e: Int) {
        state.a = a;
        state.b = b;
        state.c = c;
        state.d = d;
        state.e = e;
    }

    public function gen() {
        var t = state.e;
        var s = state.a;
        state.e = state.d;
        state.d = state.c;
        state.c = state.b;
        state.b = s;
        t = Utils.pow(t, t >> 2);
        t = Utils.pow(t, t << 1);
        t = Utils.pow(t, Utils.pow(s, (s << 4)));
        state.a = t;
        counter += 362437;
        return t + counter;
    }

    public static function main() {
        var xs = new XorShift();
        xs.seed(1, 2, 3, 4, 5);

        for (i in 0...5) {
            trace(xs.gen());
        }
    }
}
