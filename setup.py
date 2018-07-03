# coding=utf-8

from setuptools import setup

setup(
    name='mvpboss1004-datx',
    version='0.1',
    description=(
        '''基于IPIP进行拓展的数据查询接口。包括：
            1. IPIP.net的IP信息查询 https://www.ipip.net/product/ip.html
            2. IEEE公开的MAC信息查询 https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries
            3. 手机归属地查询 https://www.qqzeng-ip.com/
            4. 身份证信息解析（地级市代码，年份）'''
    ),
    author='mvpboss1004',
    author_email='mvpboss1004@126.com',
    maintainer='mvpboss1004',
    maintainer_email='mvpboss1004@126.com',
    license='Apache License Version 2.0',
    packages=['datx'],
    package_data={'datx': ['china_city_code.csv', 'mydata4vipday2.datx', 'phone-qqzeng.csv', 'oui36.csv', 'mam.csv', 'oui.csv']},
    platforms=['all'],
    install_requires=['pandas'],
    url='https://github.com/mvpboss1004/datx-python',
    classifiers=[
        'Development Status :: 1 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)