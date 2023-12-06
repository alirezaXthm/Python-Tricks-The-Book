age = int(input())


def age_validation(age):
    assert age > 18 , 'you are under 18'
    return True

print(age_validation(age))