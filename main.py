#1
class Kitob:
    def __init__(self, n, m):
        self.nomi = n
        self.muallif = m

kitob1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy")
print(f"Kitob 1: {kitob1.nomi} {kitob1.muallif}")

kitob2 = Kitob("Mehrobdan chayon", "Abdulla Qodiriy")
print(f"Kitob 2: {kitob2.nomi} {kitob2.muallif}")


#2
class Talaba:
    def __init__(self, i, y):
        self.ism = i
        self.yosh = y

talaba1 = Talaba("Ali", 20)
print(f"Talaba 1: {talaba1.ism} {talaba1.yosh}")

talaba2 = Talaba("Vali", 22)
print(f"Talaba 2: {talaba2.ism} {talaba2.yosh}")


#3
class Telefon:
    def __init__(self, m, n):
        self.model = m
        self.narx = n

tel1 = Telefon("iPhone 13", 1200)
print(f"Telefon 1: {tel1.model} {tel1.narx}")

tel2 = Telefon("Samsung S21", 900)
print(f"Telefon 2: {tel2.model} {tel2.narx}")


#4
class Shahar:
    def __init__(self, n, a):
        self.nomi = n
        self.aholi = a

shahar1 = Shahar("Toshkent", 3000000)
print(f"Shahar 1: {shahar1.nomi} {shahar1.aholi}")

shahar2 = Shahar("Samarqand", 600000)
print(f"Shahar 2: {shahar2.nomi} {shahar2.aholi}")


#5
class Mashina:
    def __init__(self, m, r):
        self.marka = m
        self.rang = r

m1 = Mashina("Cobalt", "oq")
print(f"m 1: {m1.marka} - {m1.rang}")

m2 = Mashina("Malibu", "qora")
print(f"m 2: {m2.marka} - {m2.rang}")

m3 = Mashina("Nexia", "kulrang")
print(f"m 2: {m2.marka} - {m2.rang}")


#6
class Talaba:
    def __init__(self, ism, yosh, kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs

ism1 = Talaba("Ali", 20, "2-kurs")
print(f"ism 1: {ism1.ism} - {ism1.yosh} - {ism1.kurs}")

ism2 = Talaba("Vali", 22, "3-kurs")
print(f"ism 2: {ism2.ism} - {ism2.yosh} - {ism2.kurs}")


#7
class Kitob:
    def __init__(self, n, m, s):
        self.nomi = n
        self.muallif = m
        self.sahifa_nomi = s

nom1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 300)
print(f"nom 1: {nom1.nomi} - {nom1.muallif} - {nom1.sahifa_nomi}")

nom2 = Kitob("Alkimyogar", "Paulo Coelho", 200)
print(f"nom 2: {nom2.nomi} - {nom2.muallif} - {nom2.sahifa_nomi}")


#8
class Telefon:
    def __init__(self, m, r, n):
        self.model = m
        self.rang = r
        self.narx = n

t1 = Telefon("iPhone 13", "qora", 1200)
print(f"t 1: {t1.model} - {t1.rang} - {t1.narx}")

t2 = Telefon("Samsung S21", "oq", 900)
print(f"t 2: {t2.model} - {t2.rang} - {t2.narx}")


#9
class Mashina:
    def __init__(self, m, r, y):
        self.marka = m
        self.rang = r
        self.yili = y

m1 = Mashina("Cobalt", "oq", 2022)
print(f"m 1: {m1.marka} - {m1.rang} - {m1.yili}")

m2 = Mashina("Malibu", "qora", 2023)
print(f"m 2: {m2.marka} - {m2.rang} - {m2.yili}")


#10
class Xodim:
    def __init__(self, i, l, m):
        self.ism = i
        self.lavozim = l
        self.maosh = m

x1 = Xodim("Ali", "Dasturchi", 1000)
print(f"x 1: {x1.ism} - {x1.lavozim} - {x1.maosh}")

x2 = Xodim("Vali", "Manager", 1500)
print(f"x 2: {x2.ism} - {x2.lavozim} - {x2.maosh}")

x3 = Xodim("Hasan", "Dizayner", 1200)
print(f"x 3: {x3.ism} - {x3.lavozim} - {x3.maosh}")
