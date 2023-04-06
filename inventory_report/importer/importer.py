from abc import ABC, abstractmethod


class Importer(ABC):

    @abstractmethod
    def file_extension(path):
        raise NotImplementedError

    @abstractmethod
    def import_data(path):
        raise NotImplementedError
