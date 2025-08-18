"""
print("Manthan")
print(3+1)
"""
print("Manthan Patel is \n \'a\' \"software developer\"");
#print("Manthan Patel")

"""
you can comments the line using the multiline=Using Triple Quotes("""""",'''''') and single-line=#;
"""
print("Manthan","Khushbu",sep="~")

# \\ - Backslash
print("Backslash: \\")

# \' - Single quote
print('Single quote: I\'m happy')

# \" - Double quote
print("Double quote: She said, \"Hello!\"")

# \n - Newline
print("First Line\nSecond Line")

# \t - Horizontal tab
print("Name\tAge\tCity")

# \r - Carriage return
print("12345\rAB")  # Overwrites beginning: Output likely "AB345"

# \b - Backspace
print("Oops\b!")  # Removes 's': Output likely "Oop!"

# \f - Form feed (rarely visible in terminal, used in printers)
print("Page 1\fPage 2")

# \v - Vertical tab (rarely used, can act like newline)
print("Line1\vLine2")

# \a - Bell/alert (may make a sound in some terminals)
print("Alert\a")  # Might beep

# \0 - Null character
print("Null\0Character")  # Null is invisible but present

# \N{name} - Unicode character by name
print("Unicode by name: \N{COPYRIGHT SIGN}")

# \uXXXX - Unicode with 16-bit hex
print("Unicode heart: \u2764")  # ❤

# \UXXXXXXXX - Unicode with 32-bit hex
print("Unicode emoji: \U0001F600")  # 😀

# \xXX - Character with hex value
print("Hex A: \x41")  # A
