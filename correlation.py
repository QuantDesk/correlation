import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from IPython.display import HTML 

# pd.set_option("display.max_rows", None, "display.max_columns", None)

# # a = np.loadtxt('IT.csv',delimiter=',')
a = pd.read_csv('nifty50.csv')

df = pd.DataFrame(data=a)

stock_str = """ADANIPORTS	ASIANPAINT	AXISBANK	BAJAJ-AUTO	BAJAJFINSV	BAJFINANCE	BHARTIARTL	BPCL	BRITANNIA	CIPLA
			COALINDIA	DRREDDY	EICHERMOT	GAIL	GRASIM	HCLTECH	HDFC	HDFCBANK	HEROMOTOCO	HINDALCO	HINDUNILVR	ICICIBANK	
			INDUSINDBK	INFY	IOC	ITC	JSWSTEEL	KOTAKBANK	LT	MARUTI	MM	NESTLEIND	NTPC	ONGC	POWERGRID	RELIENCE	SBIN
			SHREECEM	SUNPHARMA	TATAMOTORS	TATASTEEL	TCS	TECHM	TITAN	ULTRACEMCO	UPL	VEDL	WIPRO	ZEEL"""

df.columns = stock_str.split()

plt.figure(figsize=(50,50))

corr = df.corr()

sns.heatmap(corr)

plt.show()



#---------------------------
#Convert DataFrame to HTML
# r = corr.to_html()
# print(r)
#------------------------


#To Convert float string to list
# r1 = "1.000000	0.181117	0.302425	0.186603	0.225125	0.225313	0.156155	0.183224	0.134094	0.178191	0.141220	0.124762	0.173043	0.173066	0.284474	0.131970	0.238175	0.244810	0.213830	0.300374	0.131216	0.316941	0.231037	0.133116	0.176128	0.132961	0.295865	0.259548	0.304186	0.256391	0.201487	0.113345	0.240112	0.196097	0.174523	0.234795	0.305417	0.157954	0.180413	0.245131	0.292927	0.076675	0.124394	0.171222	0.287142	0.199327	0.251482	0.096780	0.174833"

# r1 = r1.split()

# l1 = []

# for i in r1:
# 	l1.append(i)

# l2 = []
# for i in l1:
# 	l2.append(float(i))

# l2.sort()

# print(l2[0:4])
