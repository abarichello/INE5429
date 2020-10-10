class Utils {
    public static function pow(a, b): Int {
        var a = cast(a, Float);
        var b = cast(b, Float);
        var res = Math.pow(a, b);
        return Std.int(res);
    }
}
