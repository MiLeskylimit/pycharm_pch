# for与while的应用场景
# for循环更适用于已知的list、set
# while则更适合于未知的条件

while True:
    try:
        text = input('Please enter you questions, enter "q" to exit')
        if text == 'q':
            print('Exit system!')
            break
        print(response)
    except Exception as err:
        print('Encountered error: {}'.format(err))
        break


# Exe
