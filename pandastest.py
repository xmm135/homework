import pandas as pd
from pylab import *
import datetime

def testpd():
    df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")
    # df_rank = df.groupby(['rank','sex'])
    # df_sub = df[ df['salary'] > 150000 ]
    # print(df[10:20].sex)


    # print(df)
    # print(df.head())
    # print(df['rank'].dtype)



    # df['phd'].plot.bar()
    df['salary'].plot.hist()
    # df.plot()
    plt.show()

    # print(df.shape)
    # print(df.size)
    # print(df.describe())
    # print(df['service'].mean())
    # print(df.columns)
    # print(df_rank.mean())
    # print(df_sub)


def testtime():
	idx  = pd.date_range('2018-01-01', periods=365, freq='d') 
	print(idx)
	ts = pd.Series(range(len(idx)), index=idx)
	print(ts)
	# ts.plot.bar()
	# ts.plot
	# plt.show()
	ts.groupby(ts.index.quarter).sum().plot.bar()   #year month day quarter(季度)都可以
	plt.show()
    

def main():
	print("hhh")
	# testpd()
	testtime()

if __name__ == '__main__':
	main()
