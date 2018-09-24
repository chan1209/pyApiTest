- 基于python的接口测试框架
    * python
    * requests 接口调用
    * unittest 测试框架
    * xlrd excel数据读取

- 数据驱动
```python
@data(*ExcelUtil().getAllParams('ad'), unpack=False)
def test_getAllParams(self, reward):
    """
        获取tag对应参数
    """
    print(reward)
```
*ExcelUtil().getAllParams('ad') 作用根据tag名称筛选对应的元组数据，并传递到函数中，用于接口请求数据

- 接口调用
```python
import myrequests as requests # 引入自定义requests包

url = 'https://www.baidu.com'
logger.close_print_info() # 是否打印日志
r = requests.get(url)
if r:
    print(r.text)

```
post模式传入url和excel得到的元组即可，如果有header的特殊配置，可加上

- setting类提供多个设置选项进行配置
```python
class setting:

    # 只运行的用例类型
    run_case = {Tag.SMOKE}

    # 开启用例排序
    sort_case = True

    # 每个用例的执行间隔，单位是秒
    execute_interval = 0.1

    # 开启检测用例描述
    check_case_doc = True

    # 显示完整用例名字（函数名字+参数信息）
    full_case_name = False

    # 测试报告显示的用例名字最大程度
    max_case_name_len = 80

    # 执行用例的时候，显示报错信息
    show_error_traceback = True

    # 生成ztest风格的报告
    create_ztest_style_report = True

    # 生成bstest风格的报告
    create_bstest_style_report = True
```


- 集成 [ztest](https://github.com/zhangfei19841004/ztest) 和 [BSTestRunner](https://github.com/easonhan007/HTMLTestRunner) 自动生成两份测试报告，感谢两位作者的测试报告模版

> ztest风格

![ztest风格](https://github.com/jianbing/utx/raw/master/img/ztest.png)

> bstest风格

![bstest风格](https://github.com/jianbing/utx/raw/master/img/bstest.png)


- 集成[utx](https://github.com/jianbing/utx)功能，优化了unittest框架，感谢作者

