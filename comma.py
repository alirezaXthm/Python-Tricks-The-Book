list1 = ['1',
       '2',
       '3' #missing a comma
       '4'
       ]
print(list1)
'''
This so-called “string literal concatenation” is intentional
and documented behavior.
''' 
print('hello' "world")
'''
Thus, "hello" 'world' is equivalent to "helloworld".
'''
my_str = ('This is a super long string constant '
'spread out across multiple lines. '
'And look, no backslash characters needed!')
print(my_str)

list2 = ['one',
          'two',
          'three',
          'four', #comma 
          ]
print(list2)
'''
you can place a comma after every item in a list, dict, or set
constant, including the last item.
That’ll make it easy to add or
remove new items without having to update the comma placement
'''

'''
Key Takeaways
• Smart formatting and comma placement can make your list,
dict, or set constants easier to maintain.
• Python’s string literal concatenation feature can work to your
benefit, or introduce hard-to-catch bugs.
'''