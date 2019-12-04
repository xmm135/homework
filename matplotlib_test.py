# import numpy as np 
# from matplotlib import pyplot as plt 
 
# x = np.arange(1,11) 
# y = x^2
# plt.title("Matplotlib demo") 
# plt.xlabel("x axis caption") 
# plt.ylabel("y axis caption") 
# plt.plot(x,y) 
# plt.show()

# import numpy as np 
# from matplotlib import pyplot as plt 
# import matplotlib
 
# # fname 为 你下载的字体库路径，注意 SimHei.ttf 字体的路径
# zhfont1 = matplotlib.font_manager.FontProperties(fname="SimHei.ttf") 
 
# x = np.arange(1,11) 
# y =  2  * x +  5 
# plt.title("许明铭的demo", fontproperties=zhfont1) 
 
# # fontproperties 设置中文显示，fontsize 设置字体大小
# plt.xlabel("我的x轴", fontproperties=zhfont1)
# plt.ylabel("我的y轴", fontproperties=zhfont1)
# plt.plot(x,y,"ob")
# # plt.plot(x,y)
# plt.show()

# import numpy as np 
# from matplotlib import pyplot as plt 
# import matplotlib
# zhfont1 = matplotlib.font_manager.FontProperties(fname="SimHei.ttf") 
# # 计算正弦曲线上点的 x 和 y 坐标
# x = np.arange(0,  3  * np.pi,  0.1) 
# y = np.tan(x)
# plt.title("tan函数", fontproperties=zhfont1)  
# # 使用 matplotlib 来绘制点
# plt.xlabel("x轴", fontproperties=zhfont1)
# plt.ylabel("y轴", fontproperties=zhfont1)
# plt.plot(x, y) 
# plt.show()

# from matplotlib import pyplot as plt 
# x =  [5,8,10] 
# y =  [12,16,6] 
# x2 =  [6,9,11] 
# y2 =  [6,15,7] 
# plt.bar(x, y, color =  'k',align =  'center') 
# plt.bar(x2, y2, color =  'c', align =  'center') 
# plt.title('Bar graph') 
# plt.ylabel('Y axis') 
# plt.xlabel('X axis') 
# plt.show()

import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib
zhfont1 = matplotlib.font_manager.FontProperties(fname="SimHei.ttf")
# 计算正弦和余弦曲线上的点的 x 和 y 坐标 
x = np.arange(0,  30  * np.pi,  0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)
y_tan = np.tan(x)  
# 建立 subplot 网格，高为 2，宽为 1  
# 激活第一个 subplot
plt.subplot(5,  1,  1)  
# 绘制第一个图像 
plt.plot(x, y_sin) 
plt.title("正弦函数", fontproperties=zhfont1)  
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(5,  1,  3) 
plt.plot(x, y_cos) 
plt.title("余弦函数", fontproperties=zhfont1) 
# 激活第三个 subplot
plt.subplot(5,  1,  5)  
# 绘制第三个图像 
plt.plot(x, y_tan) 
plt.title("正切函数", fontproperties=zhfont1)  
# 展示图像
plt.show()