import logging
import time
import os


def log_operation():
    # 获取项目的路径
    log_path = os.getcwd()+'\\Log_dir\\'
    # print('日志路径:',log_path )
    # 判断并创建日志目录
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    # 初始化日志器对象
    lo = logging.getLogger('lo')
    # 设置日志的级别
    lo.setLevel(logging.INFO)
    if not lo.handlers:  # 处理日志重复输出
        # 创建文件处理器
        file_clq = logging.FileHandler(
            filename=log_path + '{}_log.txt'.format(time.strftime("%Y%m%d%H%M%S", time.localtime())))
        # 创建格式器，处理日志器的格式
        gsq = logging.Formatter(fmt='%(asctime)s %(levelname)s [%(filename)s:%(lineno)d]: %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')
        # 给处理器设置格式
        file_clq.setFormatter(gsq)
        # 把处理器添加到日志器中才能展示
        lo.addHandler(file_clq)
    return lo