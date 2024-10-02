def override(method):
    """
    A custom decorator to indicate that a method is overriding a method in the parent class.
    """

    def wrapper(*args, **kwargs):
        return method(*args, **kwargs)

    return wrapper
