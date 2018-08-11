from ckanapi import RemoteCKAN

secret = '99a4919a-310e-43c1-8f4b-175b946c816c'
data = "https://raw.githubusercontent.com/OpenDataSTL/pyckan/data_example/data_demo.csv"

class DataDemo:
    def __init__(self):
        self.name = 'demo_data'
        self.connect()
        self.delete()

    def connect(self):
        print("Setting up connection")
        self.conn = RemoteCKAN('http://beta.stlouisdata.org', apikey=secret)
        self.a = self.conn.action
        
    def delete(self):
        if self.name in self.a.package_list():
            self.a.package_delete(id=self.name)

    def create(self):
        print("Creating Package")
        self.pkg = self.a.package_create(
            name=self.name, title='Demo Data',
            notes="For use with the data_demo.py file")
        print(self.pkg)

        print("Adding Resource")
        self.res = self.a.resource_create(package_id=self.pkg['id'], url=data, name="Example Places")
        print(self.res)

    def find_data(self):
        # Not actually working, but this looks like what it should be
        print('searching for "arch":')
        result = self.a.datastore_search(resource_id=self.res, q={"place": "arch"})
        print(result)

if __name__ == "__main__":
    d = DataDemo()
    d.create()
    d.find_data()
