import datetime
import functools
import inspect
import os
from colorama import Fore
from datetime import datetime
import time

from main import DIR

def case(text):
    '''
    打印用例信息并输出对应的日志
    :param text: str 控制台要输出的内容或要打印的日志文本数据
    :return:
    '''
    format_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]
    stack = inspect.stack()
    code_path = f'{os.path.basename(stack[1].filename)} : {stack[1].lineno}'
    content = f'【CASE】{format_time} - {code_path} >> {text}'
    print(f'{Fore.LIGHTBLUE_EX} {content}')
    str_time = datetime.now().strftime("%Y%m%d")
    LOG_DIR = os.path.join(DIR, 'logs')
    os.makedirs(LOG_DIR, exist_ok=True)
    log_file = os.path.join(LOG_DIR, f'{str_time}_info.log')
    with open(file=log_file, mode='a', encoding='utf-8') as f:
        f.write(content + '\n')


def info(text):
    '''
    打印用例运行时数据并输出对应的日志
    :param text: str 控制台要输出的内容或要打印的日志文本数据
    :return:
    '''
    format_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]
    stack = inspect.stack()
    code_path = f'{os.path.basename(stack[1].filename)} : {stack[1].lineno}'
    content = f'【INFO】{format_time} - {code_path} >> {text}'
    print(f'{Fore.LIGHTYELLOW_EX} | {content}')
    str_time = datetime.now().strftime("%Y%m%d")
    LOG_DIR = os.path.join(DIR, 'logs')
    os.makedirs(LOG_DIR, exist_ok=True)
    log_file = os.path.join(LOG_DIR, f'{str_time}_info.log')
    with open(file=log_file, mode='a', encoding='utf-8') as f:
        f.write(content + '\n')

def error(text):
    '''
    打印用例断言失败信息或异常信息并输出对应的日志
    :param text: str 控制台要输出的内容或要打印的日志文本数据
    :return:
    '''
    format_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]
    stack = inspect.stack()
    code_path = f'{os.path.basename(stack[1].filename)} : {stack[1].lineno}'
    content = f'【ERROR】{format_time} - {code_path} >> {text}'
    print(f'{Fore.LIGHTRED_EX} | {content}')
    str_time = datetime.now().strftime("%Y%m%d")
    LOG_DIR = os.path.join(DIR, 'logs')
    os.makedirs(LOG_DIR, exist_ok=True)
    log_file_info = os.path.join(LOG_DIR, f'{str_time}_info.log')
    log_file_error = os.path.join(LOG_DIR, f'{str_time}_error.log')
    with open(file=log_file_info, mode='a', encoding='utf-8') as f:
        f.write(content + '\n')
    with open(file=log_file_error, mode='a', encoding='utf-8') as f:
        f.write(content + '\n')

# if __name__ == '__main__':
#     case('fff')
#     info("infoXXXXX")
#     error("出现问题了！！！")
def case_decorate(func):
    @functools.wraps(func)
    def wraper(*args,**kwargs):
        start = time.time()
        case('==='*30)
        class_name = args[0].__class__.__name__
        method_name = func.__name__
        doc =inspect.getdoc(func)
        case(f'Method Name:{method_name},Class Name:{class_name}')
        case(f'Test Description:{doc}')
        func(*args,**kwargs)
        end =time.time()
        duration = end-start
        case(f'Case run time:%.2fs'%duration)
    return wraper

def class_case_decoration(cls):
    for name ,method in inspect.getmembers(cls,inspect.isfunction):
        if name.startswith("testCase"):
            setattr(cls,name,case_decorate(method))
    return cls








