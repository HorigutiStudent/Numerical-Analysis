from data_analyzer.Counter import Counter
from data_handler.Replacer import Replacer
from generator.Malcof import Malcof

import time

if __name__ == "__main__":
  #現在のファイルでは、英語で書かれた聖書を参照していますが、別言語のファイルがあれば、それを読み込ませることもできます。ただし、文字が異なる場合には、正規表現も修正してください
  replacer_input_file = "/home/RoboSys/Numerical-Analysis/report_work/NLP/DataSet/replacer/from/bible.txt"
  replacer_output_file = "/home/RoboSys/Numerical-Analysis/report_work/NLP/DataSet/replacer/to/bible.txt"
  counter_output_file = "/home/RoboSys/Numerical-Analysis/report_work/NLP/DataSet/analyzer/counter.txt"
  malcof_output_file = "/home/RoboSys/Numerical-Analysis/report_work/NLP/DataSet/generator/0_malcof_2.txt"
  #正規表現を変え、どの文字を取得するかを変えれば、別言語も生成できます。
  pattern = r"^[a-z0-9\n]+$"
  replacer = Replacer(replacer_input_file,replacer_output_file,pattern)
  counter = Counter(replacer_output_file,counter_output_file,pattern)
  #シードを固定することで、出力を比べることができます
  #今回は簡便法を使うのでシードをランダムに設定しています
  malcof = Malcof(counter_output_file,malcof_output_file,100,seed=int(time.time()))
  
  #出現頻度まで終わっているなら(counter.done()が完了しているなら)malcof.doneのみを実行すればよいです。
  replacer.done()
  counter.done()
  malcof.done()
  