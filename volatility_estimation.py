import pandas as pd
import numpy as np

def estimate_volatility(prices, l):
    """Create an exponential moving average model of the volatility of a stock
    price, and return the most recent (last) volatility estimate.
    
    Parameters
    ----------
    prices : pandas.Series
        A series of adjusted closing prices for a stock.
        
    l : float
        The 'lambda' parameter of the exponential moving average model. Making
        this value smaller will cause the model to weight older terms less 
        relative to more recent terms.
        
    Returns
    -------
    last_vol : float
        The last element of your exponential moving averge volatility model series.
    
    """
    # TODO: Implement the exponential moving average volatility model and return the last value.
    
    # let's compute the returns
    returns = np.log(prices / prices.shift(1))

    # Udacity helper is telling us to use .ewm from pandas. 
    # Documentation is : https://pandas.pydata.org/pandas-docs/stable/user_guide/computation.html
    # Reading the documentation we realise that the weight there is (1 - alpha) for us this is l
    # 1 - alpha = l ; alpha = 1 - l - this is the parameter we need to pass to the function

    weighted_average_returns = returns.ewm(com=1-l).std()

    return weighted_average_returns[-1]

def test_run(filename='data.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'], index_col='date', squeeze=True)
    print("Most recent volatility estimate: {:.6f}".format(estimate_volatility(prices, 0.7)))

filename = 'data.csv'
test_run(filename)