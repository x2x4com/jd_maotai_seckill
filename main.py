import sys
from os import path

from maotai.jd_spider_requests import JdSeckill

try:
    config = sys.argv[1]
except IndexError:
    config = "config.ini"

if not path.exists(config):
    raise RuntimeError("%s not existed" % config)

if __name__ == '__main__':
    a = """
功能列表：                                                                                
 1.预约商品
 2.秒杀抢购商品
    """
    print(a)

    jd_seckill = JdSeckill(config)
    choice_function = input('请选择:')
    if choice_function == '1':
        jd_seckill.reserve()
    elif choice_function == '2':
        jd_seckill.seckill_by_proc_pool()
    else:
        print('没有此功能')
        sys.exit(1)

