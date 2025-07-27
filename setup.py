from setuptools import setup, find_packages

setup(
    name="tienda",      # Cambia por el nombre de tu paquete
    version="1.0.0",                # Versión inicial
    author="NEC",             # Opcional: tu nombre o el de tu equipo
    author_email="arenitamar7632@gmail.com",  # Opcional: tu email
    description="venta de productos o servicios",  # Descripción breve
    long_description="Larga descripción de lo que hace el paquete.",
    long_description_content_type="text/markdown",  # Tipo de contenido de la descripción larga
    url="https://github.com/MSE-256/store",  # URL de tu repositorio (si corresponde)
    packages=find_packages(),       # Esto buscará todos los paquetes dentro del directorio
    install_requires=[              # Lista de dependencias necesarias para el paquete
        "django",
        "pip",
    ],
    classifiers=[                   # Clasificadores (opcional)
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',         # Versión mínima de Python
)
