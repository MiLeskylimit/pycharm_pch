# finally block中的内容无论如何都会被执行
import sys

try:
    f = open('in2.txt', 'r')
except OSError as err:
    print('OS error: {}'.format(err))
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    print('Hello!')

# 自定义异常函数
class MyInputError(Exception):
    """Exception raised when there're errors in input"""

    def __init__(self, value):  # 自定义异常类型的初始化
        self.value = value

    def __str__(self):  # 自定义异常类型的string表达形式
        return ("{} is invalid input".format(repr(self.value)))

try:
    raise MyInputError(1)  # 抛出MyInputError这个异常
except MyInputError as err:
    print('error: {}'.format(err))

# example
try:
    db = DB.connect('<db path>') # 可能会抛出异常
    raw_data = DB.queryData('<viewer_id>') # 可能会抛出异常
except (DBConnectionError, DBQueryDataError) as err:
    print('Error: {}'.format(err))
