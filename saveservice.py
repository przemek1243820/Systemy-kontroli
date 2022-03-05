import stat
from serialization import SaveLoad

class SaveService:

    @staticmethod
    def save(filename,data):
        if(type(data) is str):
            file=open(filename,"w")
            file.write(data)
            file.close()
        else:
            SaveLoad.write(filename,data)

        print("data saved")

    @staticmethod
    def deserialize(filename):
        return SaveLoad.read(filename)