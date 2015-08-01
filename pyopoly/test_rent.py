from rent import Rent
from property import Property,PropertyGroup

player1 = "1"
player2 = "2"

def setup_purple():
    med = Property(name="Mediteranian Ave.")
    baltic = Property(name="Baltic Ave.")
    purple = PropertyGroup(med, baltic, name="Purple")
    return med, baltic, purple

def setup_lightblue():
    ori = Property(name="Oriental Ave.")
    verm = Property(name="Vermont Ave.")
    conn = Property(name="Connecticut Ave.")
    lightblue = PropertyGroup(ori, verm, conn, name="Light Blue")
    return ori, verm, conn, lightblue

def test_property():
    med, baltic, purple = setup_purple()

    assert med in purple.properties
    assert baltic in purple.properties
    assert len(purple.properties) == 2

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

# vim: ts=4:sw=4:expandtab
