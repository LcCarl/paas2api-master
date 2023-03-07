接口自动化规范
===

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.7-blue"/>
    <img src="https://img.shields.io/badge/Doc. Last Update Time-2021.8.2-blue"/>
</p>

```
逻辑层更新履历：
2021/5/12
1.新增sql_type 4，用于校验sql结果非空
2021/5/10
1.当前版本不再需要手动维护tools/project_path & tools/init_list
2.强调config / testcase / init 文件命名规范
3.支持空冷测试环境
2021/8/2
1.添加返回值多种断言方式
```

# 1. 前言
+ 本自动化框架采用 `unittest+request+ddt+HTMLTestRunnerNew`
+ 代码管理采用 `gitlab`
+ 持续集成采用 `Jenkins`
+ 目前'get''patch'类型（且参数为字典）提供参数传递；其余类型提供json传递；

# 2. 目录
|    目录    |     含义     | 权限 |       说明       |
| :--------: | :--------: | :--------: | :--------: |
|    Conf    |    配置层    |  √   |     公用模块     |
| Data_excel |  测试用例层  |  √   | 只操作自己的模块 |
| Data_init  | 参数预定义层 |  √   | 只操作自己的模块 |
|   Result   |   测试结果   |      |                  |
|   Tools    |    工具层    |      |                  |
|   run.py   |   批量执行文件   |     |         |
|   run_single.py  |   单个执行文件   |     |         |
|   README.md   |   说明文档  |    |          |
  
![image](http://172.19.32.226:8900/zoujie/paas2api/raw/master/readme/readme.files/readme282.png?inline=false)  

#### 2.1添加模块/用例表顺序
1.	添加excel用例表，将内容填完，并将表放入data_excel文件夹中  
2.	在conf文件夹的.config文件中配置excel名、sheet名、执行行； 
3.	在data_init文件夹，对应模块的文件中，配置预定义参数——如果没有对应模块文件，则新增  
4.	在执行文件run中，执行文件  

### `注意！！config中的mode_list内容、mode中的参数名、用例excel的文件名，需要保持一致！！！！！！！`
![image](http://172.19.32.226:8900/zoujie/paas2api/raw/master/readme/readme.files/readme4001.png?inline=false)   


# 3. 规则
### 步骤1：用例数据层：
 - Data_excel——  
>根据自己的模块的功能点，自行按需新增文件。  
>>文件命名规则：test_case_功能名.xlsx  <br>

>文件内部sheet：  
>>自己控制好一张sheet放多少接口，总体一张sheet中用例数量不要超过100行。  
>>单个接口的所有前置，也体现在同一张sheet中  

 - 举个栗子sheet：    
 ![image](http://172.19.32.226:8900/zoujie/paas2api/raw/master/readme/readme.files/readme664.png?inline=false)    
 ![image](http://172.19.32.226:8900/zoujie/paas2api/raw/master/readme/readme.files/readme666.png?inline=false)  
 
 | **序号** | **列** |        **列名**        |          **影响范围**          | **何时需要填写**                                        | **填写规则**                                                 |
| :------: | :----: | :--------------------: | :----------------------------: | :------------------------------------------------------ | :----------------------------------------------------------- |
|    1     |   A    |          序号          |          结果写回位置          | all                                                     |                                                              |
|    2     |   B    |        sheet名         |          结果写回表单          | all                                                     |                                                              |
|    3     |   C    |         模块名         |      展示在报告用例标题中      | all                                                     |                                                              |
|    4     |   D    |      测试用例名称      |      展示在报告用例标题中      | all                                                     |                                                              |
|    5     |   E    |        请求方式        |                                | all                                                     |                                                              |
|    6     |   F    |          接口          |                                | all                                                     |                                                              |
|    7     |   G    |        请求数据        |                                | all                                                     | Rule：字典，参数如果需要替换，**见下方注释1**                |
|    8     |   H    |       变更参数名       |    下一次使用同一个参数的值    | G列数据的参数，在使用过后，  下次调用需要换成新的参数值。 | Rule：列表嵌套字符串，无顺序要求。  例子：["RentName"]  <br>*只要H列写了参数名，那么在init文件中，  <br>就要建两个对应的参数：  RentName  = 随机数  RentName_cur = None |
|    9     |   I    |    测试用例路径地址    |         结果写回excel          | all                                                     | Rule：对应project_path文件中的参数名  例子：test_case_authService |
|    10    |   J    |       init文件名       | 对应数据库；  对应init文件参数 | all                                                     | Rule：对应init文件的文件名，不需要写文件后缀  例子：auth_service_init |
|    11    |   K    |      接口运行耗时      |                                | ——                                                      |                                                              |
|    12    |   L    |        预期code        |                                | all                                                     |                                                              |
|    13    |   M    |        实际code        |                                | ——                                                      |                                                              |
|    14    |   N    |     L和M的对比结果     |                                | ——                                                      | 一致pass，不一致fail                                         |
|    15    |   O    |        sql验证         |          sql查询结果           | 需要sql验证时                                           | **见下方注释2**                                              |
|    16    |   P    |  保存查询结果的参数名  |          后续参数引用          | O列数据，在查询过后，需要  将查询结果保存到一个参数名中。 | Rule：列表嵌套字符串，顺序要求如下：若查询多个结果，  按照查询顺序，来排列接收参数名的顺序。  例子：["RentID"] |
|    17    |   Q    |    验证sql查询结果     |                                | ——                                                      | 成功填入查询结果，或显示pass，失败fail                       |
|    18    |   R    | 查询结果是否与期望一致 |                                | 需要对返回结果进行期望比对时                            | **见下方注释3**                                              |
|    19    |   S    |      R的对比结果       |                                | ——                                                      | 一致pass，不一致fail                                         |
|    20    |   T    |        前提条件        |                                | 需要用到前面用例的返回值时                              | Rule：sheet名>用例id>返回值参数，多个用逗号隔开    <br>例子：  login>1>data.access_token,  login>4>data[*].id，  login>4>data |
|    21    |   U    |         关键字         |                                | T列填写时且G列为字典形式 <br>*如果此列不填，则表示G列不是字典形式，T列结果将以列表添加的形式进入data| Rule：G列中需要放入值的参数名路径，多个用逗号隔开    <br>例子：pid、pid,platformProjects[*].platformId |

#### 注释1：
 - 被替换的值，在http请求之前能获取，参数名格式：${参数名}  
 - 被替换的值，在http请求之后才能获取，参数名格式：*{参数名}  
 - 若${参数名}，里面的参数被写在了H列，下次还想调用更新之前的值，那么需要使用${参数名_cur}来调用  
#### 注释2：
 - Sql类型如下：（如有新的可添加）
 
| **sql列** |      |                                                              | 示例|
| ------- | ------- | ----------------------------------------------------------- |------- | 
| sql_type  |  1   | 创建新的（网关），查看数据库是否新建成功，并返回元组，将查询内容返回 |{"sql":"SELECT user_id,id FROM ...","sql_type":1}|
|           |  2   | 查询数据库的结果，和request的data条数做对比                  |{"sql":"SELECT count(id) FROM ...","sql_type":2}|
|           |  3   | 查询结果期望为空                                             |{"sql":"SELECT user_id FROM ...","sql_type":3}|
|           |  4   | 查询结果期望为非空                                             |{"sql":"SELECT user_id FROM ...","sql_type":4}|
| expected  |      | 将查询结果和期望值做比对，如果比对多个值，”xxx,xxx,xxx”|{"sql":"SELECT user_id,id FROM ...","expected":"*{UserID},20"}|
| database  |      | 查询语句对应的数据库；此优先级高于J列init的对应关系。|{"sql":"SELECT ...","database":"service-project"}|

#### 注释3：
| **expected列** |      |                                                              |
| ------- | ------- | ----------------------------------------------------------- |
| expected_type  |  1   | 结果中PageSize值和target是否一致：  {"expected_type":1,"target":${PageSize}} |
|           |  2   | 期望查询结果中data不为空：{"expected_type":2}                  |
|           |  3   | 返回中msg是否包含期望值：{"expected_type":3,"msg":"consist"}                 |
|           |  4   | 期望查询结果中data为空                  |
 
  - Data_init——  
根据自己的模块，自行按需新增文件。  
本文件存放所有需要使用的参数。  
>>文件命名规则：模块名_init.py 
>>类名命名规则：XxxInit   ——驼峰命名，且包含Init 

参数命名规则：  
>>根据接口参数名命名，规则使用驼峰命名，如：AgentNum  
>>所有获取当前数值的参数名，为：原参数_cur。如：AgentNum_cur

![image](http://172.19.32.226:8900/zoujie/paas2api/raw/master/readme/readme.files/readme1791.png?inline=false)  

### 步骤2：工具配置层：
### >Conf——
>环境配置：
>>environment_type的值：
>>>1——旧的paas，测试环境  
>>>2——旧的paas，开发环境  
>>>5——新的paas，测试环境  
>>>11——空冷，   生产环境

可切换环境，合并代码时请默认测试环境。请勿私自变更修改。  
当环境中的数据库配置时，无法固定database，则需要额外进行数据库的对应关系  init_database配置，`此字典名固定，不能变更`。具体如下：  
init_database的值：
```
init_database = {
        "auth_service_init": "auth_service"
    }
```
字典键值对，键：excel中J列的值；值：数据库名  
![image](http://172.19.32.226:8900/zoujie/paas2api/raw/master/readme/readme.files/readme4000.png?inline=false)  
  - #### 测试用例配置：
如下图。根据自己的模块，在里面添加。请勿增加文件。  
分为case.config（测试调试用）、case_new.config（新paas用于Jenkins运行）、<br> 
case_old.config（旧paas用于Jenkins运行），合并时请切换case_new.config。配置<br>
文件请保持最新最全  
![image](http://172.19.32.226:8900/zoujie/paas2api/raw/master/readme/readme.files/readme1986.png?inline=false)  
#### 注意：config中的mode_list内容、mode中的参数名、用例excel的文件名，需要保持一致！！！！！！！

### >Tools——
## `勿修改原有文件，如果实在有需求，请告知邹洁，由邹洁统一修改。  `
如果由需要新增工具类，可自行新增。提交合并时请告知邹洁。命名只需要简单易懂即可。  


 ### 步骤3：执行层
 ## `Run文件请勿修改！！`

 ### 步骤4：结果层
- 日志：按小时生成
- 报告：自动生成，用浏览器打开查看。如果需要配置报告中的用例标题，请使用下方设置。

# 4.设置
进入mk_test_name方法类  
![image](http://172.19.32.226:8900/zoujie/paas2api/raw/master/readme/readme.files/readme2235.png?inline=false)  
![image](http://172.19.32.226:8900/zoujie/paas2api/raw/master/readme/readme.files/readme2237.png?inline=false)    
将原有方法注释掉，换成以下内容：  
****
```
# # Add zeros before index to keep order
    # index = "{0:0{1}}".format(index + 1, index_len)
    # if not is_trivial(value):
    #     return "{0}_{1}".format(name, index)
    # try:
    #     value = str(value)
    # except UnicodeEncodeError:
    #     # fallback for python2
    #     value = value.encode('ascii', 'backslashreplace')
    # test_name = "{0}_{1}_{2}".format(name, index, value)
    # return re.sub(r'\W|^(?=\d)', '_', test_name)
```
****
```
 # Add zeros before index to keep order
    index = "{0:0{1}}".format(index + 1, index_len)
    # 测试用例名称读取 case_name 字段的值 start --Victor
    # 添加了对字典数据的处理。
    if not is_trivial(value) and type(value) is not dict:
        return "{0}_{1}".format(name, index)
    # 如果数据是字典，则获取字典当中的api_name对应的值，加到测试用例名称中。
    if type(value) is dict:
        try:
            value = value["case_name"]  # case_name作为value值
        except:
            return "{0}_{1}".format(name, index)
    # if not is_trivial(value):  # 注释原有方法
    #     return "{0}_{1}".format(name, index)
    # 测试用例名称读取 case_name 字段的值 end --Victor
    try:
        value = str(value)
    except UnicodeEncodeError:
        # fallback for python2
        value = value.encode('ascii', 'backslashreplace')
    test_name = "{0}_{1}_{2}".format(name, index, value)
    return re.sub(r'\W|^(?=\d)', '_', test_name)
```
****
