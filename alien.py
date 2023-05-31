class Alien:
    def __init__(self, name:str, volume, fill):
        self.name = name
        self.volume = volume
        self.fill = fill

    def __repr__(self):
        return f"Alien('{self.name}', {self.volume}, {self.fill})"

    def __le__(self, other):
        if self.volume * self.fill == other.volume * other.fill:
            if len(self.name) == len(other.name):
                return self.name <= other.name
            return len(self.name) <= len(other.name)
        return self.volume * self.fill <= other.volume * other.fill

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.volume * self.fill == other.volume * other.fill:
            if len(self.name) == len(other.name):
                if self.name < other.name:
                    return self.name < other.name
                return self.name > other.name
            return len(self.name) < len(other.name)
        return self.volume * self.fill < other.volume * other.fill

    def __gt__(self, other):
        if self.volume * self.fill == other.volume * other.fill:
            if len(self.name) == len(other.name):
                return self.name > other.name
            return len(self.name) > len(other.name)
        return self.volume * self.fill > other.volume * other.fill


    def __add__(self, other):
        name = '-'.join(sorted([self.name, other.name]))
        volume = (self.volume + other.volume) // 2
        fill = min(self.fill, other.fill)
        return Alien(name, volume, fill)

    def __isub__(self, number):
        self.volume = max(self.volume - number, 0)
        return self

    def __mul__(self, number):
        result = []
        for i in range(number):
            name = f"{self.name}-{i+1}"
            volume = self.volume // number
            fill = self.fill // number
            result.append(Alien(name, volume, fill))
        return result

    def __call__(self, number):
        return (self.volume - self.fill) * len(self.name) // number

    def __eq__(self, other):
        return self.name == other.name and self.volume == other.volume and self.fill == other.fill

    def __ge__(self, other):
        if self.volume * self.fill == other.volume * other.fill:
            if len(self.name) == len(other.name):
                return self.name >= other.name
            return len(self.name) >= len(other.name)
        return self.volume * self.fill >= other.volume * other.fill

    def __str__(self):
        return f"Wheel Alien {self.name} with {self.volume} volume and filled up {self.fill}."

    def fill_up(self, number: int):
        if number >= 0:
            return self.fill + number
        else:
            if self.fill - number >= 0:
                return self.fill - number
            else:
                return self.fill == 0


al = Alien("Man", 200, 148)
al1 = Alien("Spider", 800, 201)
print(al < al1, al != al1, al > al1)
print(al, al1, sep="\n")
print()
al.fill_up(-203)
res = al1 * 3
print(al, al1, res,sep="\n")
print(res[0](7))
