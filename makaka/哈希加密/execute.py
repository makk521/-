'''
参考：
    https://www.tomczhen.com/2016/10/10/hashing-security/
'''
import os
def check_hash(password_input,password_hashed):
    '''
    哈希验证，用以验证当前输入的密码与之前存储的密码
    参数：输入的密码与原始密码哈希值
    '''
    if hash(password_input) == password_hashed:
        return True
    else:
        return False

def hash_add_salt(password):
    '''
    加盐哈希
    '''
    salt = str(os.urandom(20))  
    password_with_salt = password + salt
    return hash(password_with_salt)

print(check_hash('111',hash('111')))
print(hash_add_salt('111'))