import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # TODO: Fill in this function.
    price_resh = prices.pivot(index='date', columns='ticker', values='price')

    returns = np.log(price_resh / price_resh.shift(1))
    volatility = returns.std(axis=0)

    pos_Highest = np.where(volatility == np.amax(volatility, axis=0))

    return returns.columns[pos_Highest]
    

prices = pd.read_csv('prices2.csv', parse_dates=['date'])
print(get_most_volatile(prices))
