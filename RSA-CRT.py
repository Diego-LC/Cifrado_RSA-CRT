from keysGen import clave_privada, clave_publica, p, q, euclides_extendido

#  Algoritmo 'Square and Multiply' para exponenciación modular (usado para cifrar y descifrar)
def exponenciacion_rapida(base, exponente, modulo):
    resultado = 1
    while exponente > 0:
        if exponente % 2 == 1:
            resultado = (resultado * base) % modulo
        base = (base * base) % modulo
        exponente //= 2
    return resultado


# Función para cifrar un mensaje usando la clave pública
def cifrar(mensaje, clave_publica):
    e, n = clave_publica
    mensaje_cifrado = [exponenciacion_rapida(ord(char), e, n) for char in mensaje]
    return mensaje_cifrado


# Descifrado usando el Teorema del Resto Chino (CRT)
def descifrar_con_crt(c, clave_privada, p, q):
    d, n = clave_privada
    
    # Calcular dp = d mod (p-1) y dq = d mod (q-1)
    dp = d % (p - 1)
    dq = d % (q - 1)
    
    # Calcular el inverso de q mod p
    _, q_inv, _ = euclides_extendido(q, p)
    
    # c mod p y c mod q
    m1 = exponenciacion_rapida(c, dp, p)
    m2 = exponenciacion_rapida(c, dq, q)
    
    # Usar CRT para combinar los resultados
    h = (q_inv * (m1 - m2)) % p
    m = (m2 + h * q) % n
    
    return m


# Función para descifrar un mensaje cifrado
def descifrar_mensaje_con_crt(mensaje_cifrado, clave_privada, p, q):
    mensaje_descifrado = ''.join([chr(descifrar_con_crt(char, clave_privada, p, q)) for char in mensaje_cifrado])
    return mensaje_descifrado

# Prueba de cifrado y descifrado usando CRT
mensaje_original = "Hola, RSA!"
mensaje_cifrado = cifrar(mensaje_original, clave_publica)
print("Mensaje cifrado:", mensaje_cifrado)

# Recordar que en la generación de claves, ya se tienen p y q
# Usar el descifrado con CRT
mensaje_descifrado_crt = descifrar_mensaje_con_crt(mensaje_cifrado, clave_privada, p, q)
print("Mensaje descifrado con CRT:", mensaje_descifrado_crt)
