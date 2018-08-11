

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
        pkg = demo.action.package_create(name='ya_set', title='not going to work')
    except:
        print("create_error")

    pkg = demo.action.package_show(id='ya_set')

    groups = demo.action.package_list(id='test_data')
    print(groups)
    print("\nPackage_Create {}".format(pkg))

    pkg['title'] = "WORKING!!"
    #pkg['tags'] = ['a_tag', 'b_tag']
    pkg['notes'] = 'Just playing around really...' # this is the description field

    #print("\nPackage_Create {}".format(pkg))

    pkg = demo.action.package_update(**pkg)
    #print("\nPackage_Create {}".format(pkg))

    npkg = demo.action.package_show(id='test_data')
    print("\nPackage_Create {}".format(npkg))

    pkg['resources'] = npkg['resources']
    pkg = demo.action.package_update(**pkg)



    #pkg = demo.action.resource_update(package_id='my-dataset3', name='test-data', id='ec2191c7-fd13-44c6-a51f-71c1081330df', url='https://raw.githubusercontent.com/OpenDataSTL/pyckan/Clarys-Branch/testdata.csv', upload='true')

    #res = demo.action.resource_show(package_id='my-dataset3', name='test-data',  id='ec2191c7-fd13-44c6-a51f-71c1081330df')

if __name__ == "__main__":
    run()
