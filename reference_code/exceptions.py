# Exceptions
############

def some_function():
    try:
        # Division by zero raises an exception
        10 / 0
    except ZeroDivisionError as e:
        print("Oops, invalid.")
        print(e)
    else:
        # Exception didn't occur, we're good.
        print('No exception occurred')
    finally:
        # This is executed after the code block is run
        # and all exceptions have been handled, even
        # if a new exception is raised while handling.
        print("We're done with that.")

some_function()