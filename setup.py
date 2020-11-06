import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

with open('requirements.txt', 'r') as req:
    requirements = req.read().split('\n')

setuptools.setup(
    name='fylesdk',
    version='1.1.0',
    author='Siva Narayanan',
    author_email='siva@fyle.in',
    description='Python SDK for accessing Fyle Platform APIs',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['fyle', 'platform', 'api', 'python', 'sdk'],
    url='https://github.com/fylein/fyle-sdk-py',
    packages=setuptools.find_packages(),
    install_requires=[requirements],
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
