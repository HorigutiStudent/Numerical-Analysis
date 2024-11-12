from abc import ABC,abstractmethod

class Handler(ABC):
    def __init__(self,input_file_path:str,output_file_path:str):
        super().__init__()
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    @abstractmethod
    def done(self,) -> None:
        """"""
        pass

    def read_file(self,option:str= "r") -> str:
        with open(self.input_file_path,option) as r:
            text = r.read()

        return text
    
    def write_file(self,option:str="w",text:str="") -> None:
        with open(self.output_file_path,option) as w:
            w.write(text)