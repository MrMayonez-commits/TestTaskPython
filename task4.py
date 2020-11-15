line1 = input()
line2 = input()
line1Len = len(line1)
line2Len = len(line2)
if line1Len > line2Len:
    line2  = line2 + '*' * (line1Len - line2Len )
else:
    line1 = line1 + '*' * (line2Len - line1Len )
X = max(line1Len,line2Len)
a = 0
for x in range(X):
    if line1[x] or line2[x] == '*':
        a = 0
    if line1[x] == line2[x]:
        a = 0
    if (line1[x] != line2[x]) and line1[x] != '*' and line2[x] != '*':
        a = a + 1
if a == 0:
    print('OK')
else:
    print('KO')