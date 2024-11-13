import sys
sys.path.append("/home/RoboSys/Numerical-Analysis/report_work/NLP/scripts/")
from generator.Generator import Generator
import re
import random

class Malcof(Generator):
  def __init__(
    self, 
    input_file_path: str,
    output_file_path: str, 
    num_characters:int = 100,
    pattern:str = r"([^:]+):(\d+)",
    seed: int = 1111,
    n_fold:int = 0,
  ) -> None:
    super().__init__(input_file_path, output_file_path, seed)
    self.pattern = pattern
    self.data_dict = {}
    self.num_characters = num_characters

    
  def done(self) -> None:
    frequency = self.read_file("r")
    self.__create_frequency_dict(frequency)
    total = self.__sum_frequency()
    self.write_file("w")
    for _ in range(self.num_characters):
      rand = random.randint(0,total-1)
      accumulation = 0
      j = 0
      for j,val in enumerate(self.data_dict.values()):
        #print(self.data_dict.values())
        #accumulation += self.data_dict.values()[j]
        accumulation += val
        #print(rand,accumulation)
        print(j)
        if rand < accumulation:
          if j < 26:
            self.write_file("a",chr(ord('a') + j))
          else:
            self.write_file("a"," ")
          break
  
  
  def __create_frequency_dict(self,text:str) -> None:
    for line in text:
      match = re.match(self.pattern,line.strip())
      if match:
        key,value = match.groups()
        self.data_dict[key] = int(value)
        
        
  def __sum_frequency(self) -> int:
    total = 0
    for val in self.data_dict.values():
      total += val
    return total
  
if __name__ == "__main__":
  
  input_file = "/home/RoboSys/Numerical-Analysis/report_work/NLP/scripts/data_analyzer/log/test.txt"
  output_file = "/home/RoboSys/Numerical-Analysis/report_work/NLP/scripts/generator/generated/test.txt"
  
  malcof = Malcof(input_file,output_file)
  
  malcof.done()