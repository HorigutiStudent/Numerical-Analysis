from data_handler.Handler import Handler

import re

class Replacer(Handler):
  def __init__(
    self,
    input_file_path: str, 
    output_file_path: str,
    correct_pattern:str = r'^[a-z0-9\n]+$'
  ):
    super().__init__(input_file_path, output_file_path)
    self.pattern = re.compile(correct_pattern)
    
  def done(self) -> None:
    texts = self.read_file("r")
    for line in texts:
      for char in line:
        tex = char.lower()
        if self.pattern.match(tex):
          self.write_file(option="a",text=tex)
        else:
          self.write_file(option="a",text=" ")
          
          
if __name__ == "__main__":
  from_path = "/home/RoboSys/Numerical-Analysis/report_work/NLP/DataSet/test/replace_from.txt"
  to_path = "/home/RoboSys/Numerical-Analysis/report_work/NLP/DataSet/test/replace_to.txt"
  replacer = Replacer(from_path,to_path)
  
  replacer.done()