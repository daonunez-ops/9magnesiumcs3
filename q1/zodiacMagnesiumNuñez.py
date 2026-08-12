YEAR = int(input('Enter your birth year: '))

class Zodiac:

    def __init__(self, year):
        self.year = year
        self.REMAINDER = self.year % 12

    def zodiac_teller(self):
        if self.REMAINDER == 0:
            print('Monkey (猴 / Hóu)')
        elif self.REMAINDER == 1:
            print('Rooster (鸡 / Jī)')
        elif self.REMAINDER == 2:
            print('Dog (狗 / Gǒu)')
        elif self.REMAINDER == 3:
            print('Pig (猪 / Zhū)')
        elif self.REMAINDER == 4:
            print('Rat (鼠 / Shǔ)')
        elif self.REMAINDER == 5:
            print('Ox (牛 / Niú)')
        elif self.REMAINDER == 6:
            print('Tiger(虎 / Hǔ)')
        elif self.REMAINDER == 7:
            print('Rabbit (兔 / Tù)')
        elif self.REMAINDER == 8:
            print('Dragon (龙 / Lóng)')
        elif self.REMAINDER == 9:
            print('Snake (蛇 / Shé)')
        elif self.REMAINDER == 10:
            print('Horse (马 / Mǎ)')
        elif self.REMAINDER == 11:
            print('Goat (羊 / Yáng)')

    def main(self):
        if self.year < 1900:
            print('Invalid year, it should not be earlier than 1900.')
        else:
            self.zodiac_teller()

z = Zodiac(YEAR)
z.main()