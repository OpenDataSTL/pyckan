

import requests
from ckanapi import RemoteCKAN

secret = '99a4919a-310e-43c1-8f4b-175b946c816c'

def run():
    print("OpenSTL-DataExchange")

    ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

    demo = RemoteCKAN('http://beta.stlouisdata.org', apikey=secret)

    groups = demo.action.package_list(id='test_data')
    print(groups)

    try:
        pkg = demo.action.package_create(name='my-dataset', title='not going to work')
    except:
        print("create_error")

    pkg = demo.action.package_show(id='my-dataset')

    groups = demo.action.package_list(id='test_data')
    print(groups)
    print("\nPackage_Create {}".format(pkg))

    pkg['title'] = "WORKING!!"
    pkg['tags'] = ['a_tag', 'b_tag']
    pkg['description'] = 'Just playing around really...'

    print("\nPackage_Create {}".format(pkg))

    pkg = demo.action.package_patch(id='my-dataset',  data_dict=pkg)

if __name__ == "__main__":
    run()
