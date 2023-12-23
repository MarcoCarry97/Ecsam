import clingo
import sqlite3
import django
import pylatex
import pypdf

class test_maker:

    def __init__(self,num_of_exe=10,exe_list=[]):
        self.num_of_exe=num_of_exe
        self.exe_list=exe_list

    def generate(self,num_tests,couple_num_exe):
        models=[]
        file=open("logic_program.lp","r")
        program=file.read()
        args=["--model="+str(num_tests)]
        control=clingo.Control(arguments=args)
        control.add("base",[],program)
        control.ground([("base",[])])
        handle=control.solve(yield_=True)
        for model in handle:
            models+=[model]
        return models

