from property import Property,Utility,Railroad,PropertyGroup,LandException

# TODO: These should be player classes
player1 = "1"
player2 = "2"

class Board(object):
    def __init__(self):
        self.init = False

board = Board()

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

    board.med.set_owner(player1)
    board.baltic.set_owner(player1)
    board.ori.set_owner(player1)
    board.verm.set_owner(player2)

    assert board.purple.all_owned(player1)
    assert not board.purple.all_owned(player2)

    assert not board.lightblue.all_owned(player1)
    assert not board.lightblue.all_owned(player2)

def test_property_rent():
    board = setup_board()

    board.med.set_owner(player1)
    board.baltic.set_owner(player1)
    board.ori.set_owner(player1)
    board.verm.set_owner(player2)

    # Player 1 owns both purple, so rent should be double
    assert board.med.charge_rent(player1) == 0
    assert board.med.charge_rent(player2) == 4
    assert board.baltic.charge_rent(player1) == 0
    assert board.baltic.charge_rent(player2) == 8
    assert board.ori.charge_rent(player1) == 0
    assert board.ori.charge_rent(player2) == 30
    assert board.verm.charge_rent(player1) == 30
    assert board.verm.charge_rent(player2) == 0

def test_property_houses():
    board = setup_board()

    board.med.set_owner(player1)
    board.baltic.set_owner(player1)

    board.med.buy_house(3)
    board.baltic.buy_house(4)

    assert board.med.charge_rent(player1) == 0
    assert board.med.charge_rent(player2) == 90
    assert board.baltic.charge_rent(player1) == 0
    assert board.baltic.charge_rent(player2) == 320

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
    board.rr.set_owner(player1)

    assert board.rr.charge_rent(player1) == 0
    assert board.rr.charge_rent(player2) == 25

    board.pr.set_owner(player1)

    assert board.rr.charge_rent(player1) == 0
    assert board.rr.charge_rent(player2) == 50
    assert board.pr.charge_rent(player1) == 0
    assert board.pr.charge_rent(player2) == 50

    board.bo.set_owner(player2)
    assert board.rr.charge_rent(player1) == 0
    assert board.rr.charge_rent(player2) == 50
    assert board.pr.charge_rent(player1) == 0
    assert board.pr.charge_rent(player2) == 50
    assert board.bo.charge_rent(player1) == 25
    assert board.bo.charge_rent(player2) == 0

    board.sl.set_owner(player1)
    assert board.rr.charge_rent(player1) == 0
    assert board.rr.charge_rent(player2) == 100
    assert board.pr.charge_rent(player1) == 0
    assert board.pr.charge_rent(player2) == 100
    assert board.bo.charge_rent(player1) == 25
    assert board.bo.charge_rent(player2) == 0
    assert board.sl.charge_rent(player1) == 0
    assert board.sl.charge_rent(player2) == 100

    board.bo.set_owner(player1)
    assert board.rr.charge_rent(player1) == 0
    assert board.rr.charge_rent(player2) == 200
    assert board.pr.charge_rent(player1) == 0
    assert board.pr.charge_rent(player2) == 200
    assert board.bo.charge_rent(player1) == 0
    assert board.bo.charge_rent(player2) == 200
    assert board.sl.charge_rent(player1) == 0
    assert board.sl.charge_rent(player2) == 200

def test_utility_rent():
    raise BaseException("Implement me!")

def test_owner_type():
    assert type(player1) != str


# vim: ts=4:sw=4:expandtab
