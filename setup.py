from setuptools import setup

setup(
    name='yolodeck',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=['pillow', 'streamdeck'],
    packages=['yolodeck'],
    url='',
    license='',
    author='Luiz Amaral',
    author_email='',
    description='',
    entry_points={
        'console_scripts': [
            'yolodeck=yolodeck.main:main',
        ],
    },
)
