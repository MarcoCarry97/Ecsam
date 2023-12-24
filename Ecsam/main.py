from test_maker import test_maker

def main():
    maker=test_maker()
    dict={"open" : 5, "multiple" : 5}
    models=maker.generate(1,dict)
    print(models)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
