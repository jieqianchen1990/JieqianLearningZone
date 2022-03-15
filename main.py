import jieqian_packages.baidu_translator as trans

if __name__ == '__main__':
    # test code: 测试循环调用不同 appid 的效果，OK
    src_ls = ['This is a test sentence.', 'I am a translator using BaiduApi.']
    src_str = 'Python is a perfect programming language.'
    print(trans.translator(src_ls))
    print(trans.translator.call_number)
    print(trans.translator(src_str))
    print(trans.translator.call_number)
