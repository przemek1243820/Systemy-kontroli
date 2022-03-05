import pickle

class SaveLoad:
    @staticmethod
    def write(filename,data):
        file=open(filename,"wb")
        pickle.dump(data,file)
        file.close()

    @staticmethod
    def read(filename):
        return pickle.load(open(filename,"rb"))