""" lec_pd_indexing.py

Companion codes for the lecture on indexing pandas objects
"""

import pandas as pd

# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
dates = [
  '2020-01-02',
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600,
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# Trading day counter
bday = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10]

# # ----------------------------------------------------------------------------
# #   Create instances
# # ----------------------------------------------------------------------------
#
# # Create a series object
ser = pd.Series(data=prices, index=dates)
print(ser)
#
# # Output:
# #   2020-01-02    7.16
# #   2020-01-03    7.19
# #   2020-01-06    7.00
# #   2020-01-07    7.10
# #   2020-01-08    6.86
# #   2020-01-09    6.95
# #   2020-01-10    7.00
# #   2020-01-13    7.02
# #   2020-01-14    7.11
# #   2020-01-15    7.04
# #   dtype: float64
#
#
# # Data Frame with close and Bday columns
df = pd.DataFrame(data={'Close': ser, 'Bday': bday}, index=dates)
print(df)
#
# # Output:
# #             Close  Bday
# # 2020-01-02   7.16     1
# # 2020-01-03   7.19     2
# # 2020-01-06   7.00     3
# # 2020-01-07   7.10     4
# # 2020-01-08   6.86     5
# # 2020-01-09   6.95     6
# # 2020-01-10   7.00     7
# # 2020-01-13   7.02     8
# # 2020-01-14   7.11     9
# # 2020-01-15   7.04    10
#
# # ----------------------------------------------------------------------------
# #   Outline:
# #
# #   1. Selection using .loc (label based)
# #     1.1 Series:
# #       1.1.1 Selection using a single label
# # ser.loc[label] --> scalar if label in index, error otherwise
#
# # # Set `x` below to be the price on 2020-01-10
# x = ser.loc['2020-01-10'] # --> 7.0
# print(x)
# # Using .loc to set elements:
# # Copy the series
# ser2 = ser.copy()
# print(ser2)
#
# # Output:
# #  2020-01-02    7.16
# #  2020-01-03    7.19
# #  2020-01-06    7.00
# #  2020-01-07    7.10
# #  2020-01-08    6.86
# #  2020-01-09    6.95
# #  2020-01-10    7.00
# #  2020-01-13    7.02
# #  2020-01-14    7.11
# #  2020-01-15    7.04
# #  dtype: float64
# #
# # # Set the price for 2020-01-02 to zero
# ser2.loc['2020-01-02'] = 0
# print(ser2)
# # # 1.1.2 Series.loc: Selection using sequence of labels
# # # will return a series
# #
# x = ser.loc[['2020-01-03', '2020-01-10']]
# print(x)
# #
# # # Output:
# # #  2020-01-03    7.19
# # #  2020-01-10    7.00
# # #  dtype: float64
# #
# print(type(x)) # --> <class 'pandas.core.series.Series'>
# # # Output:
# # #    2020-01-02    0.00   <-- Note the difference
# # #    2020-01-03    7.19
# # #    2020-01-06    7.00
# # #    2020-01-07    7.10
# # #    2020-01-08    6.86
# # #    2020-01-09    6.95
# # #    2020-01-10    7.00
# #    2020-01-13    7.02
# #    2020-01-14    7.11
# #    2020-01-15    7.04
# #    dtype: float64
#
#
#
#
# #
# #
# #
# # #       1.1.2 Selection using sequence of labels
# # #       1.1.3 Selection using slices
# # #     1.2 DataFrame:
# # #       1.2.1 Selection using a single label
# # #       1.2.2 Selection using sequence of labels
# # #       1.2.3 Selection using slices
# # # 1.2 DataFrames
# # # -------------
# #
# # # 1.2.1 Selection using a single label:
# # # A single row and column labels will return a single value (scalar)
# #
# # # For instance, selecting the close price on January 3, 2020
# x = df.loc['2020-01-03', 'Close']
# print(x) # --> 7.19
# #
# # # A single row **or** a single column label will return a series:
# # # The following will return a series corresponding to the column "Close"
# x = df.loc[:,'Close']
# print(x)
#
# # Output :
# # 2020-01-02    7.16
# # 2020-01-03    7.19
# # 2020-01-06    7.00
# # 2020-01-07    7.10
# # 2020-01-08    6.86
# # 2020-01-09    6.95
# # 2020-01-10    7.00
# # 2020-01-13    7.02
# # 2020-01-14    7.11
# # 2020-01-15    7.04
# # Name: Close, dtype: float64
# #
# # type(df.loc[:, 'Close']) # --> <class 'pandas.core.series.Series'>
#
# y = df.loc['2020-01-03', :]
# print(y)
# #
# # # Output:
# # # Close    7.19
# # # Bday     2.00
# # # Name: 2020-01-03, dtype: float64
# #
# print(type(df.loc['2020-01-03', :])) # --> <class 'pandas.core.series.Series'>
# #
# # # When omitting column labels, pandas will return a series if the row label
# # # exists. Otherwise it will raise an exception
# #
# # # This is equivalent to df.loc['2020-01-03',:]
# x = df.loc['2020-01-03']
# print(x)
# #
# # # Out:
# # # Close    7.19
# # # Bday     2.00
# # # Name: 2020-01-03, dtype: float64
#
# #
# print(type(df.loc['2020-01-03'])) # --> <class 'pandas.core.series.Series'>
# #
# # # This will raise an exception because the label does not exist
# # b = df.loc['2020-01-01']
# # print(b)
# #

# 1.2.2 Dataframe.loc: Selection using sequence of labels

# Set x so it contains the closing prices for '2020-01-02' and '2020-01-03'
x = df.loc[['2020-01-02', '2020-01-03'], 'Close']
print(x)

# Output:
#  2020-01-02    7.16
#  2020-01-03    7.19
#  Name: Close, dtype: float64

# 1.2.3 Dataframe.loc: Selection using slices
# Using slices will return
#  - A series if the other index is a single label
#  - A data frame otherwise

# the next statement is equivalent to x = df.loc['2020-01-01':'2020-01-10']
x = df.loc['2020-01-01':'2020-01-10', :]
print(x)
# b = df.loc['2020-01-01']
# print(b)
# #
# Output:
#             Close  Bday
# 2020-01-02   7.16     1
# 2020-01-03   7.19     2
# 2020-01-06   7.00     3
# 2020-01-07   7.10     4
# 2020-01-08   6.86     5
# 2020-01-09   6.95     6
# 2020-01-10   7.00     7

print(type(x)) # --> <class 'pandas.core.frame.DataFrame'>








#   2. Selection using .iloc (position based)
#     2.1 Series:
#       2.1.1 Selection using a single label
#       2.1.2 Selection using sequence of labels
#       2.1.3 Selection using slices


df = pd.DataFrame({'co11': range(10), 'co12': range(10, 20)}, index=list('acgfhibdje'))
print(df)
resu = df.loc[['b', 'c', 'd', 'e'], 'co11']
print(resu)
d = df.sort_index(inplace=True)
print(d)
res = df.loc['b' : 'e', 'co11']
print(res)
sv = df.loc[['b', 'd', 'f', 'j'], ['co11']]
print(sv)


# 2.1
# 2.1 Series
# -------------

# 2.1.1 Series.iloc: Selection using a single label
# Series.iloc using single index will return a numpy scalar

# ser.iloc[pos] --> scalar if abs(pos) < len(ser), otherwise error
x = ser.iloc[0]  # --> 7.16
print(x)
x = ser.iloc[-1] # --> 7.04
print(x)
# x = ser.iloc[100] # raises IndexError

# Using .loc for assignment
# Copy the series
s2 = ser.copy()
print(s2)

# assign
s2.iloc[0] = 0
print(s2)

# Output:
# 2020-01-02    0.00
# 2020-01-03    7.19
# 2020-01-06    7.00
# 2020-01-07    7.10
# 2020-01-08    6.86
# 2020-01-09    6.95
# 2020-01-10    7.00
# 2020-01-13    7.02
# 2020-01-14    7.11
# 2020-01-15    7.04
# dtype: float64

# 2.1.2 Series.iloc: Selection using sequence of labels

x = ser.iloc[[0, 2]]
print(x)

# Output:
# 2020-01-02    7.16
# 2020-01-06    7.00
# dtype: float64

# 2.1.3 Series.iloc: Selection using slices
# Slices will not include endpoints, otherwise, work like ser.loc

x = ser.iloc[0:1] # x --> series with one row
print(x)
# Output:
# 2020-01-02    7.16
# dtype: float64


x = ser.iloc[0:2]
print(x)
# Output:
# 2020-01-02    7.16
# 2020-01-03    7.19
# dtype: float64





#     2.2 DataFrame:
#       2.2.1 Selection using a single label
#       2.2.2 Selection using sequence of labels
#       2.2.3 Selection using slices
#
# 2.2 Dataframe
# -------------

# 2.2.1 Dataframe.iloc: Selection using a single label

# df.iloc[row pos] --> series if abs(pos) < len(df.index)
# --> series with elements from the first "row" -- column labels as row indexes

x = df.iloc[0]
print(x)

# Output:
#   Close    7.16
#   Bday     1.00

# Equivalent to
x = df.iloc[0,:]
print(x)

# Output:
#   Close    7.16
#   Bday     1.00


# x = df.iloc[10] # --> raises IndexError because the DF contains 10 rows

# First column (and all rows):
x = df.iloc[:,0]
print(x)

# Output:
# 2020-01-02    7.16
# 2020-01-03    7.19
# 2020-01-06    7.00
# 2020-01-07    7.10
# 2020-01-08    6.86
# 2020-01-09    6.95
# 2020-01-10    7.00
# 2020-01-13    7.02
# 2020-01-14    7.11
# 2020-01-15    7.04
# Name: Close, dtype: float64
#
# This will return a series with the first two columns as labels:
x = df.iloc[0,[0,1]]
print(x)

# Output :
#   Close    7.16
#   Bday     1.00
#   Name: 2020-01-02, dtype: float64

# This will return a *dataframe* with the first row of df
x = df.iloc[0:1,:]
print(x)

# Output:
#             Close  Bday
# 2020-01-02   7.16     1

# print(type(x)) # --> <class 'pandas.core.frame.DataFrame'>

# If the column indexer is omitted, all columns will be returned.

# df.iloc[list of row pos] --> dataframe with rows in the list
# Note: will raise IndexError if pos is out of bounds
x = df.iloc[[0, 1]] # --> DF with first two rows of df
print(x)

# Output:
#             Close  Bday
# 2020-01-02   7.16     1
# 2020-01-03   7.19     2


df = pd.DataFrame({'co11' : range(0,20), 'co12' : range(20,40), 'co13' : range(40,60)})
print(df)
f = [i for i in 'co12']
fbh = df.iloc[::2, 1]
print(fbh)




#   3. Selection using []
#     3.1 Series:
#       3.1.1 label, list of labels, label slices
#       3.1.2 position, list of positions, position slices
#

print(ser)

# Out:
#    2020-01-02    7.16
#    2020-01-03    7.19
#    2020-01-06    7.00
#    2020-01-07    7.10
#    2020-01-08    6.86
#    2020-01-09    6.95
#    2020-01-10    7.00
#    2020-01-13    7.02
#    2020-01-14    7.11
#    2020-01-15    7.04
#    dtype: float64


# 3.1.1 label, list of labels, label slices

# Set `x` to be the price for '2020-01-13'
x = ser['2020-01-13']
print(x) # --> 7.02

# The following raises KeyError because label not part of ser.index
# x = ser['3000-01-10']
# print(x)

# Set `x` to be a series with the first two rows of `ser`
x = ser[['2020-01-02', '2020-01-03']] # --> first two rows
print(x)

# All labels must exist
# x = ser[['2020-01-02', '3000-01-10']] # raises KeyError because a label is not part of ser.index


# Set `x` to include all obs between  '2020-01-13' and '2020-01-14'
x = ser['2020-01-13':'2020-01-14']
print(x)

# Output:
# 2020-01-13    7.02
# 2020-01-14    7.11
#  dtype: float64

# 3.1.2 position, list of positions, position slices

# Using the ser created above
print(ser)
# Out:
#    2020-01-02    7.16
#    2020-01-03    7.19
#    2020-01-06    7.00
#    2020-01-07    7.10
#    2020-01-08    6.86
#    2020-01-09    6.95
#    2020-01-10    7.00
#    2020-01-13    7.02
#    2020-01-14    7.11
#    2020-01-15    7.04
#    dtype: float64

# Get the first element of the series
x = ser[0]

# Get the first and fourth element (series)
x = ser[[0,3]]

# NOTE: When using slices, the endpoints are NOT included
# This will return a series with the first element only
x = ser[0:1]
print(x)

# Output:
#  2020-01-02    7.16
#  dtype: float64

# This will return the first five elements of the series
x = ser[:5]
print(x)
# Returns:
# 2020-01-02    7.16
# 2020-01-03    7.19
# 2020-01-06    7.00
# 2020-01-07    7.10
# 2020-01-08    6.86
# dtype: float64

# This will return every other element, starting at position 0
x = ser[::2]
# Out:
# 2020-01-02    7.16
# 2020-01-06    7.00
# 2020-01-08    6.86
# 2020-01-10    7.00
# 2020-01-14    7.11
# dtype: float64

# This returns the series in reverse order
x = ser[::-1]
# Out:
# 2020-01-15    7.04
# 2020-01-14    7.11
# 2020-01-13    7.02
# 2020-01-10    7.00
# 2020-01-09    6.95
# 2020-01-08    6.86
# 2020-01-07    7.10
# 2020-01-06    7.00
# 2020-01-03    7.19
# 2020-01-02    7.16
# dtype: float64

print(df)

# Output:
#             Close  Bday
# 2020-01-02   7.16     1
# 2020-01-03   7.19     2
# 2020-01-06   7.00     3
# 2020-01-07   7.10     4
# 2020-01-08   6.86     5
# 2020-01-09   6.95     6
# 2020-01-10   7.00     7
# 2020-01-13   7.02     8
# 2020-01-14   7.11     9
# 2020-01-15   7.04    10


# df[column label] --> series if column exists, error otherwise
# `x` will be a series with values in Close
# x = df['Close']
# print(x)
# Returns a series:
# Out:
# 2020-01-02    7.16
# 2020-01-03    7.19
# 2020-01-06    7.00
# 2020-01-07    7.10
# 2020-01-08    6.86
# 2020-01-09    6.95
# 2020-01-10    7.00
# 2020-01-13    7.02
# 2020-01-14    7.11
# 2020-01-15    7.04
# Name: Close, dtype: float64

# print(type(df["Close"]))
# <class 'pandas.core.series.Series'>

# Note that the label is case sensitive. For instance the following
# raises KeyError
#df['CLOSE']


new_ser = pd.Series(data=['a','b', 'c'], index=[1, -4, 10])
# This will produce an empty series (because pandas thinks these are positions, not labels)
x = new_ser[1:-4]
print(new_ser)
print(x)










#     3.2 DataFrame:
#       3.2.1 column label, list of column labels
#       3.2.2 row label slices
#       3.2.3 row position slices