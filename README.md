# SCUEC- nCoV-AutoReport

## 运行环境

此项目为使用selenium简单实现的每日健康情况报表自动化提交爬虫，要使用本项目，请确保电脑具备以下条件：

+ 较新版本的Python 3
+ selenium库
+ Chrome浏览器
+ 合适版本的chromedriver

在编写时，我的机器对应版本为：

+ macOS Big Sur 11.5.2
+ Python 3.9.6
+ selenium 3.141.0
+ Chrome 92.0.4515.131
+ ChromeDriver 92.0.4515.107

selenium可借助pip直接安装（尝试下面二者直至安装成功）：

```
pip install selenium	# anaconda等环境下
pip3 install selenium	# 系统默认安装环境下
```

ChromeDriver版本应与Chrome浏览器版本相对应，具体说明见下图。

![image-20210814050350779](/Users/visors/Library/Application Support/typora-user-images/image-20210814050350779.png)

**项目内自带了92版本的macOS和Windows下的ChromeDriver，请酌情使用。**若版本号不匹配，请更新chrome或前往国外源https://sites.google.com/a/chromium.org/chromedriver/downloads｜国内源http://npm.taobao.org/mirrors/chromedriver/下载对应版本的ChromeDriver。

## 使用方法

### 设置信息门户账号密码

打开文件ReportSpider.py，找到这两行：

![image-20210814051113237](/Users/visors/Library/Application Support/typora-user-images/image-20210814051113237.png)

修改为自己的账号密码即可。

### 设置selenium路径

打开文件ReportSpider.py，找到这两行：

![image-20210814051231343](/Users/visors/Library/Application Support/typora-user-images/image-20210814051231343.png)

将其改为你对应版本的ChromeDriver路径。

macOS下的ChromeDriver为Unix可执行文件，不需要后缀名。

Windows下的ChromeDriver为可执行文件，所以应添加后缀名.exe，即改上述内容为`./chromedriver.exe`

### 运行py文件

执行完上述步骤后，直接运行ReportSpider.py，当打印出*Login successfully!*时，说明后台已成功登录你的账号。当打印出*Report Successfully!*时，健康填报完成。

若抛出连接异常，则说明当前网络存在问题，可尝试重新执行py文件。若多次执行皆抛出异常，考虑填报网站服务器出现问题，可等待一段时间后再尝试。

## 注意事项

### 关于本脚本

使用selenium编写，实际是在后台运行一个headless Chrome，完全模拟人工操作流程，故编写时考虑到校园网站访问的卡满，在各个跳转间设置了休眠等待时间，整个填报流程耗时约30～60秒。

### 重要内容

由于健康填报表单内容有云端缓存，每次打开填报页面直接点提交就可以了，所以我在编写此脚本时并未逐一对表单内容进行填写——**这意味着你需要先手动提交一天后再使用本脚本**。

如果使用起来遇到了麻烦，可以联系我，我会考虑是否要对代码进行补全或改进。也希望使用者能借此机会了解一点爬虫知识，比如本项目的python+selenium，进而可以自行对本项目进行修改。selenium绝对不是效率高的选择，但却是最有效的选择之一。

---------

#### 若因使用本项目填错信息导致的一系列负面后果，本人概不负责。