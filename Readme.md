# Implementación de un Sistema de Cifrado RSA con Cambio de Bases y Teorema del Resto Chino (CRT)

## Descripción

Este proyecto implementa el algoritmo de cifrado RSA, incorporando optimizaciones como el Teorema del Resto Chino (CRT) para mejorar la eficiencia en las operaciones de descifrado. También se utilizan técnicas de exponenciación modular rápida ('square and multiply') y un proceso de cambio de bases en el cifrado.

## Características

- **Generación de Claves RSA**: Generación de dos grandes números primos (p, q), cálculo de la clave pública y privada, pruebas de primalidad.
- **Cifrado de Mensajes**: Implementación del cifrado modular usando 'square and multiply'.
- **Descifrado Optimizado**: Descifrado acelerado mediante el uso del CRT.
- **Exponenciación Modular Rápida**: Optimización en el cálculo de potencias modulares.

## Archivos

- `keysGen.py`: Generación de las claves públicas y privadas (p, q, n, e, d).
- `RSA-CRT.py`: Cifrado y descifrado de mensajes utilizando CRT.
- `RSA-sin-CRT.py`: Cifrado y descifrado de mensajes sin utilizar CRT.

## Requisitos

- Python 3.8+
- Bibliotecas estándar de Python

## Ejecución

1. Ejecución:

   ```bash
   python RSA-CRT.py
