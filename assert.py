age = int(input('How old are you?'))
gender = input('Gender (M/F)?').upper()

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
        

# Caveat One  
# NEVER user assertion for Data Validation!
'''
def delete_product(prod_id, user):
    assert user.is_admin(), 'Must be admin'
    assert store.has_product(prod_id), 'Unknown product'
    store.get_product(prod_id).delete()
'''
# do this instead
'''
def delete_product(product_id, user):
    if not user.is_admin():
        raise AuthError('Must be admin to delete')
    if not store.has_product(product_id):
        raise ValueError('Unknown product id')
        store.get_product(product_id).delete()
'''


# Caveat two
# Asserts That Never Fail
assert(1 == 2, 'This should fail')
assert (
10 == 12, 'It always passes...'
)



"""
Key Takeaways
• Python's assert statement is a debugging aid that tests a condition
as an internal self-check in your program.
• Asserts should only be used to help developers identify bugs.
They're not a mechanism for handling run-time errors.
• Asserts can be globally disabled with an interpreter setting.
24

python will raise this to help you with a warning:
SyntaxWarning: assertion is always true, perhaps remove parentheses?
"""