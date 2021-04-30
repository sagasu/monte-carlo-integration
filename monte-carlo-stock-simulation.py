import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2020, 1, 3)
end = dt.datetime(2020, 11, 20)

prices = web.DataReader('AAPL','google', start, end)['Close']