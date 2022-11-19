# 用于方便创建ISE的管脚配置文件

HDU管脚配置的教程可以参考这篇博客：
> [【杭电数电实验】verilog入门指北](https://blog.csdn.net/kjy55262227/article/details/121871190?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166884728816782414989716%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166884728816782414989716&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-121871190-null-null.142^v65^wechat,201^v3^control,213^v2^t3_esquery_v3&utm_term=%E6%9D%AD%E7%94%B5%E6%8C%87%E5%8C%97&spm=1018.2226.3001.4187)

##表格文件中  
第一行：开关  
第二行：灯泡  
第三行：按钮  
第四行：由于上下跳沿要忽略时钟配置规则的变量（所有使用了posedge或negedge的变量）

**注意：**  
n位变量请在变量名后加入'[n-1]'