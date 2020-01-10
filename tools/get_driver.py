# 6++++++++++
from selenium import webdriver


class GetDriver:
    __driver = None

    # 获取driver
    @classmethod
    def get_driver(cls, url):
        # 判断driver是否为None
        if cls.__driver is None:
            # 获取driver对象-->注意导包
            cls.__driver = webdriver.Chrome()
            # 最大化
            cls.__driver.maximize_window()
            # 打开url
            cls.__driver.get(url)
        return cls.__driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            # 退出driver
            cls.__driver.quit()
            # 置空 大坑
            cls.__driver = None
