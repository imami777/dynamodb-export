from distutils.core import setup

setup(
    name='dynamodb-export',
    packages=['dynamodbexport', 'dynamodbexport.entrypoints'],
    version='1.0',
    description='A cli to export Amazon DynamoDb tables',
    keywords=['aws', 'dynamodb', 'export'],
    python_requires='>=3.6',
    install_requires=[
        'click==6.7',
        'boto3==1.7.19'
    ],
    entry_points={
        'console_scripts': [
            'dynamodb-export = dynamodbexport.__main__:main'
        ]
    }
)
