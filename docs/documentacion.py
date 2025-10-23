"""
Documentación Técnica del Proyecto
Sistema de Análisis Léxico y Validación de Patrones
"""

INFORMACIÓN_PROYECTO = {
    "nombre": "ProyectoTLF - Sistema de Análisis Léxico y Validación de Patrones",
    "curso": "Teoría de Lenguajes Formales",
    "universidad": "Universidad del Quindío",
    "año": "2025",
    "semestre": "8vo",
    "profesora": "Ana María Tamayo Ocampo",
    "estudiantes": [
        "Diego Alejandro Carvajal Camargo",
        "Nicolás Jurado Ramirez", 
        "Johan Noé Londoño Salazar"
    ]
}

EXPRESIONES_REGULARES = {
    "email": {
        "patron": r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        "descripcion": "Dirección de correo electrónico válida",
        "explicacion": "Inicia con caracteres alfanuméricos y algunos especiales, seguido de @, dominio y extensión de al menos 2 caracteres",
        "ejemplos_validos": ["usuario@ejemplo.com", "test.email@dominio.co"],
        "ejemplos_invalidos": ["email_sin_arroba.com", "@dominio.com"]
    },
    
    "telefono": {
        "patron": r'^(\+57|57)?[\s\-]?[3][0-9]{2}[\s\-]?[0-9]{3}[\s\-]?[0-9]{4}$',
        "descripcion": "Número telefónico colombiano",
        "explicacion": "Opcional código país (+57 o 57), debe iniciar con 3, seguido de 9 dígitos con separadores opcionales",
        "ejemplos_validos": ["3001234567", "+57 300 123 4567"],
        "ejemplos_invalidos": ["123456789", "2001234567"]
    },
    
    "fecha": {
        "patron": r'^(?:(?:0?[1-9]|[12][0-9]|3[01])[\/\-](?:0?[1-9]|1[012])[\/\-](?:19|20)\d{2}|(?:19|20)\d{2}[\/\-](?:0?[1-9]|1[012])[\/\-](?:0?[1-9]|[12][0-9]|3[01]))$',
        "descripcion": "Fecha en formato dd/mm/yyyy, dd-mm-yyyy o yyyy/mm/dd",
        "explicacion": "Acepta días 1-31, meses 1-12, años 1900-2099, con separadores / o -",
        "ejemplos_validos": ["25/12/2024", "2024/01/15"],
        "ejemplos_invalidos": ["32/12/2024", "25/13/2024"]
    },
    
    "cedula": {
        "patron": r'^[1-9][0-9]{7,9}$',
        "descripcion": "Cédula de ciudadanía colombiana (8-10 dígitos)",
        "explicacion": "Inicia with 1-9, seguido de 7-9 dígitos adicionales",
        "ejemplos_validos": ["12345678", "1234567890"],
        "ejemplos_invalidos": ["01234567", "1234567"]
    },
    
    "url": {
        "patron": r'^https?:\/\/(?:[-\w.])+(?:\:[0-9]+)?(?:\/(?:[\w\/_.])*(?:\?(?:[\w&=%.])*)?(?:\#(?:[\w.])*)?)?$',
        "descripcion": "URL válida con protocolo HTTP o HTTPS",
        "explicacion": "Inicia con http:// o https://, seguido de dominio válido, puerto opcional, ruta opcional",
        "ejemplos_validos": ["https://www.google.com", "http://localhost:8080"],
        "ejemplos_invalidos": ["www.google.com", "ftp://servidor.com"]
    }
}

ARQUITECTURA_SISTEMA = {
    "patron_arquitectonico": "MVC (Modelo-Vista-Controlador)",
    "componentes_principales": {
        "Model (TextModel)": "Gestiona datos y lógica de negocio del análisis léxico",
        "View (TextView)": "Maneja interacción con usuario y presentación de resultados", 
        "Controller (TextController)": "Coordina flujo entre modelo y vista"
    },
    "modulos_especializados": {
        "patterns.py": "Definición de expresiones regulares y validador de patrones",
        "lexical_analyzer.py": "Analizador léxico con tokenización y clasificación",
        "test_cases.py": "Casos de prueba y ejemplos organizados",
        "demo.py": "Sistema de demostración interactivo"
    }
}

CONCEPTOS_TEORICOS = {
    "logica_proposicional": "Evaluación binaria de patrones (válido/inválido)",
    "teoria_conjuntos": "Operaciones con alfabetos y lenguajes formales",
    "expresiones_regulares": "Notación algebraica para describir patrones de texto",
    "automatas_finitos": "Modelos matemáticos para reconocimiento de lenguajes regulares", 
    "analisis_lexico": "Proceso de tokenización y clasificación de elementos del texto"
}

FLUJO_PROCESAMIENTO = [
    "1. Entrada de texto por el usuario",
    "2. Tokenización mediante análisis léxico", 
    "3. Clasificación de tokens según patrones definidos",
    "4. Generación de estadísticas y reportes",
    "5. Presentación de resultados al usuario"
]

RESULTADOS_OBTENIDOS = {
    "patrones_implementados": 11,
    "tipos_token_soportados": ["VALID_PATTERN", "INVALID_TOKEN", "PUNCTUATION", "UNKNOWN"],
    "funcionalidades": [
        "Análisis léxico completo",
        "Validación de patrones específicos", 
        "Búsqueda de patrones en texto",
        "Generación de reportes detallados",
        "Interfaz interactiva con menú",
        "Casos de prueba exhaustivos"
    ],
    "metricas_rendimiento": {
        "precision_patrones": "Alta - patrones bien definidos",
        "manejo_errores": "Robusto - clasifica tokens inválidos",
        "casos_extremos": "Contemplados - texto vacío, solo puntuación, etc."
    }
}

INSTRUCCIONES_USO = {
    "aplicacion_principal": "python main.py",
    "demostracion": "python demo.py", 
    "casos_prueba": "python test_cases.py",
    "prueba_rapida": "python quick_test.py"
}

def mostrar_documentacion():
    """Muestra la documentación técnica completa"""
    print("="*80)
    print("DOCUMENTACIÓN TÉCNICA DEL PROYECTO")
    print("="*80)
    
    print(f"\n📋 INFORMACIÓN DEL PROYECTO:")
    for key, value in INFORMACIÓN_PROYECTO.items():
        if isinstance(value, list):
            print(f"  {key}: {', '.join(value)}")
        else:
            print(f"  {key}: {value}")
    
    print(f"\n🔍 EXPRESIONES REGULARES IMPLEMENTADAS:")
    for patron, info in EXPRESIONES_REGULARES.items():
        print(f"\n  📌 {patron.upper()}:")
        print(f"     Patrón: {info['patron']}")
        print(f"     Descripción: {info['descripcion']}")
        print(f"     Válidos: {info['ejemplos_validos']}")
    
    print(f"\n🏗️ ARQUITECTURA DEL SISTEMA:")
    print(f"  Patrón: {ARQUITECTURA_SISTEMA['patron_arquitectonico']}")
    print(f"  Componentes:")
    for comp, desc in ARQUITECTURA_SISTEMA['componentes_principales'].items():
        print(f"    • {comp}: {desc}")
    
    print(f"\n📚 CONCEPTOS TEÓRICOS APLICADOS:")
    for concepto, descripcion in CONCEPTOS_TEORICOS.items():
        print(f"  • {concepto}: {descripcion}")
    
    print(f"\n⚡ FLUJO DE PROCESAMIENTO:")
    for paso in FLUJO_PROCESAMIENTO:
        print(f"  {paso}")
    
    print(f"\n🎯 RESULTADOS OBTENIDOS:")
    print(f"  Patrones implementados: {RESULTADOS_OBTENIDOS['patrones_implementados']}")
    print(f"  Funcionalidades: {len(RESULTADOS_OBTENIDOS['funcionalidades'])}")
    for func in RESULTADOS_OBTENIDOS['funcionalidades']:
        print(f"    ✓ {func}")
    
    print(f"\n🚀 INSTRUCCIONES DE USO:")
    for comando, descripcion in INSTRUCCIONES_USO.items():
        print(f"  {comando}: {descripcion}")
    
    print("="*80)

if __name__ == "__main__":
    mostrar_documentacion()