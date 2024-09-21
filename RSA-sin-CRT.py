from keysGen import clave_privada, clave_publica

# Algoritmo 'Square and Multiply' para exponenciación modular
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

# Función para descifrar un mensaje usando la clave privada
def descifrar(mensaje_cifrado, clave_privada):
    d, n = clave_privada
    mensaje_descifrado = ''.join([chr(exponenciacion_rapida(char, d, n)) for char in mensaje_cifrado])
    return mensaje_descifrado

# Prueba de cifrado y descifrado
mensaje_original = "Hola, RSA!"
mensaje_cifrado = cifrar(mensaje_original, clave_publica)
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = descifrar(mensaje_cifrado, clave_privada)
print("Mensaje descifrado:", mensaje_descifrado)
