def check_age(user_age: int) -> str:
    if user_age < 0:
        result = 'передано не валідне значення віку, оскільки вік не може бути менше 0'
    elif user_age <= 1 and user_age <= 18:
        result = 'користувач є дитиною'
    elif user_age <= 19 and user_age <= 65:
        result = 'потрібно працювати'
    else:
        result = 'щасливої пенсії'
    return result

