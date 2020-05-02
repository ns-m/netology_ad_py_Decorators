from datetime import datetime


def decorator(log_path):
    def decorator_log(function):
        def logging(*args, **kwargs):
            arg_string = str()
            data = datetime.today()
            ret = function(*args, **kwargs)
            function_name = function.__name__
            for arg in args:
                arg_string += f'{arg} '
            for name, value in kwargs.items():
                arg_string += f'{name}: {value}; '
            if not arg_string:
                func_string = f'Function "{function_name}" performed {data} without arguments and returned "{ret}"\n'
            else:
                func_string = f'Function "{function_name}" performed {data} with arguments {arg_string.rstrip()} and returned "{ret}"\n'

            with open(log_path, mode='a', encoding='utf-8') as file:
                file.write(func_string)

        return logging

    return decorator_log
