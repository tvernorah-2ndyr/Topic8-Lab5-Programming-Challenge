def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if 80 <= score <= 100:
        return "A"
    elif 60 <= score <= 79:
        return "B"
    elif 40 <= score <= 59:
        return "C"
    else:
        return "F"