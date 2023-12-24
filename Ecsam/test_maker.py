import clingo
import sqlite3
import django
import pylatex
import pypdf

def to_asp_format(model):
    string=""
    string=".".join(str(symbol) for symbol in model.split(" "))
    if(string!=""):
        string+="."
    return string

class test_maker:

    def __init__(self):
        pass

    def generate(self,num_tests=1,couple_num_exe={}):
        tot_exe=0
        for key in couple_num_exe.keys():
            tot_exe+=couple_num_exe[key]
        model=""
        for key in couple_num_exe.keys():

            num_exe_per_test=couple_num_exe[key]

            file = open("logic_program.lp", "r")
            program = model+"\n"+file.read()
            args = ["--model=" + str(num_tests),
                    "-c num_exe=" + str(num_exe_per_test),
                    "-c tot_exe=" + str(tot_exe),
                    "-c type="+key,
                    ]
            control = clingo.Control(arguments=args)
            control.add("base", [], program)
            control.ground([("base", [])])
            handle = control.solve(yield_=True)
            for submodel in handle:
                model = to_asp_format(str(submodel))
        return model
