a=int(input("nhap so"))
for i in range(1, a-1):
    if a&i == 0:
        b= False
        break
if b:
    print("a la so nguyen to")
else:
    print("a khong phai la so nguyen to")