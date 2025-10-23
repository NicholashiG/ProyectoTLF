"""
Test Cases: Ejemplos de texto para validar el funcionamiento del sistema
Incluye diferentes tipos de patrones para análisis léxico y validación
"""

# Casos de prueba organizados por categorías

def get_test_cases():
    """Retorna diccionario con casos de prueba organizados"""
    
    test_cases = {
        "emails": {
            "validos": [
                "usuario@ejemplo.com",
                "test.email@dominio.co",
                "admin@universidad.edu.co",
                "contacto@empresa.org",
                "soporte123@servicio.net"
            ],
            "invalidos": [
                "email_sin_arroba.com",
                "@dominio.com",
                "usuario@",
                "usuario@.com",
                "usuario@@dominio.com"
            ]
        },
        
        "telefonos": {
            "validos": [
                "3001234567",
                "+57 300 123 4567",
                "57-315-555-0123",
                "+573001234567",
                "3151234567"
            ],
            "invalidos": [
                "123456789",  # Muy corto
                "12345678901",  # Muy largo
                "2001234567",  # No inicia con 3
                "300-123-456",  # Formato incorrecto
                "abc1234567"  # Contiene letras
            ]
        },
        
        "fechas": {
            "validos": [
                "25/12/2024",
                "2024/01/15",
                "01-06-2025",
                "15/03/2023",
                "2025-12-31"
            ],
            "invalidos": [
                "32/12/2024",  # Día inválido
                "25/13/2024",  # Mes inválido
                "25/12/24",    # Año de 2 dígitos
                "2024/1/1",    # Sin ceros
                "25-12-2024"   # Formato mixto
            ]
        },
        
        "cedulas": {
            "validos": [
                "12345678",
                "1234567890",
                "987654321",
                "123456789",
                "12345678901"  # Límite superior
            ],
            "invalidos": [
                "1234567",     # Muy corto
                "01234567",    # Inicia con 0
                "abc1234567",  # Contiene letras
                "12345678A",   # Termina con letra
                "12.345.678"   # Contiene puntos
            ]
        },
        
        "urls": {
            "validos": [
                "https://www.google.com",
                "http://localhost:8080",
                "https://github.com/user/repo",
                "https://universidad.edu.co/facultad",
                "http://192.168.1.1:3000/api"
            ],
            "invalidos": [
                "www.google.com",        # Sin protocolo
                "ftp://servidor.com",    # Protocolo incorrecto
                "https://",              # Sin dominio
                "http://local host",     # Espacio en dominio
                "https://.com"           # Dominio inválido
            ]
        },
        
        "codigos_postales": {
            "validos": [
                "630001",
                "660001",
                "170001",
                "110111",
                "050001"
            ],
            "invalidos": [
                "12345",      # Muy corto
                "1234567",    # Muy largo
                "A63001",     # Contiene letra
                "63000A",     # Termina con letra
                "63-001"      # Contiene guion
            ]
        },
        
        "ip_addresses": {
            "validos": [
                "192.168.1.1",
                "127.0.0.1",
                "8.8.8.8",
                "255.255.255.255",
                "10.0.0.1"
            ],
            "invalidos": [
                "192.168.1",      # Incompleta
                "192.168.1.256",  # Octeto > 255
                "192.168.1.1.1",  # Demasiados octetos
                "192.168.01.1",   # Cero inicial
                "192.168.a.1"     # Contiene letra
            ]
        },
        
        "placas_vehiculo": {
            "validos": [
                "ABC123",
                "XYZ-789",
                "DEF 456",
                "GHI789",
                "JKL-012"
            ],
            "invalidos": [
                "AB123",       # Muy pocas letras
                "ABCD123",     # Demasiadas letras
                "ABC12",       # Muy pocos números
                "ABC1234",     # Demasiados números
                "123ABC"       # Orden incorrecto
            ]
        },
        
        "passwords_seguras": {
            "validos": [
                "MiPassword123!",
                "Segura2024@",
                "Clave#Fuerte9",
                "Sistema$2025",
                "Proyecto&TLF8"
            ],
            "invalidos": [
                "password",        # Sin mayúscula, número, especial
                "PASSWORD123",     # Sin minúscula, especial
                "Password!",       # Sin número
                "Password123",     # Sin carácter especial
                "Pass1!"           # Muy corta
            ]
        }
    }
    
    return test_cases


def get_mixed_text_examples():
    """Retorna ejemplos de texto mixto para análisis completo"""
    
    examples = [
        # Ejemplo 1: Información de contacto
        """
        Contacto de emergencia:
        Email: admin@hospital.com
        Teléfono: +57 300 123 4567
        Dirección IP del servidor: 192.168.1.100
        Fecha de actualización: 15/12/2024
        Código postal: 630001
        """,
        
        # Ejemplo 2: Datos de usuario
        """
        Registro de usuario:
        Correo: usuario.test@universidad.edu.co
        Cédula: 1234567890
        Teléfono móvil: 3151234567
        Fecha de nacimiento: 25/03/1995
        Sitio web personal: https://miportfolio.com
        Contraseña: MiClave123!
        """,
        
        # Ejemplo 3: Información de vehículo
        """
        Datos del vehículo:
        Placa: ABC-123
        Fecha de matrícula: 2024/01/15
        Propietario: juan.perez@email.com
        Cédula propietario: 987654321
        Teléfono: 57-315-555-0123
        """,
        
        # Ejemplo 4: Configuración de red
        """
        Configuración de red:
        IP Gateway: 192.168.1.1
        IP DNS: 8.8.8.8
        IP Servidor: 10.0.0.100
        URL Admin: http://admin.local:8080
        Fecha configuración: 01-06-2025
        Admin email: network@company.org
        """,
        
        # Ejemplo 5: Texto con errores intencionados
        """
        Datos con errores:
        Email inválido: usuario@
        Teléfono malo: 123456789
        Fecha incorrecta: 32/13/2024
        IP errónea: 300.300.300.300
        Cédula inválida: 01234567
        URL mal formada: www.sitio.com
        Placa incorrecta: 123ABC
        """
    ]
    
    return examples


def get_performance_test_text():
    """Retorna texto largo para pruebas de rendimiento"""
    
    test_cases = get_test_cases()
    performance_text = "Texto de prueba de rendimiento con múltiples patrones:\n\n"
    
    # Repetir todos los patrones válidos varias veces
    for category, patterns in test_cases.items():
        performance_text += f"=== {category.upper()} ===\n"
        for valid_pattern in patterns["validos"]:
            performance_text += f"{valid_pattern} "
        for invalid_pattern in patterns["invalidos"]:
            performance_text += f"{invalid_pattern} "
        performance_text += "\n\n"
    
    # Repetir el texto varias veces para crear un documento grande
    large_text = performance_text * 10
    
    return large_text


def get_edge_cases():
    """Retorna casos extremos para pruebas"""
    
    edge_cases = [
        # Texto vacío
        "",
        
        # Solo espacios
        "   \n\n\t  ",
        
        # Solo puntuación
        "!@#$%^&*()[]{}.,;:",
        
        # Un solo carácter
        "a",
        
        # Texto muy largo de un solo token
        "a" * 1000,
        
        # Mezcla de caracteres especiales con patrones
        "!!!admin@test.com??? 3001234567### 25/12/2024$$$",
        
        # Patrones en diferentes líneas
        """admin@test.com
        3001234567
        25/12/2024
        https://test.com""",
        
        # Patrones con espacios extra
        "  admin@test.com   3001234567  25/12/2024  ",
    ]
    
    return edge_cases


if __name__ == "__main__":
    # Función de prueba para mostrar ejemplos
    print("=== CASOS DE PRUEBA DISPONIBLES ===")
    
    test_cases = get_test_cases()
    for category, patterns in test_cases.items():
        print(f"\n{category.upper()}:")
        print(f"  Válidos: {patterns['validos']}")
        print(f"  Inválidos: {patterns['invalidos']}")
    
    print("\n=== EJEMPLOS DE TEXTO MIXTO ===")
    examples = get_mixed_text_examples()
    for i, example in enumerate(examples, 1):
        print(f"\nEjemplo {i}:")
        print(example.strip())