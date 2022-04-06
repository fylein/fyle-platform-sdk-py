import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='fyle',
    version='v0.23.0',
    author='Siva Narayanan',
    author_email='siva@fyle.in',
    description='Python SDK for accessing Fyle Platform APIs',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['fyle', 'api', 'python', 'sdk'],
    url='https://github.com/fylein/fyle-platform-sdk-py',
    packages=setuptools.find_packages(),
    install_requires=[
        'enum34==1.1.10',
        'requests>=2.25.0'
    ],
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
