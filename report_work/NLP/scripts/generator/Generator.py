from abc import ABC,abstractmethod
import random

class Generator(ABC):
    def __init__(self,input_file_path:str,output_file_path:str,seed:int = 1111) -> None:
      super().__init__()
      self.input_file_path = input_file_path
      self.output_file_path = output_file_path
      self.random = random.seed(seed)
      self.pattern = r":(\d+)" 
   
    @abstractmethod
    def done(self,) -> None:
        """"""
        pass

    def read_file(self, option: str = "r") -> list:
        with open(self.input_file_path, option) as r:
            text = r.readlines()
            
        return text
    
    def write_file(self,option:str="w",text:str="") -> None:
        with open(self.output_file_path,option) as w:
            w.write(text)