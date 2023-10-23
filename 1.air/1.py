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
    assert_exists(Template(r"tpl1697945758209.png", record_pos=(-0.376, -0.248), resolution=(1200, 2664)), "找车展示正确")

    assert_exists(Template(r"tpl1697948809129.png", record_pos=(-0.001, 0.892), resolution=(1200, 2664)), "扫码开锁展示正确")
    swipe(Template(r"tpl1698056129365.png", record_pos=(-0.332, 0.672), resolution=(1200, 2664)), vector=[0, -100])
    assert_exists(Template(r"tpl1698064742161.png", record_pos=(-0.297, 0.517), resolution=(1200, 2664)), "用车规则展示正确")




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