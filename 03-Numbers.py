# Calculate the area of a rectangle (Area = Width x Length)
Width = float(input('What is the width of your rectangle? '))
Length = float(input('What is the length of your rectangle? '))

Area = Width * Length

print('The area of your rectangle is %.2f' %Area)

print('\n')

# Calculate the area of a triangle (Area = Width x Height/2)
Width = float(input('What is the base length of your triangle? '))

Height = float(input('What is the height of your triangle? '))

Area = Width * Height / 2

print('The area of your triangle is %.2f' %Area)

print('\n')

# How to format numbers to display to users
# f stands for float and d stands for decimal

print('I have %d cats' % 6)
# This will print 'I have 6 cats'
print('I have %3d cats' % 6)
# This will print 'I have    6 cats'
print('I have %03d cats' % 6)
# This will print 'I have 006 cats'
print('I have %f cats' % 6)
# This will print 'I have 6.000000 cats'
print('I have %.2f cats' % 6)
# This will print 'I have 6.00 cats' (2 decimal places)
print('I have %.3f cats' %6)
# This will print 'I have 6.000 cats' (3 decimal places)

print('\n')

# Calculate the value of z, based on user-input for x and y
print('You will enter values for the following equation:  x * y = z')
x = float(input('Enter a value for x? '))

y = float(input('Enter a value for y? '))

z = x * y

print('The value for z is %.2f' %z)