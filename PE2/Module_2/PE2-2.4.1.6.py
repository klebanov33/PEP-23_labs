a = ['  # ','  # ','  # ','  # ','  # ',]
b = ['### ','  # ','### ','#   ','### ',]
c = ['### ','  # ','### ','  # ','### ',]
d = ['# # ','# # ','### ','  # ','  # ',]
e = ['### ','#   ','### ','  # ','### ',]
f = ['### ','#   ','### ','# # ','### ',]
g = ['### ','  # ','  # ','  # ','  # ',]
h = ['### ','# # ','### ','# # ','### ',]
i = ['### ','# # ','### ','  # ','### ',]
j = ['### ','# # ','# # ','# # ','### ',]

x0 = ""
x1 = ""
x2 = ""
x3 = ""
x4 = ""

num = input("Enter number: ")

new_lst = list(num)

for ch in new_lst:
    if ch == '1':
        y0, y1, y2, y3, y4 = a[0], a[1], a[2], a[3], a[4]
    if ch == '2':
        y0, y1, y2, y3, y4 = b[0], b[1], b[2], b[3], b[4]
    if ch == '3':
        y0, y1, y2, y3, y4 = c[0], c[1], c[2], c[3], c[4]
    if ch == '4':
        y0, y1, y2, y3, y4 = d[0], d[1], d[2], d[3], d[4]
    if ch == '5':
        y0, y1, y2, y3, y4 = e[0], e[1], e[2], e[3], e[4]
    if ch == '6':
        y0, y1, y2, y3, y4 = f[0], f[1], f[2], f[3], f[4]
    if ch == '7':
        y0, y1, y2, y3, y4 = g[0], g[1], g[2], g[3], g[4]
    if ch == '8':
        y0, y1, y2, y3, y4 = h[0], h[1], h[2], h[3], h[4]
    if ch == '9':
        y0, y1, y2, y3, y4 = i[0], i[1], i[2], i[3], i[4]
    if ch == '0':
        y0, y1, y2, y3, y4 = j[0], j[1], j[2], j[3], j[4]

    x0 += y0
    x1 += y1
    x2 += y2
    x3 += y3
    x4 += y4 

    y0 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0

print(x0)  
print(x1)
print(x2)
print(x3)
print(x4) 
