import pytest


@pytest.mark.parametrize("input_one, expected", [(85, "Normal"), (50, "Borderline Low"), (30, "Low")])


def test_check_HDL(input_one, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input_one)
    assert answer == expected


'''
def test_check_HDL_Normal():
    from blood_calculator import check_HDL
    answer = check_HDL(85)
    expected = "Normal"
    assert answer == expected

def test_check_HDL_BorderlineLow():
    from blood_calculator import check_HDL
    answer = check_HDL(50)
    expected = "Borderline Low"
    assert answer == expected

def test_check_HDL_Low():
    from blood_calculator import check_HDL
    answer = check_HDL(30)
    expected = "Low"
    assert answer == expected
'''
