from property import Property,Utility,Railroad,PropertyGroup

# TODO: These should be player classes
player1 = "1"
player2 = "2"

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

def test_owner_type():
    assert type(player1) != str

def test_property():
    med, baltic, purple = setup_purple()

    assert med in purple.properties
    assert baltic in purple.properties
    assert len(purple.properties) == 2

def test_railroads():
    rr, pr, bo, sl, railroads = setup_railroad()

    assert rr in railroads.properties
    assert pr in railroads.properties
    assert bo in railroads.properties
    assert sl in railroads.properties
    assert len(railroads.properties) == 4

def test_utilities():
    electric, water, utilities = setup_utilities()

    assert water in utilities.properties
    assert electric in utilities.properties
    assert len(utilities.properties) == 2

def test_group_owner():
    med, baltic, purple = setup_purple()
    ori, verm, conn, lightblue = setup_lightblue()

    med.set_owner(player1)
    baltic.set_owner(player1)
    ori.set_owner(player1)
    verm.set_owner(player2)

    assert purple.all_owned(player1)
    assert not purple.all_owned(player2)

    assert not lightblue.all_owned(player1)
    assert not lightblue.all_owned(player2)

def test_property_rent():
    med, baltic, purple = setup_purple()
    ori, verm, conn, lightblue = setup_lightblue()

    med.set_owner(player1)
    baltic.set_owner(player1)
    ori.set_owner(player1)
    verm.set_owner(player2)

    assert med.charge_rent(player1) == 0
    assert med.charge_rent(player2) == 2
    assert baltic.charge_rent(player1) == 0
    assert baltic.charge_rent(player2) == 4
    assert ori.charge_rent(player1) == 0
    assert ori.charge_rent(player2) == 30
    assert verm.charge_rent(player1) == 30
    assert verm.charge_rent(player2) == 0

def test_property_houses():
    raise BaseException("Implement me!")

def test_property_hotel():
    raise BaseException("Implement me!")

def test_hotel():
    raise BaseException("Implement me!")

def test_utility_rent():
    raise BaseException("Implement me!")

def test_railroad_rent():
    raise BaseException("Implement me!")

# vim: ts=4:sw=4:expandtab
