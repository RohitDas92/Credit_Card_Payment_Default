import setuptools

with open('README.md', 'r',encoding='utf-8') as f:
    long_discreption = f.read()

__version__ = '0.0.1'

REPO_NAME = 'CREDIT_CARD_PAYMENT_DEFAULT'
AUTHOR_USER_NAME = 'RohitDas92'
SRC_REPO = 'credit_card_payment_default'
AUTHOR_EMAIL = 'rhtdas1992@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A python package which analyses last 5 months payments made for credit card and predict if customer will default in the next month.',
    long_description=long_discreption,
    long_discreption_content = 'text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls = {
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)