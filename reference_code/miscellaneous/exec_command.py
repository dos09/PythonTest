from subprocess import call, check_output, CalledProcessError


def test01():
    cmd = 'cd'
    res_code = call(cmd, shell=True)
    print(res_code)


def test02():
    cmd = 'cd'
    try:
        output = check_output(cmd, shell=True)

        print(output.decode('utf-8'))
    except CalledProcessError as e:
        print('Error occurred, code:', e.returncode)
        print(e.output.decode('utf-8'))

# test01()
test02()
