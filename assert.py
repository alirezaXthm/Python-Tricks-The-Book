age = int(input('How old are you?'))
gender = input('Gender (M/F)?')

def age_validation(age):
    assert age > 18 , 'you are under 18'
    return True
        
print(age_validation(age))

if gender == 'M':
    print('you are a man!')
elif gender == 'F':
    print('sorry this is for men :)')
else:
    assert False, f'what the fuck is the "{gender}" gender?'
        