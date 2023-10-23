# -*- encoding=utf8 -*-
__author__ = "落花流水"

from airtest.core.api import *

auto_setup(__file__)
# -*- encoding=utf8 -*-
__author__ = "落花流水"

from airtest.core.api import *

auto_setup(__file__)



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

id = "com.jingyao.easybike"

#用例执行主要逻辑
def case():
    touch(Template(r"tpl1697875039491.png", record_pos=(-0.235, 0.514), resolution=(1200, 2664)))
    touch(Template(r"tpl1697875077075.png", record_pos=(-0.001, -0.763), resolution=(1200, 2664)))
    touch(Template(r"tpl1698065145690.png", record_pos=(-0.367, -0.468), resolution=(1200, 2664)))
    wait(Template(r"tpl1698065185551.png", record_pos=(-0.282, 0.195), resolution=(1200, 2664)))
    swipe(Template(r"tpl1698065206319.png", record_pos=(-0.282, 0.204), resolution=(1200, 2664)), vector=[0, -100])

    touch(Template(r"tpl1698065279360.png", record_pos=(-0.376, -0.249), resolution=(1200, 2664)))
    assert_exists(Template(r"tpl1698065317178.png", record_pos=(0.258, 0.876), resolution=(1200, 2664)), "立即兑换按钮展示正确")





#用例的初始化工作
def set_up():
    stop_app(id)
    home()
    start_app(id)
    
#用例执行完成后的清理工作
def tear_down():
    stop_app(id)
    home()

#用例执行的框架，任何异常就要到tear_down完成清理
def case_main():
    try:
        set_up()
        case()
        tear_down()
    except:
        tear_down()
case_main()