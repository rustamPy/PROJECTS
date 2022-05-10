import scripts.creator as c
import pytest
@pytest.fixture()
def list_val():
    return []
@pytest.fixture(autouse=True)
def add_val(list_val):
    list_val.append(3)
    return list_val
    #Hello
@pytest.mark.parametrize('val',[2,3,4])
def test_april_2(add_val,val):

    assert add_val==[val]

def test_april_3():
    assert 4==4
