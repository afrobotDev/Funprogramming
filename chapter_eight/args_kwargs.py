def args_logger(*args, **kwargs):
    for i, value in enumerate(args, start=1):
        print(f'{i}. {value}')
    
    sorted_key = sorted(kwargs.keys())
    for key in sorted_key:
        print(f'* {key} : {kwargs[key]}')

