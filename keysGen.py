import random

# Algoritmo de Miller-Rabin para verificar primalidad
def es_primo(n, k=10):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    # Escribir n-1 como 2^s * d con d impar
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    # Prueba de Miller-Rabin
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Función para generar un número primo grande
def generar_primo(bits):
    while True:
        primo = random.getrandbits(bits)
        if es_primo(primo):
            return primo

# Función para calcular el máximo común divisor (MCD)
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Algoritmo de Euclides extendido para encontrar el inverso modular
def euclides_extendido(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclides_extendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Generación de claves públicas y privadas RSA
def generar_claves(bits=1024):
    p = generar_primo(bits)
    q = generar_primo(bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Elegir e tal que 1 < e < φ(n) y mcd(e, φ(n)) = 1
    e = 65537  # Valor común de e
    while mcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Calcular d, el inverso modular de e mod φ(n)
    _, d, _ = euclides_extendido(e, phi_n)
    d = d % phi_n
    if d < 0:
        d += phi_n

    # Claves públicas y privadas
    clave_publica = (e, n)
    clave_privada = (d, n)

    return clave_publica, clave_privada, p, q

# Generación de las claves
#clave_publica, clave_privada, p, q = generar_claves()
p = 23971320714167150822653478663195394948037825543016543191917112831018209438098916949351916608262483809872321437137642073257248981764475483181751745216650123788347883602114656079226177329520106906008098346451679128897524488984281446454436340146078543585221025443829224731194866857409865556201549240215928223621
q = 14789921043624176197013089535594040788933999237145453953913590993322681505459789311006651366772194651330711198134739222568060758746887974836590003597661373097826185858745681807397101157683391231814627212530707313380058794522430182327957528218210654025834170477558652096361534468193409404243901797871546403981
n = p * q
clave_publica = (65537, n)
clave_privada = (276942956785646417770267455212819719013051788892167731739328350322902898531137174176229854593244771829597681145630409344037964870873295425083061873472913871227377223251056687303271239117015507783743673241488345627680133112221269194624526062571792588086050531987696310247389791890426404488726503557455209190318754745434450718419457811834169974652939171705130891457203989073446771900911105156980241295579849265493629939519145982655330194970735966692235322730472167297394859373167195497441750264714223507421279902448451190354783665836616719929697524948279478808142501835131314629580807132618902852836494294088109864673, n)
#print("Clave pública (e, n):", clave_publica)
#print("Clave privada (d, n):", clave_privada)
#print("\nNúmero primo p:", p)
#print("\nNúmero primo q:", q)
