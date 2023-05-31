class AutomaticTranslator:
    def __init__(self, num_languages, vocabulary, form):
        self.num_languages = num_languages
        self.vocabulary = vocabulary
        self.form = form

    def __lt__(self, other):
        if self.vocabulary == other.vocabulary:
            if self.num_languages == other.num_languages:
                return self.form < other.form
            return self.num_languages < other.num_languages
        return self.vocabulary < other.vocabulary

    def __le__(self, other):
        if self.vocabulary == other.vocabulary:
            if self.num_languages == other.num_languages:
                return self.form <= other.form
            return self.num_languages <= other.num_languages
        return self.vocabulary <= other.vocabulary

    def __eq__(self, other):
        return self.num_languages == other.num_languages and self.vocabulary == other.vocabulary and self.form == other.form

    def __sub__(self, other):
        num_languages = min(self.num_languages, other.num_languages)
        vocabulary = (self.vocabulary + other.vocabulary) // 2
        form = min(self.form, other.form)
        return AutomaticTranslator(num_languages, vocabulary, form)

    def __iadd__(self, other):
        self.num_languages += other[0]
        self.vocabulary += other[1]
        return self

    def __truediv__(self, other):
        return [AutomaticTranslator(self.num_languages // other, self.vocabulary // other, self.form) for i in range(other)]

    def __ge__(self, other):
        if self.vocabulary == other.vocabulary:
            if self.num_languages == other.num_languages:
                return self.form >= other.form
            return self.num_languages >= other.num_languages
        return self.vocabulary >= other.vocabulary

    def __gt__(self, other):
        if self.vocabulary == other.vocabulary:
            if self.num_languages == other.num_languages:
                return self.form > other.form
            return self.num_languages > other.num_languages
        return self.vocabulary > other.vocabulary

    def __str__(self):
        return f"Translator in the form of {self.form} from {self.num_languages} languages, {self.vocabulary} words."

    def __repr__(self):
        return f"AutomaticTranslator({self.num_languages}, {self.vocabulary}, '{self.form}')"

    def __call__(self):
        return (self.vocabulary + len(self.form)) // self.num_languages

    def add_language(self, nums):
        self.num_languages+=1
        self.vocabulary+=nums


#at = AutomaticTranslator(5, 1200, "glasses")
#at1 = AutomaticTranslator(5, 1200, "ears")
#print(at < at1, at != at1, at >= at1)
#print(at, at1, sep="\n")
#print()
#at += (2, 578)
#at1.add_language(850)
#at2 = at - at1
#print(at, at1, at2, sep="\n")
at = AutomaticTranslator(12, 5432, "box")
at1 = AutomaticTranslator(3, 15, "hat")
print(at <= at1, at == at1, at > at1)
print(at, at1, sep="\n")
print()
res = at / 4
res[0] += (2, 187)
print(res, at(), at1(), sep="\n")



