def func():
    print('printer.py -> func() -> __name__:', __name__)
    
print('printer.py -> not in function -> __name__:', __name__)
# if you run the script the above prints:
# This is not in function-> __name__: __main__

# if printer.py is imported in another script the above prints:
# printer.py -> not in function -> __name__: printer
# (printed once during the import)