
from data_analyzer.Analyzer import Analyzer
import re


class Counter(Analyzer):
  def __init__(self, input_file_path: str, output_file_path: str,correct_pattern:str = r'^[a-z0-9\n]+$') -> None:
    super().__init__(input_file_path, output_file_path)
    pattern = re.compile(correct_pattern)
    matching_chars = [chr(i) for i in range(32, 127) if pattern.match(chr(i))] + ['\n']
    self.nums = {char:0 for char in matching_chars}
    
  def done(self) -> None:
    text = self.read_file("r")
    for line in text:
      for char in line:
        for key in self.nums.keys():
          if char == key:
            self.nums[key] += 1
            continue
    
    with open(self.output_file_path,"w") as w:
      pass
    
    for key,value in self.nums.items():
      self.write_file("a",f"{key}:{value}\n")
      
if __name__ == "__main__":
  from_path = "/home/RoboSys/Numerical-Analysis/report_work/NLP/DataSet/test/replace_to.txt"
  to_path = "/home/RoboSys/Numerical-Analysis/report_work/NLP/scripts/data_analyzer/log/test.txt"
  
  counter = Counter(from_path,to_path)
  counter.done()