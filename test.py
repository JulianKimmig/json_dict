import os
import tempfile
import unittest

import json_dict

from json_dict import JsonDict, JsonSubDict
json_dict.VERBOSE=True

class DictTest(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.temp_file= os.path.join(self.temp_dir,"d")
        with open(self.temp_file,"wb+") as f:
            f.write(b'{"test":"file"}')
        with open(self.temp_file,"r") as f:
            print(f.read(),self.temp_file)
        self.d = JsonDict(self.temp_file, backup=False)

    def tearDown(self):
        os.remove(self.temp_file)
        os.rmdir(self.temp_dir)

    def test_create_dict(self):
        assert list(self.d.data.keys())==["test"]
        assert self.d.get("test") == "file"

    def test_result_is_dict_to_json_dict(self):
        self.d.put("test",value={})
        assert isinstance(self.d.get("test"), JsonSubDict)

    def test_create_subdict(self):
        print("A")
        print(self.d._file_size)
        sub1 = self.d.getsubdict("testsub","dict")
        print("B")
        sub2 = self.d.getsubdict(["testsub","dict"])
        assert len(self.d.data.keys())==2
        assert len(self.d["testsub"].keys())==1

    def test_data_is_dict(self):
        sd = self.d.getsubdict("testsub","dict")
        assert isinstance(self.d.data,dict)
        assert isinstance(sd.data,dict),(type(sd.data),sd.data)

    def test_double_open_file(self):
        d2=JsonDict(self.d.file,backup=False)
        d2.put("second_entry",value=1)
        print(self.d)
        print(d2)



if __name__ == '__main__':
    unittest.main()