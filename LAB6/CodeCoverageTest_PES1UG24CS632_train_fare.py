import pytest
from train_fare import base_fare, concession, tatkal_charge


# ---------- base_fare ----------
def test_sleeper_fare():
    assert base_fare("SL", 500) == 500

def test_base_fare_unknown_class():
    with pytest.raises(ValueError):
        base_fare("CC", 100)

def test_base_fare_invalid_distance():
    with pytest.raises(ValueError):
        base_fare("SL", 0)

def test_base_fare_minimum_fare():
    assert base_fare("SL", 20) == 50


# ---------- concession ----------
def test_adult_no_concession():
    assert concession(30, "M", False) == 0

def test_tatkal_no_concession():
    assert concession(3, "M", True) == 0

def test_infant_concession():
    assert concession(3, "M", False) == 100

def test_child_concession():
    assert concession(10, "M", False) == 50

def test_senior_female_concession():
    assert concession(65, "F", False) == 50

def test_senior_male_concession():
    assert concession(65, "M", False) == 40


# ---------- tatkal_charge ----------
def test_tatkal_sleeper_min_charge():
    assert tatkal_charge("SL", 500) == 100

def test_tatkal_ac_max_charge():
    assert tatkal_charge("1A", 5000) == 400
