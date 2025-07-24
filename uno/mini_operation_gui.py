import sys
from collections import defaultdict
from __init__ import *
from stdqt import *

WINDOW_TITLE = '快速行动'
SKIPPED_TIP = '这个回合你无法出牌, 为你摸到一张{}' # {0}: str(card)

class InHandCards:
    def __init__(self):
        self.cards:list[BaseCard] = []
        self.cnt = 0
        self.uuid_card_dict:defaultdict[str, BaseCard|None] = defaultdict(None)
    def add(self, card:BaseCard) -> bool:
        if card in self.cards:
            return False
        self.cards += [card]
        self.cnt += 1
        self.uuid_card_dict[card.uuid] = card
        return True
    def remove(self, card:BaseCard) -> bool:
        if card not in self.cards:
            return False
        self.cards.remove(card)
        self.cnt -= 1
        del self.uuid_card_dict[card.uuid]
        return True
    def find_card(self, _uuid:str) -> BaseCard|None:
        return self.uuid_card_dict[_uuid]
    def force_refresh_cnt(self) -> int:
        self.cnt = len(self.cards)
        return self.cnt
    def select_valid_cards(self, last:BaseCard) -> list[BaseCard]:
        ans = set()
        for c in self.cards:
            if is_valid_action(last, c):
                ans.add(c)
        ans = list(ans)
        return ans
    def merge(self, *cards:list[BaseCard]|tuple[BaseCard]):
        if len(cards) == 1:
            cards = cards[0]
            if isinstance(cards, list):
                for c in cards:
                    self.add(c)
            elif isinstance(cards, BaseCard):
                self.add(c)
        else:
            for c in cards:
                self.add(c)

class CardGui(QWidget):
    def __init__(self, parent:'MiniOperationWindow', card:BaseCard) -> None:
        super().__init__(parent)
        self.card = card
        self.setFixedSize(100, 200)
        self.o_card = QLabel(self)
        self.o_card.setFixedSize(self.size())
        self.o_card.setText(str(self.card))

class CardZoneGui(QWidget):
    def __init__(self, parent:'MiniOperationWindow', cards:list[BaseCard]) -> None:
        super().__init__(parent)
        self.cards = cards
        self.card_gui_lst:list[CardGui] = [CardGui(self, c) for c in cards]
        self.lay_card_gui()
    def lay_card_gui(self) -> None:
        for i, cg in enumerate(self.card_gui_lst):
            y = (i - 1) * 18
            cg.setGeometry(self.x(), y, self.width(), self.height())

class MiniOperationWindow(QWidget):
    def __init__(self, last:BaseCard, hand:InHandCards):
        super().__init__()
        self.last = last
        self.hand = hand
        self.setWindowTitle(WINDOW_TITLE)
        self.setFixedSize(400, 400)
        if valids := self.select_valid_cards():
            self.o_card_zone = CardZoneGui(self, valids)
        else:
            self.o_skipped_tip = QLabel(self)
            self.o_skipped_tip.setText(SKIPPED_TIP.format(''))
            self.o_skipped_tip.setFixedSize(self.size())
    def select_valid_cards(self) -> list[BaseCard]:
        ans = set()
        for c in self.hand.cards:
            if is_valid_action(self.last, c):
                ans.add(c)
        ans = list(ans)
        return ans
    def showEvent(self, a0):
        return super().showEvent(a0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    last = Num(0, 2)
    hand = InHandCards()
    hand.merge(random.choices(gen_shuffled(), k=25))
    window = MiniOperationWindow(last, hand)
    window.show()
    app.exec()