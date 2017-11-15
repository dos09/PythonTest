import subprocess

test_num = 1

def test_check_output(cmd):
    global test_num
    print(' *** test %s ******************************************************************' 
        % test_num)
    test_num += 1
    
    b_res = subprocess.check_output(cmd, shell=True)
    res = b_res.decode('utf-8')
    print(res)

def test_Popen(cmd):
    global test_num
    print(' *** test %s ***' % test_num)
    test_num += 1

    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE) as proc:
        data, err = proc.communicate()
        print('data:',data.decode('utf-8'))
        print('err:', err)

test_check_output(['ls', '-l'])
test_check_output('ls -l')
try:
    test_check_output('whois q.com')
except subprocess.CalledProcessError as err:
    print(err)
    print(err.output.decode('utf-8'))

print('-------- using Popen -----------')

test_Popen('ls -l')
test_Popen('whois q.com')

# tested on linux 
# sudo apt-get update
# sudo apt-get install whois
