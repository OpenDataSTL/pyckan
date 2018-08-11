

import requests
from ckanapi import RemoteCKAN

secret = '99a4919a-310e-43c1-8f4b-175b946c816c'

def run():
    print("OpenSTL-DataExchange")

    ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

    demo = RemoteCKAN('http://beta.stlouisdata.org', apikey=secret)

    packages = demo.action.package_list()
    print(packages)

if __name__ == "__main__":
    run()
