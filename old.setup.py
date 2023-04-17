from setuptools import setup, find_packages

setup(
    name="my_functions",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Здесь можно указать зависимости вашего пакета
    ],
)


# После добавления файла setup.py в корень вашего репозитория, 
# убедитесь, что вы его закоммитили и запушили в ваш репозиторий на GitHub.
# !pip install git+https://github.com/dnp34/my_functions.git
