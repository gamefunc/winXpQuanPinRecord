import pynput, time
"""
pynput 录制全拼输入法;
其实就是自动鼠标键盘操作;
得出来的格式
# 格式 ai=爱=1, 拼音=字=顺序;
之后使用<深蓝词库转换.exe>转为WIN10的格式;

我录制的步骤:
1: 有个虚拟机装WINXP
2: 进去WINXP虚拟机后装PYTHON3.44(PYTHON只支持XP到PY3.4.4)
3: pip install pynput
4: 打开一个记事本
5: 鼠标点击记事本并且切换到全拼5.0输入法
6: 运行该脚本,5秒之内一定要点击一次记事本
7: 之后他自动操作了,可以挂机去干其他;
8: 录制完毕后,把TXT的内容复制出来即可
9: 自己写个大写转小写 open().read().lower();
10: 使用深蓝词库转换到win10可导入的格式(设置图已上传),下载地址如下: 
https://github.com/studyzy/imewlconverter/releases
11: WIN10自定义短语导入即可;

PS:理论上只要有足够拼音,就能录制全部语言;
"""

allPinYin = ['a','ai', 'an', 'ang', 'ao', \
'ba', 'bai', 'baike', 'ban', 'bang', \
'bao', 'bei', 'ben', 'beng', 'bi', 'bian', \
'biao', 'bie', 'bin', 'bing', 'bo', 'bu', 'bun', \
'ca', 'cai', 'can', 'cang', 'cao', 'ce', 'cen', 'ceng', \
'cha', 'chai', 'chan', 'chang', 'chao', 'che', 'chen', \
'cheng', 'chi', 'chong', 'chou', 'chu', 'chua', 'chuai', \
'chuan', 'chuang', 'chui', 'chun', 'chuo', 'ci', 'cong', 'cou', \
'cu', 'cuan', 'cui', 'cun', 'cuo', 'da', 'dai', 'dan', 'dang', 'dao', 'de', \
'dei', 'den', 'deng', 'di', 'dia', 'dian', 'diao', 'die', 'ding', 'diu', 'dong', \
'dou', 'du', 'duan', 'dui', 'dun', 'duo', 'e', 'ei', 'en', 'eng', 'er', 'fa', 'fan', \
'fang', 'fei', 'fen', 'feng', 'fenwa', 'fiao', 'fo', 'fou', 'fu', 'ga', 'gai', 'gan', 'gang', \
'gao', 'ge', 'gei', 'gen', 'geng', 'gi', 'gong', 'gongfen', 'gongli', 'gou', 'gu', 'gua', \
'guai', 'guan', 'guang', 'gui', 'gun', 'guo', 'ha', 'hai', 'haili', 'han', 'hang', 'hao', 'haoke', \
'he', 'hei', 'hen', 'heng', 'hng', 'ho', 'hong', 'hou', 'hu', 'hua', 'huai', 'huan', 'huang', 'hui', \
'hun', 'huo', 'ji', 'jia', 'jian', 'jiang', 'jiao', 'jie', 'jin', 'jing', 'jiong', 'jiu', 'ju', \
'juan', 'jue', 'jun', 'jv', 'ka', 'kai', 'kan', 'kang', 'kao', 'ke', 'kei', 'ken', 'keng', \
'kong', 'kou', 'ku', 'kua', 'kuai', 'kuan', 'kuang', 'kui', 'kun', 'kuo', 'la', 'lai', 'lan', \
'lang', 'lao', 'le', 'lei', 'leng', 'li', 'lia', 'lian', 'liang', 'liao', 'lie', 'lin', \
'ling', 'liu', 'liwa', 'lo', 'long', 'lou', 'lu', \
'luan', 'lun', 'luo', 'lv', 'lve', 'm', 'ma', 'mai', 'man', 'mang', \
'mao', 'maowa', 'me', 'mei', 'men', 'meng', 'mi', 'mian', 'miao', 'mie', \
'min', 'ming', 'miu', 'mo', 'mou', 'mu', 'n', 'na', 'nai', 'nan', 'nang', 'nao', 'ne', 'nei', 'nen', \
'neng', 'ng', 'ngai', 'ni', 'nian', 'niang', 'niao', 'nie', 'nin', 'ning', 'niu', 'nong', 'nou', 'nu', 'nuan', 'nun', \
'nuo', 'nv', 'nve', 'o', 'ou', 'pa', 'pai', 'pan', 'pang', 'pao', 'pei', 'pen', 'peng', 'pi', 'pian', 'piao', 'pie', 'pin', \
'ping', 'po', 'pou', 'pu', 'qi', 'qia', 'qian', 'qiang', 'qianke', 'qianwa', 'qiao', 'qie', 'qin', 'qing', 'qiong', 'qiu', \
'qu', 'quan', 'que', 'qun', 'ra', 'ran', 'rang', 'rao', 're', 'ren', 'reng', 'ri', 'rong', 'rou', 'ru', 'ruan', 'rui', \
'run', 'ruo', 'sa', 'sai', 'san', 'sang', 'sao', 'se', 'sen', 'seng', 'sha', 'shai', 'shan', 'shang', 'shao', 'she', \
'shei', 'shen', 'sheng', 'shi', 'shike', 'shiwa', 'shou', 'shu', 'shua', 'shuai', 'shuan', 'shuang', 'shui', 'shun', \
'shuo', 'si', 'song', 'sou', 'su', 'suan', 'sui', 'sun', 'suo', 'ta', 'tai', 'tan', 'tang', 'tao', 'te', 'teng', 'ti', \
'tian', 'tiao', 'tie', 'ting', 'tong', 'tou', 'tu', 'tuan', 'tui', 'tun', 'tuo', 'uu', 'wa', 'wai', 'wan', 'wang', \
'wei', 'wen', 'weng', 'wo', 'wu', 'xi', 'xia', 'xian', 'xiang', 'xiao', 'xie', 'xin', 'xing', 'xiong', 'xiu', 'xu', \
'xuan', 'xue', 'xun', 'ya', 'yan', 'yang', 'yao', 'ye', 'yi', 'yie', 'yin', 'ying', 'yingli', 'yo', 'yong', 'you', 'yu', 'yuan', \
'yue', 'yun', 'za', 'zai', 'zan', 'zang', 'zao', 'ze', 'zei', 'zen', 'zeng', 'zha', 'zhai', 'zhan', 'zhang', 'zhao', 'zhe', 'zhei', \
'zhen', 'zheng', 'zhi', 'zhong', 'zhou', \
'zhu', 'zhua', 'zhuai', 'zhuan', 'zhuang', 'zhui', 'zhun', 'zhuo', 'zi', 'zong', 'zou', 'zu', 'zuan', 'zui', 'zun', 'zuo']


def useKeyBoard(x, sleepTime=1):
    keyboard = pynput.keyboard.Controller()
    keyboard.press(x)
    keyboard.release(x)
    time.sleep(sleepTime)

def caps_lock_x2(keyboard):
    for i in range(2):
        keyboard.press(pynput.keyboard.Key.caps_lock)
        time.sleep(0.2)
        keyboard.release(pynput.keyboard.Key.caps_lock)
        time.sleep(0.3)

def getPinYin():
    # 实例化keyboard;
    keyboard = pynput.keyboard.Controller()
    for pinYin in allPinYin:
        for i in range(1,10):
            keyboard.press(pynput.keyboard.Key.shift_l)
            time.sleep(0.5)
            keyboard.type(pinYin)
            keyboard.release(pynput.keyboard.Key.shift_l)
            time.sleep(0.5)

            thisF = "={pinYin}{i}".format(pinYin=pinYin, i=i)
            keyboard.type(thisF)
            time.sleep(1)

            caps_lock_x2(keyboard)
            keyboard.type("={i}".format(i=i))

            keyboard.press(pynput.keyboard.Key.enter)
            time.sleep(0.2)
            keyboard.release(pynput.keyboard.Key.shift_l)
            time.sleep(0.5)
            


time.sleep(5)
getPinYin()
