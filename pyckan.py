

import requests
from ckanapi import RemoteCKAN

secret = '99a4919a-310e-43c1-8f4b-175b946c816c'

def run():
    print("OpenSTL-DataExchange")

    ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

    demo = RemoteCKAN('http://beta.stlouisdata.org', apikey=secret)

    groups = demo.action.package_list(id='test_data')
    print(groups)

    pkg = demo.action.package_create(name='my-dataset', title='not going to work')
    groups = demo.action.package_list(id='test_data')
    print(groups)

if __name__ == "__main__":
    run()
