from grading import letter_grade


def test_boundary_39_40():
    assert letter_grade(39) == "F"
    assert letter_grade(40) == "C"


def test_boundary_59_60():
    assert letter_grade(59) == "C"
    assert letter_grade(60) == "B"


def test_boundary_79_80():
    assert letter_grade(79) == "B"
    assert letter_grade(80) == "A"