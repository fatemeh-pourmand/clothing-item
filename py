class User:
    def __init__(self, name, gender, favorite_style, hair_color, eye_color, skin_tone):
        self.name= name
        self.gender= gender
        self.favorite_style= favorite_style
        self.hair_color= hair_color
        self.eye_color= eye_color
        self.skin_tone= skin_tone
    def show_info(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

class Closet:
    def __init__(self, User):
        self.User= User
        self.stats= {
            'shirts':20,
            'dress pants':25,
            'skirt':80,
            'shoes':['sneakers':100,'loafers':50,'sandals':40,'high heels':150,'flip flop':33,'boots':70]
            'colors':['red', 'blue', 'black','white']
            'hat':30,
            'jumper':40,
            'vest':15,
            'dress':300,
            'socks':60,
            'scarf':40,
            'swimsuit':50,
            'umbrella':30,
            'shorts':100,
            'bag':250,
            'hoodie':200,
            'bikini':400,
            'straw hat':55,
            ......
            
            
        }
