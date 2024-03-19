class Simplecalc:
    @classmethod
    def get_triangle_area(cls, base, height):
        return base * height / 2


print(Simplecalc.get_triangle_area(1000, 500))
