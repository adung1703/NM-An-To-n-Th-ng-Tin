import gmpy2
import binascii
def factorize_level1(N):
    # Lấy căn bậc hai của N và làm tròn lên
    A = gmpy2.isqrt(N) + 1

    # Tìm giá trị x để A^2 - x^2 = N
    x = gmpy2.isqrt(A ** 2 - N)

    # Vòng lặp để tìm giá trị p và q
    while True:
        p = A - x
        q = A + x
        if p * q == N:
            break
        A += 1
        x = gmpy2.isqrt(A ** 2 - N)
    return p, q

# Thay vì phân tích N = p*q, ta phân tích 24N = 6p * 4q
def factorize_level2(N):
    # M = 24N
    M = 24 * N

    # Lấy căn bậc hai của 24N và làm tròn lên
    A = gmpy2.isqrt(M) + 1

    # Lặp cho tới khi x là số chính phương
    while True:
        x_squared = A ** 2 - M
        if gmpy2.is_square(x_squared):
            x = gmpy2.isqrt(x_squared)
            break
        A += 1
    p = (A - x) // 6
    q = (A + x) // 4

    return p, q

# Bài 1
N1 = gmpy2.mpz(
    "179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581"
)
p1, q1 = factorize_level1(N1)
print("Bài 1: Phân tích N1 = p1*q1, với p1, q1 là số nguyên tố")
print("\tp1:", p1)
print("\tq1:", q1)
print("\tKiểm tra p1 là số nguyên tố:", gmpy2.is_prime(p1))
print("\tKiểm tra q1 là số nguyên tố:", gmpy2.is_prime(q1))

# Bài 2
N2 = gmpy2.mpz(
    "648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877"
)
p2, q2 = factorize_level1(N2)
print("Bài 2: Phân tích N2 = p2*q2, với p2, q2 là số nguyên tố")
print("\tp2:", p2)
print("\tq2:", q2)
print("\tKiểm tra p2 là số nguyên tố:", gmpy2.is_prime(p2))
print("\tKiểm tra q2 là số nguyên tố:", gmpy2.is_prime(q2))

# Bài 3
N3 = gmpy2.mpz(
    "720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929"
    )
p3, q3 = factorize_level2(N3)
print("Bài 3: Phân tích N3 = p3*q3, với p3, q3 là số nguyên tố")
print("\tp3:", p3)
print("\tq3:", q3)
print("\tKiểm tra p3 là số nguyên tố:", gmpy2.is_prime(p3))
print("\tKiểm tra q3 là số nguyên tố:", gmpy2.is_prime(q3))

# Bài 4
N = N1
p = p1
q = q1
# Bản mã
y = gmpy2.mpz("22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540"
              )
phiN = (p-1)*(q-1)
e = 65537
d = gmpy2.powmod(e, -1, phiN)
x = gmpy2.powmod(y, d, N)

# Chuyển sang kiểu hex
hex_message = hex(x)[2:]

# Tìm vị trí bắt đầu bản rõ: '0x00' separator
separator_index = hex_message.index('00')

# Cắt phần bản rõ
ascii_message = hex_message[separator_index + 2:]

# Chuyển sang ASCII
plaintext = binascii.unhexlify(ascii_message).decode('utf-8')

print("Bài 4: Giải mã bản mã RSA")
print("\tBản rõ:\n\t\t", plaintext)


