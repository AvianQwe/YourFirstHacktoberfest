# dits-o-dahs

# .... .- -.-. -.- - --- -... . .-. ..-. . ... - -.-.--

# Solution:
morse = {
    'A':'.-','B':'-...','C':'-.-.','D':'-..',
    'E':'.','F':'..-.','G':'--.','H':'....',
    'I':'..','J':'.---','K':'-.-','L':'.-..',
    'M':'--','N':'-.','O':'---','P':'.--.',
    'Q':'--.-','R':'.-.','S':'...','T':'-',
    'U':'..-','V':'...-','W':'.--','X':'-..-',
    'Y':'-.--','Z':'--..','!':'-.-.--'}
rev_morse = {morse[x]:x for x in morse.keys()}

[print(rev_morse[i], end = "") for i in ".... .- -.-. -.- - --- -... . .-. ..-. . ... - -.-.--".split()]


# Output :  HACKTOBERFEST!