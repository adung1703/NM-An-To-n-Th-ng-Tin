import gmpy2

def factorize_N1(N):
    sqrt_N = gmpy2.isqrt(N)
    A = sqrt_N + 1
    while True:
        x_squared = A**2 - N
        if x_squared >= 0 and gmpy2.is_square(x_squared):
            x = gmpy2.isqrt(x_squared)
            p = A - x
            q = A + x
            return int(p), int(q)
        A += 1

def factorize_N2(N):
    sqrt_N = gmpy2.isqrt(N)
    A = sqrt_N + 1
    while True:
        x_squared = A**2 - N
        if x_squared >= 0 and gmpy2.is_square(x_squared):
            x = gmpy2.isqrt(x_squared)
            p = A - x
            q = A + x
            return int(p), int(q)
        A += 1

def factorize_N3(N):
    A = gmpy2.isqrt(24 * N) + 1
    while True:
        x_squared = A**2 - 24 * N
        if gmpy2.is_square(x_squared):
            x = gmpy2.isqrt(x_squared)
            break
        A += 1
    p = (A - x) // 6
    q = (A + x) // 4
    return int(p), int(q)

def decrypt_RSA(N, e, d, c):
    m = gmpy2.powmod(c, d, N)
    return m

# Câu hỏi 1
N1 = gmpy2.mpz('179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581')
p1, q1 = factorize_N1(N1)
print(f'Câu hỏi 1 - Phân tích thừa số nguyên tố của N1:')
print(f'  p1: {p1}')
print(f'  q1: {q1}\n')
print("Kiểm tra p1: ", gmpy2.is_prime(p1))
print("Kiểm tra q1: ", gmpy2.is_prime(q1))

# Câu hỏi 2
N2 = gmpy2.mpz('648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877')
p2, q2 = factorize_N2(N2)
print(f'Câu hỏi 2 - Phân tích thừa số nguyên tố của N2:')
print(f'  p2: {p2}')
print(f'  q2: {q2}\n')
print("Kiểm tra p2: ", gmpy2.is_prime(p2))
print("Kiểm tra q2: ", gmpy2.is_prime(q2))

# Câu hỏi 3
N3 = gmpy2.mpz('720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929')
p3, q3 = factorize_N3(N3)
print(f'Câu hỏi 3 - Phân tích thừa số nguyên tố của N3:')
print(f'  p3: {p3}')
print("Kiểm tra p3: ", gmpy2.is_prime(p3))
print(f'  q3: {q3}')
print("Kiểm tra q3: ", gmpy2.is_prime(q3))
print("N =", gmpy2.mul(p3, q3))

# bai 4
# Extract the ASCII message from the PKCS1 padding
import binascii

def decrypt_rsa(N, e, C, p, q):
    # Compute phi(N)
    phi_N = (p - 1) * (q - 1)
    
    # Compute the modular inverse of e
    d = pow(e, -1, phi_N)
    
    # Decrypt the ciphertext
    M = pow(C, d, N)
    
    return M

N = 179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581
e = 65537
C = int('22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540', 10)
p = p1
q = q1

M = decrypt_rsa(N, e, C, p, q)

# Convert the decrypted message to hex
hex_message = hex(M)[2:]

# Locate '0x00' separator
separator_index = hex_message.index('00')

# Extract the ASCII part after the separator
ascii_message = hex_message[separator_index + 2:]

# Convert to ASCII
plaintext = binascii.unhexlify(ascii_message).decode('utf-8')

print(f"Bai 4:")
print(f"Decrypted message: {plaintext}")
