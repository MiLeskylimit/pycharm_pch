# finally block�е�����������ζ��ᱻִ��
import sys

try:
    f = open('in2.txt', 'r')
except OSError as err:
    print('OS error: {}'.format(err))
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    print('Hello!')

# �Զ����쳣����
class MyInputError(Exception):
    """Exception raised when there're errors in input"""

    def __init__(self, value):  # �Զ����쳣���͵ĳ�ʼ��
        self.value = value

    def __str__(self):  # �Զ����쳣���͵�string�����ʽ
        return ("{} is invalid input".format(repr(self.value)))

try:
    raise MyInputError(1)  # �׳�MyInputError����쳣
except MyInputError as err:
    print('error: {}'.format(err))

# example
try:
    db = DB.connect('<db path>') # ���ܻ��׳��쳣
    raw_data = DB.queryData('<viewer_id>') # ���ܻ��׳��쳣
except (DBConnectionError, DBQueryDataError) as err:
    print('Error: {}'.format(err))
