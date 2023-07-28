from classpt import Pokemon

# 상속받는다

class Pikachu(Pokemon):
    no =25
    type = '전기'


    def __init__(self, name, lv=5):
        super().__init__()

        self.name = name
        self.lv = lv

        super().increase_species('피카츄')

        self.number = Pokemon.number_of_pokemon



p1=Pikachu('지우개')

print(p1.name)
print(Pokemon.number_of_pokemon)
print(Pokemon.discovered_species)

