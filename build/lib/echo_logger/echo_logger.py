#!/usr/bin/env python
import functools
import json
import os
import socket
import time
import warnings
from pathlib import Path
from typing import Callable, Any, Dict, Union

import requests

# noinspection DuplicatedCode
echo_logger_debug = True


# noinspection PyPep8Naming
class _colors:
    def __init__(self):
        pass

    RESET = "\033[0m"  # Text Reset

    # Regular Colors
    BLACK = "\033[0;30m"  # BLACK
    RED = "\033[0;31m"  # RED
    GREEN = "\033[0;32m"  # GREEN
    YELLOW = "\033[0;33m"  # YELLOW
    BLUE = "\033[0;34m"  # BLUE
    PURPLE = "\033[0;35m"  # PURPLE
    CYAN = "\033[0;36m"  # CYAN
    WHITE = "\033[0;37m"  # WHITE

    # Bold
    BLACK_BOLD = "\033[1;30m"  # BLACK
    RED_BOLD = "\033[1;31m"  # RED
    GREEN_BOLD = "\033[1;32m"  # GREEN
    YELLOW_BOLD = "\033[1;33m"  # YELLOW
    BLUE_BOLD = "\033[1;34m"  # BLUE
    PURPLE_BOLD = "\033[1;35m"  # PURPLE
    CYAN_BOLD = "\033[1;36m"  # CYAN
    WHITE_BOLD = "\033[1;37m"  # WHITE

    # Underline
    BLACK_UNDERLINED = "\033[4;30m"  # BLACK
    RED_UNDERLINED = "\033[4;31m"  # RED
    GREEN_UNDERLINED = "\033[4;32m"  # GREEN
    YELLOW_UNDERLINED = "\033[4;33m"  # YELLOW
    BLUE_UNDERLINED = "\033[4;34m"  # BLUE
    PURPLE_UNDERLINED = "\033[4;35m"  # PURPLE
    CYAN_UNDERLINED = "\033[4;36m"  # CYAN
    WHITE_UNDERLINED = "\033[4;37m"  # WHITE

    # Background
    BLACK_BACKGROUND = "\033[40m"  # BLACK
    RED_BACKGROUND = "\033[41m"  # RED
    GREEN_BACKGROUND = "\033[42m"  # GREEN
    YELLOW_BACKGROUND = "\033[43m"  # YELLOW
    BLUE_BACKGROUND = "\033[44m"  # BLUE
    PURPLE_BACKGROUND = "\033[45m"  # PURPLE
    CYAN_BACKGROUND = "\033[46m"  # CYAN
    WHITE_BACKGROUND = "\033[47m"  # WHITE

    # High Intensity
    BLACK_BRIGHT = "\033[0;90m"  # BLACK
    RED_BRIGHT = "\033[0;91m"  # RED
    GREEN_BRIGHT = "\033[0;92m"  # GREEN
    YELLOW_BRIGHT = "\033[0;93m"  # YELLOW
    BLUE_BRIGHT = "\033[0;94m"  # BLUE
    PURPLE_BRIGHT = "\033[0;95m"  # PURPLE
    CYAN_BRIGHT = "\033[0;96m"  # CYAN
    WHITE_BRIGHT = "\033[0;97m"  # WHITE

    # Bold High Intensity
    BLACK_BOLD_BRIGHT = "\033[1;90m"  # BLACK
    RED_BOLD_BRIGHT = "\033[1;91m"  # RED
    GREEN_BOLD_BRIGHT = "\033[1;92m"  # GREEN
    YELLOW_BOLD_BRIGHT = "\033[1;93m"  # YELLOW
    BLUE_BOLD_BRIGHT = "\033[1;94m"  # BLUE
    PURPLE_BOLD_BRIGHT = "\033[1;95m"  # PURPLE
    CYAN_BOLD_BRIGHT = "\033[1;96m"  # CYAN
    WHITE_BOLD_BRIGHT = "\033[1;97m"  # WHITE

    # High Intensity backgrounds
    BLACK_BACKGROUND_BRIGHT = "\033[0;100m"  # BLACK
    RED_BACKGROUND_BRIGHT = "\033[0;101m"  # RED
    GREEN_BACKGROUND_BRIGHT = "\033[0;102m"  # GREEN
    YELLOW_BACKGROUND_BRIGHT = "\033[0;103m"  # YELLOW
    BLUE_BACKGROUND_BRIGHT = "\033[0;104m"  # BLUE
    PURPLE_BACKGROUND_BRIGHT = "\033[0;105m"  # PURPLE
    CYAN_BACKGROUND_BRIGHT = "\033[0;106m"  # CYAN
    WHITE_BACKGROUND_BRIGHT = "\033[0;107m"  # WHITE


def print_info(*args, **kwargs):
    if not echo_logger_debug:
        return
    # print with green color: [INFO]
    with_time = kwargs.pop('with_time', True)
    if not with_time:
        pre_print_str = _colors.GREEN_BOLD + '[INFO]' + _colors.RESET
    else:
        pre_print_str = _colors.GREEN_BOLD + '[INFO ' + time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + _colors.RESET
    print(pre_print_str, *args, **kwargs)


def print_err(*args, **kwargs):
    if not echo_logger_debug:
        return
    # print with red color: [ERROR]
    with_time = kwargs.pop('with_time', True)
    if not with_time:
        pre_print_str = _colors.RED_BOLD + '[ERR ]' + _colors.RESET
    else:
        pre_print_str = _colors.RED_BOLD + '[ERR  ' + time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + _colors.RESET
    print(pre_print_str, *args, **kwargs)


def print_debug(*args, **kwargs):
    if not echo_logger_debug:
        return
    # print with blue color: [DBUG]
    with_time = kwargs.pop('with_time', True)
    if not with_time:
        pre_print_str = _colors.BLUE_BOLD + '[DBUG]' + _colors.RESET
    else:
        pre_print_str = _colors.BLUE_BOLD + '[DBUG ' + time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + _colors.RESET
    print(pre_print_str, *args, **kwargs)


def print_warn(*args, **kwargs):
    if not echo_logger_debug:
        return
    # print with yellow color: [WARNING]
    with_time = kwargs.pop('with_time', True)
    if not with_time:
        pre_print_str = _colors.YELLOW_BOLD + '[WARN]' + _colors.RESET
    else:
        pre_print_str = _colors.YELLOW_BOLD + '[WARN ' + time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + _colors.RESET
    print(pre_print_str, *args, **kwargs)


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)  # reset filter
        return func(*args, **kwargs)

    return new_func


def calc_time(time_start, time_end):
    """This is a function which can be used to calculate
    the time between two time points. It will return the
    time in format xx:xx:xx.xx"""

    total_time_seconds = time_end - time_start
    hours, rem = divmod(total_time_seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    # time_str = "{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds)
    # print seconds reserving 4 digits
    if total_time_seconds < 60:
        time_str = "{:05.4f} seconds".format(seconds)
    elif total_time_seconds < 3600:
        time_str = "{:0>2} minutes {:05.4f} seconds".format(int(minutes), seconds)
    else:
        time_str = "{:0>2} hours {:0>2} minutes {:05.4f} seconds".format(int(hours), int(minutes), seconds)
    return time_str


def profile(func):
    """This is a decorator which can be used to test and record
    the time of a function. It will print the time of the function
    when the function is used."""

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        # print with xx.xxxx seconds
        time_str = calc_time(time_start, time_end)
        print_debug(f"Function {func.__name__}() costs {time_str}.", with_time=True)
        return result

    return new_func


# decorator print an object like json
def print_json(func):
    """Decorator for function, print the returned object like json"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        returned = func(*args, **kwargs)
        print_info(dumps_json(returned))
        return returned

    return wrapper


def try_catch(func):
    """Decorator for function, try catch the function
       This decorator is used to avoid the program to be terminated by exception.
       If multiple decorators are used, this decorator should be the outermost one.
       Because this decorator will catch all exceptions, and the other decorators may not work.
    """

    def wrapper(*args, **kwargs):
        try:
            returned = func(*args, **kwargs)
            return returned
        except Exception as e:
            print_err(e)
            return None

    return wrapper


def dumps_json(data, indent=2, depth=2):
    assert depth > 0
    space = ' ' * indent
    s = json.dumps(data, indent=indent, default=lambda o: '<not serializable>')
    lines = s.splitlines()
    _N = len(lines)
    # determine which lines to be shortened
    is_over_depth_line: Callable[[Any], bool] = lambda i: i in range(_N) and lines[i].startswith(space * (depth + 1))
    is_open_bracket_line: Callable[[Any], bool] = lambda i: not is_over_depth_line(i) and is_over_depth_line(i + 1)
    is_close_bracket_line: Callable[[Any], bool] = lambda i: not is_over_depth_line(i) and is_over_depth_line(i - 1)

    #
    def shorten_line(line_index):
        if not is_open_bracket_line(line_index):
            return lines[line_index]
        # shorten over-depth lines
        start = line_index
        end = start
        while not is_close_bracket_line(end):
            end += 1
        has_trailing_comma = lines[end][-1] == ','
        _lines = [lines[start][-1], *lines[start + 1:end], lines[end].replace(',', '')]
        d = json.dumps(json.loads(' '.join(_lines)))
        return lines[line_index][:-1] + d + (',' if has_trailing_comma else '')

    #
    s = '\n'.join([
        shorten_line(i)
        for i in range(_N) if not is_over_depth_line(i) and not is_close_bracket_line(i)
    ])
    #
    return s


def save_json(path_: str = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            json_str = dumps_json(result)
            with open(path_, 'w') as f:
                f.write(json_str)
            return func(*args, **kwargs)

        return wrapper

    return decorator


class ColorString:
    def __init__(self):
        pass

    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    end = '\033[0m'
    none = ''  # no color, placeholder

    @staticmethod
    def coloring(string: str, color: str = red) -> str:
        color = eval(f'ColorString.{color.lower()}')
        return color + string + ColorString.end


class FeiShuMessage:
    content: Dict[str, Any]
    div_, ln_ = {"tag": "text", "text": "\n\n"}, {"tag": "text", "text": "\n"}

    def __init__(self, title_: str = None, content_: str = None):
        self.content = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": "Notification from Python" if title_ is None else title_,
                        "content": [[
                            {
                                "tag": "text",
                                "text": "content is empty" if content_ is None else content_
                            }
                        ]]
                    }
                }
            }
        }

    def to_json(self):
        return dumps_json(self.content)

    def extent(self, msg: str):
        self.content['content']['post']['zh_cn']['content'][0].extend([
            FeiShuMessage.ln_, {"tag": "text", "text": msg}
        ])


def send_feishu(title_: str = None, content_: str = None, url_: Union[str, Path] = None, with_machine_info: bool = True,
                pre_packed_msg: FeiShuMessage = None):
    if url_ is None:
        url_file = Path.home() / ".feishu_bot"
        if not os.path.exists(url_file):
            print_err(f"Feishu Bot need a explicit url or a file named {url_file} in your home directory to work.\n"
                      f".feishu_bot content can be like: https://open.feishu.cn/open-apis/bot/v2/hook/****\n"
                      f"Please create a bot in Feishu and get the url.")
            return
        with open(url_file, 'r', encoding='UTF-8') as f:
            url_ = f.read().strip()
    elif isinstance(url_, Path) or isinstance(url_, str) and os.path.exists(url_):
        with open(url_, 'r', encoding='UTF-8') as f:
            url_ = f.read().strip()
    else:
        raise ValueError(f"Invalid url: {url_}")
    msg = FeiShuMessage(title_, content_) if pre_packed_msg is None else pre_packed_msg
    if with_machine_info:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        my_ip = s.getsockname()[0]
        s.close()
        msg.extent("\n")
        msg.extent(f"Host IP: {my_ip} (This IP may be not accurate)")
        msg.extent(f"Host Name: {socket.gethostname()}")
    headers = {'Content-Type': 'application/json'}
    requests.post(url_, data=msg.to_json(), headers=headers)


def monit_feishu(title_ok: str = None, content_ok: str = None, url_: str = None, with_machine_info: bool = True,
                 title_err: str = None, content_err: str = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time_start = time.time()
            real_title_, real_content_ = None, None
            try:
                result = func(*args, **kwargs)
                real_title_ = f"Python Function {func.__name__}() Executed Successfully" if title_ok is None else title_ok
                real_content_ = f"args: {args}\nkwargs: {kwargs}" if content_ok is None else content_ok
                return result
            except Exception as e:
                e_str = str(e)
                real_title_ = f"Failed to Execute Python Function {func.__name__}()" if title_err is None else title_err
                real_content_ = f"args: {args}\nkwargs: {kwargs}\nError: {e_str}" if content_err is None else content_err
            finally:
                time_end = time.time()
                time_str = calc_time(time_start, time_end)
                # Your function has been executed successfully in xx:xx:xx.xx
                msg = FeiShuMessage(real_title_, real_content_)
                msg.extent(f"Running time: {time_str}")
                send_feishu(pre_packed_msg=msg, url_=url_, with_machine_info=with_machine_info)

        return wrapper

    return decorator


if __name__ == '__main__':
    send_feishu('test', 'test')
