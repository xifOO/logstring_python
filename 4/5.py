class CardDeck:
    def __init__(self):
        self.suits = ['Пик', 'Треф', 'Бубен', 'Черв']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 52:
            raise StopIteration
        else:
            suit = self.suits[self.index // 13]
            value = self.values[self.index % 13]
            card = f"{value} {suit}"
            self.index += 1
            return card
        
          