import pytest
from train_fare import base_fare, concession, tatkal_charge


# ---------- base_fare ----------
def test_sleeper_fare():
    assert base_fare("SL", 500) == 500          # fare >= 50 (if False)

def test_base_fare_unknown_class():
    with pytest.raises(ValueError):
        base_fare("CC", 100)

def test_base_fare_invalid_distance():
    with pytest.raises(ValueError):
        base_fare("SL", 0)

def test_base_fare_negative_distance():
    with pytest.raises(ValueError):
        base_fare("3A", -10)

def test_base_fare_minimum_fare():
    assert base_fare("SL", 20) == 50            # fare < 50 (if True)

def test_base_fare_all_classes():
    assert base_fare("3A", 100) == 200
    assert base_fare("2A", 100) == 300
    assert base_fare("1A", 100) == 500


# ---------- concession ----------
def test_adult_no_concession():
    assert concession(30, "M", False) == 0      # falls through every condition

def test_tatkal_no_concession():
    assert concession(3, "M", True) == 0

def test_infant_concession():
    assert concession(3, "M", False) == 100

def test_child_concession():
    assert concession(10, "M", False) == 50

def test_child_boundary_age_12():
    assert concession(12, "F", False) == 50

def test_age_5_boundary():
    assert concession(5, "M", False) == 50

def test_senior_female_concession():
    assert concession(65, "F", False) == 50

def test_senior_male_concession():
    assert concession(65, "M", False) == 40

def test_senior_boundary_age_60():
    assert concession(60, "M", False) == 40

def test_age_59_no_concession():
    assert concession(59, "F", False) == 0


# ---------- tatkal_charge ----------
def test_tatkal_sleeper_min_charge():
    assert tatkal_charge("SL", 500) == 100      # charge < 100

def test_tatkal_ac_max_charge():
    assert tatkal_charge("1A", 5000) == 400     # charge > 400

def test_tatkal_sleeper_normal_charge():
    assert tatkal_charge("SL", 2000) == 200     # 100 <= charge <= 400

def test_tatkal_ac_normal_charge():
    assert tatkal_charge("3A", 1000) == 300

def test_tatkal_ac_low_charge():
    assert tatkal_charge("2A", 200) == 100
