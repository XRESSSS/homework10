from homework10 import check_age

def test_check_age_error():
    expected = 'передано не валідне значення віку, оскільки вік не може бути менше 0'
    user_age = -1
    actual = check_age(user_age)
    assert actual == expected

def test_check_age_kid():
    expected = 'користувач є дитиною'
    user_age = 15
    actual = check_age(user_age)
    assert actual == expected

def test_check_age_adult():
    expected = 'потрібно працювати'
    user_age = 20
    actual = check_age(user_age)
    assert actual == expected

def test_check_age_pensioner():
    expected = 'щасливої пенсії'
    user_age = 70
    actual = check_age(user_age)
    assert actual == expected
