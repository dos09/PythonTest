def test_1():

    def greet(name):
        return "hello {0}!".format(name)

    def p_decorate(func):
        def func_wrapper(name):
            return "<p>{0}</p>".format(func(name))
        return func_wrapper

    my_get_text = p_decorate(greet)

    print(my_get_text("John"))


def test_single_decorator():

    def p_decorate(func):
        def func_wrapper(*args, **kwargs):
            return "<p>{0}</p>".format(func(*args, **kwargs))
        return func_wrapper

    @p_decorate
    def greet(name):
        return "hello {0}!".format(name)

    print(greet("Asen"))


def test_several_decorators():

    def p_decorate(func):
        def func_wrapper(name):
            return "<p>{0}</p>".format(func(name))
        return func_wrapper

    def strong_decorate(func):
        def func_wrapper(name):
            return "<strong>{0}</strong>".format(func(name))
        return func_wrapper

    def div_decorate(func):
        def func_wrapper(name):
            return "<div>{0}</div>".format(func(name))
        return func_wrapper

    @div_decorate
    @p_decorate
    @strong_decorate
    def greet(name):
        return "Hello {0}".format(name)

    print(greet("not Asen"))

    # One important thing to notice here is that the order of
    # setting our decorators matters. If the order was different in the
    # example above, the output would have been different.


def test_decorator_parameters():

    def tags(tag_name):
        def tags_decorator(func):
            def func_wrapper(name):
                return "<{0}>{1}</{0}>".format(tag_name, func(name))
            return func_wrapper
        return tags_decorator

    @tags("p")
    def greet(name):
        return 'Hello {0}'.format(name)

    print(greet("Minka"))

if __name__ == '__main__':
    pass
    test_single_decorator()
    test_several_decorators()
    test_decorator_parameters()
    test_1()
