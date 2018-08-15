

import requests
from ckanapi import RemoteCKAN


#secret = API Key
secret = ''
demo = RemoteCKAN('http://beta.stlouisdata.org', apikey=secret)


#Create as many resources as desired
def update_resources():
    filename = " "

    #While the name input is NOT blank
    while filename != "":
        #Name displayed in big letters and on resource list
        filename = input("Enter the name of a resource to to add to a dataset.  Leave blank to finish with resources\n"
                         "'exit' to exit\n")
        if filename == "":
            break
        elif filename == "exit":
            exit()

        #Choose where the resource goes
        dataset = input("Enter the name of the existing dataset to add the file to\n")

        #Enter a description for the resource
        desc = input("Enter a description for the resource\n")

        #URL of the initial values to input into the file
        res_url = input("Enter the url for the source file\n")

        #Create resource with all of those variables
        package = demo.action.resource_create(package_id=dataset,
                                              name=filename,
                                              url=res_url,
                                              notes=desc)

        #Verify in the logs that it worked by seeing what values are in what places
        print(package)

    run()


def update_datasets():
    filename = " "

    #While the name input is NOT blank
    while filename != "":
        #Name displayed in big letters and URL
        filename = input("Enter the name of a dataset to create.  \n"
                         "Will be converted to Lowercase.  Leave blank to finish with datasets\n"
                         "'exit' to exit\n").lower()
        if filename == "":
            break
        elif filename == "exit":
            exit()

        #Enter a description for the dataset
        desc = input("Enter a description for the dataset\n")

        #Create resource with all of those variables
        package = demo.action.package_create(name=filename,
                                              notes=desc)

        #Verify in the logs that it worked by seeing what values are in what places
        print(package)
    run()

def run():
    print("OpenSTL-DataExchange")

    usr_in = input("Do you wish to create 'datasets' or 'resources'?  Leave blank to exit\n")

    #Decide if user wants to make new Datasets or Resources
    if usr_in == "datasets":
        update_datasets()
    elif usr_in == "resources":
        update_resources()
    update_resources()

    ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

    demo = RemoteCKAN('http://beta.stlouisdata.org', apikey=secret)

    groups = demo.action.package_list(id='test_data')
    print(groups)

    # try:
    #     pkg = demo.action.package_create(name='ya_set', title='not going to work')
    # except:
    #     print("create_error")

    pkg = demo.action.package_show(id='ya_set')

    groups = demo.action.package_list(id='test_data')
    print(groups)
    print("\nPackage_Create {}".format(pkg))

    pkg['title'] = "WORKING!!"
    #pkg['tags'] = ['a_tag', 'b_tag']
    pkg['notes'] = 'Just playing around really...' # this is the description field

    #print("\nPackage_Create {}".format(pkg))

    #pkg = demo.action.package_update(**pkg)
    #print("\nPackage_Create {}".format(pkg))

    npkg = demo.action.package_show(id='test_data')
    print("\nPackage_Create {}".format(npkg))

    # pkg['resources'] = npkg['resources']
    # pkg = demo.action.package_update(**pkg)

''' ToDo:
- parse_sources: 'sources dictionary" -> {source_name: source_url, data_set, group, org}
- for_each source in sources -> create/update/patch

'''




    #pkg = demo.action.resource_update(package_id='my-dataset3', name='test-data', id='ec2191c7-fd13-44c6-a51f-71c1081330df', url='https://raw.githubusercontent.com/OpenDataSTL/pyckan/Clarys-Branch/testdata.csv', upload='true')

    #res = demo.action.resource_show(package_id='my-dataset3', name='test-data',  id='ec2191c7-fd13-44c6-a51f-71c1081330df')

if __name__ == "__main__":
    run()
