from Replacer import Replacer

if __name__ == "__main__":
    from_path = "/home/RoboSys/Numerical-Analysis/report_work/NLP/DataSet/from/bible.txt"
    to_path = "/home/RoboSys/Numerical-Analysis/report_work/NLP/DataSet/to/bible.txt"
    
    replacer = Replacer(from_path,to_path)
    
    replacer.done()