from abc import ABC, abstractclassmethod


class Importer(ABC):

    @abstractclassmethod
    def file_extension(path):
        raise NotImplementedError

    @abstractclassmethod
    def import_data(path):
        raise NotImplementedError
