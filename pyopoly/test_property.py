from property import Property,Utility,Railroad,PropertyGroup,LandException
from dice import Dice

# TODO: This should inherit from the real Player when it's done
class FakePlayer(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)

# TODO: This should inherit from the real Board when it's done
class FakeBoard(object):
    def __init__(self, dice, banker, *args):
        self.init = False
        self.dice = dice
        self.banker = banker
        self.players = args

        # Banker also needs the dice
        banker.dice = dice
    def player(self, num):
        return self.players[num - 1]

# TODO: This should inherit from the real Banker when it's done
class FakeBanker(object):
    pass

class FakeDice(Dice):
    def roll(self):
        pass

board = FakeBoard(FakeDice(), FakeBanker(), FakePlayer("1"), FakePlayer("2"))

def setup_purple():
    med = Property("Mediteranian Ave.", 60, [2, 10, 30, 90, 160, 250])
    baltic = Property("Baltic Ave.", 60, [4, 20, 60, 180, 320, 450])
    purple = PropertyGroup("Purple", med, baltic)
    return med, baltic, purple

def setup_lightblue():
    ori = Property("Oriental Ave.", 100, [30, 90, 270, 400, 550])
    verm = Property("Vermont Ave.", 100, [30, 90, 270, 400, 550])
    conn = Property("Connecticut Ave.", 120, [40, 100, 300, 450, 600])
    lightblue = PropertyGroup("Light Blue", ori, verm, conn)
    return ori, verm, conn, lightblue

def setup_railroad():
    rr = Railroad("Reading Railroad", 20)
    pr = Railroad("Pennsylvania Railroad", 20)
    bo = Railroad("B. & O. Railroad", 20)
    sl = Railroad("Short Line Railroad", 20)
    railroads = PropertyGroup("Railroads", rr, pr, bo, sl)

    return rr, pr, bo, sl, railroads

def setup_utilities():
    electric = Utility("Electric Company", 30)
    water = Utility("Water Works", 30)
    utilities = PropertyGroup("Utilities", electric, water)

    return electric, water, utilities

def setup_board():
    if not board.init:
        board.init = True
        board.med, board.baltic, board.purple = setup_purple()
        board.ori, board.verm, board.conn, board.lightblue = setup_lightblue()
        board.rr, board.pr, board.bo, board.sl, board.railroads = setup_railroad()
        board.electric, board.water, board.utilities = setup_utilities()
    return board

def test_property():
    board = setup_board()

    assert board.med in board.purple.properties
    assert board.baltic in board.purple.properties
    assert len(board.purple.properties) == 2

def test_railroads():
    board = setup_board()

    assert board.rr in board.railroads.properties
    assert board.pr in board.railroads.properties
    assert board.bo in board.railroads.properties
    assert board.sl in board.railroads.properties
    assert len(board.railroads.properties) == 4

def test_utilities():
    board = setup_board()

    assert board.water in board.utilities.properties
    assert board.electric in board.utilities.properties
    assert len(board.utilities.properties) == 2

def test_group_owner():
    board = setup_board()

    board.med.set_owner(board.player(1))
    board.baltic.set_owner(board.player(1))
    board.ori.set_owner(board.player(1))
    board.verm.set_owner(board.player(2))

    assert board.purple.all_owned(board.player(1))
    assert not board.purple.all_owned(board.player(2))

    assert not board.lightblue.all_owned(board.player(1))
    assert not board.lightblue.all_owned(board.player(2))

def test_property_rent():
    board = setup_board()

    board.med.set_owner(board.player(1))
    board.baltic.set_owner(board.player(1))
    board.ori.set_owner(board.player(1))
    board.verm.set_owner(board.player(2))

    # Player 1 owns both purple, so rent should be double
    assert board.med.charge_rent(board.banker, board.player(1)) == 0
    assert board.med.charge_rent(board.banker, board.player(2)) == 4
    assert board.baltic.charge_rent(board.banker, board.player(1)) == 0
    assert board.baltic.charge_rent(board.banker, board.player(2)) == 8
    assert board.ori.charge_rent(board.banker, board.player(1)) == 0
    assert board.ori.charge_rent(board.banker, board.player(2)) == 30
    assert board.verm.charge_rent(board.banker, board.player(1)) == 30
    assert board.verm.charge_rent(board.banker, board.player(2)) == 0

def test_property_houses():
    board = setup_board()

    board.med.set_owner(board.player(1))
    board.baltic.set_owner(board.player(1))

    board.med.buy_house(3)
    board.baltic.buy_house(4)

    assert board.med.charge_rent(board.banker, board.player(1)) == 0
    assert board.med.charge_rent(board.banker, board.player(2)) == 90
    assert board.baltic.charge_rent(board.banker, board.player(1)) == 0
    assert board.baltic.charge_rent(board.banker, board.player(2)) == 320

    try:
        board.med.buy_house(3)
    except LandException, e:
        pass
    try:
        board.med.sell_house(5)
    except LandException, e:
        pass
    try:
        board.verm.buy_house(1)
    except LandException, e:
        pass

def test_railroad_rent():
    board = setup_board()

    #rr, pr, bo, sl
    board.rr.set_owner(board.player(1))

    assert board.rr.charge_rent(board.banker, board.player(1)) == 0
    assert board.rr.charge_rent(board.banker, board.player(2)) == 25

    board.pr.set_owner(board.player(1))

    assert board.rr.charge_rent(board.banker, board.player(1)) == 0
    assert board.rr.charge_rent(board.banker, board.player(2)) == 50
    assert board.pr.charge_rent(board.banker, board.player(1)) == 0
    assert board.pr.charge_rent(board.banker, board.player(2)) == 50

    board.bo.set_owner(board.player(2))
    assert board.rr.charge_rent(board.banker, board.player(1)) == 0
    assert board.rr.charge_rent(board.banker, board.player(2)) == 50
    assert board.pr.charge_rent(board.banker, board.player(1)) == 0
    assert board.pr.charge_rent(board.banker, board.player(2)) == 50
    assert board.bo.charge_rent(board.banker, board.player(1)) == 25
    assert board.bo.charge_rent(board.banker, board.player(2)) == 0

    board.sl.set_owner(board.player(1))
    assert board.rr.charge_rent(board.banker, board.player(1)) == 0
    assert board.rr.charge_rent(board.banker, board.player(2)) == 100
    assert board.pr.charge_rent(board.banker, board.player(1)) == 0
    assert board.pr.charge_rent(board.banker, board.player(2)) == 100
    assert board.bo.charge_rent(board.banker, board.player(1)) == 25
    assert board.bo.charge_rent(board.banker, board.player(2)) == 0
    assert board.sl.charge_rent(board.banker, board.player(1)) == 0
    assert board.sl.charge_rent(board.banker, board.player(2)) == 100

    board.bo.set_owner(board.player(1))
    assert board.rr.charge_rent(board.banker, board.player(1)) == 0
    assert board.rr.charge_rent(board.banker, board.player(2)) == 200
    assert board.pr.charge_rent(board.banker, board.player(1)) == 0
    assert board.pr.charge_rent(board.banker, board.player(2)) == 200
    assert board.bo.charge_rent(board.banker, board.player(1)) == 0
    assert board.bo.charge_rent(board.banker, board.player(2)) == 200
    assert board.sl.charge_rent(board.banker, board.player(1)) == 0
    assert board.sl.charge_rent(board.banker, board.player(2)) == 200

def test_utility_rent():
    board = setup_board()

    board.electric.set_owner(board.player(1))
    board.dice.die1 = 1
    board.dice.die2 = 1
    assert (board.electric.charge_rent(board.banker, board.player(2)) == (board.dice.die1 + board.dice.die2) * 4)
    board.dice.die1 = 4
    board.dice.die2 = 3
    assert (board.electric.charge_rent(board.banker, board.player(2)) == (board.dice.die1 + board.dice.die2) * 4)

    board.water.set_owner(board.player(1))
    board.dice.die1 = 1
    board.dice.die2 = 1
    assert (board.electric.charge_rent(board.banker, board.player(2)) == (board.dice.die1 + board.dice.die2) * 10)
    assert (board.water.charge_rent(board.banker, board.player(2)) == (board.dice.die1 + board.dice.die2) * 10)
    board.dice.die1 = 4
    board.dice.die2 = 3
    assert (board.electric.charge_rent(board.banker, board.player(2)) == (board.dice.die1 + board.dice.die2) * 10)
    assert (board.water.charge_rent(board.banker, board.player(2)) == (board.dice.die1 + board.dice.die2) * 10)

def test_owner_type():
    assert type(board.player(1)) != str


# vim: ts=4:sw=4:expandtab
