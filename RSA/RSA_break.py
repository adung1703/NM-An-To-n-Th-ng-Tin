#try:
    #from Crypto.Util.number import long_to_bytes, inverse
#except ImportError:
    #from Cryptodome.Util.number import long_to_bytes, inverse

from math import isqrt

# Hàm phân tích thừa số nguyên tố của N1 và N2 bằng phương pháp Fermat
def factorize(N):
    sqrt_N = isqrt(N)
    A = sqrt_N + 1
    while True:
        x_squared = A**2 - N
        x = isqrt(x_squared)
        if x * x == x_squared:
            p = A - x
            q = A + x
            return p, q
        A += 1

# Hàm phân tích thừa số nguyên tố của N3
def factorize_N3(N):
    A = isqrt(24 * N) + 1
    while True:
        x_squared = A**2 - 24 * N
        x = isqrt(x_squared)
        if x * x == x_squared:
            p = (2 * A - x) // 3
            q = (2 * A + x) // 3
            return p, q
        A += 1

# Hàm giải mã RSA
def decrypt_RSA(N, e, d, c):
    m = pow(c, d, N)
    return m

# Câu hỏi 1
N1 = int('179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581')
p1, q1 = factorize(N1)
print(f'Câu hỏi 1 - Phân tích thừa số nguyên tố của N1:')
print(f'  p1: {p1}')
print(f'  q1: {q1}\n')

# Câu hỏi 2
N2 = int('648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877')
p2, q2 = factorize(N2)
print(f'Câu hỏi 2 - Phân tích thừa số nguyên tố của N2:')
print(f'  p2: {p2}')
print(f'  q2: {q2}\n')

# Câu hỏi 3
N3 = int('720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929')
p3, q3 = factorize_N3(N3)
print(f'Câu hỏi 3 - Phân tích thừa số nguyên tố của N3:')
print(f'  p3: {p3}')
print(f'  q3: {q3}\n')

# Câu hỏi 4
phi_N1 = (p1 - 1) * (q1 - 1)
e = 65537
d1 = inverse(e, phi_N1)
c = int('2209645186741038177630656113488341801741006978789283107173183914367613560012053800428232965047350942434394621975151225646583996794288946076454204058156474898801373486412045232920176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540')
m1 = decrypt_RSA(N1, e, d1, c)

# Chuyển đổi thông điệp sang dạng bytes và in ra thông điệp ASCII
m1_bytes = long_to_bytes(m1)
ascii_message = m1_bytes.split(b'\x00')[1].decode('ascii', errors='ignore')
print(f'Câu hỏi 4 - Giải mã bản mã RSA:')
print(f'  ASCII message: {ascii_message}')
