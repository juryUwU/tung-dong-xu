import random

An = random.randint(0,1)
Binh = random.randint(0,1)
Cuong = random.randint(0,1)

if An == 0 and Binh == 0 and Cuong == 0:
    print(An, Binh, Cuong, "=> cả ba cùng sấp")
elif An == 1 and Binh == 1 and Cuong == 1:
    print(An, Binh, Cuong, "=> cả ba cùng ngửa")
elif An == 0 and Binh == 1 and Cuong == 1:
    print(An, "An thắng")
elif An == 1 and Binh == 0 and Cuong == 1:
    print(Binh, "Bình thắng")
elif An == 1 and Binh == 1 and Cuong == 0:
    print(Cuong, "Cường thắng")
elif An == 1 and Binh == 0 and Cuong == 0:
    print(An, "An thắng")
elif An == 0 and Binh == 1 and Cuong == 0:
    print(Binh, "Bình thắng")
elif An == 0 and Binh == 0 and Cuong == 1:
    print(Cuong, "Cường thắng")

