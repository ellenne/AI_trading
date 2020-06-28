import pandas as pd
import numpy as np
import scipy.stats as stats

def analyze_returns(net_returns):
    """
    Perform a t-test, with the null hypothesis being that the mean return is zero.
    
    Parameters
    ----------
    net_returns : Pandas Series
        A Pandas Series for each date
    
    Returns
    -------
    t_value
        t-statistic from t-test
    p_value
        Corresponding p-value
    """
    # TODO: Perform one-tailed t-test on net_returns
    # Hint: You can use stats.ttest_1samp() to perform the test.
    #       However, this performs a two-tailed t-test.
    #       You'll need to divide the p-value by 2 to get the results 
    #       of a one-tailed p-value.
    n = net_returns.size
    
    x_bar = net_returns.mean()
    
    s = 0
    
    for i in net_returns.tolist():
        s += (i - x_bar) ** 2
        
    s = np.sqrt(s / (n - 1))
    
    s_xbar = s / np.sqrt(n)
    
    t = x_bar / s_xbar
    
    pval = stats.t.sf(np.abs(t), n-1)
    
    return t, pval
    
def test_run(filename='net_returns.csv'):
    """Test run analyze_returns() with net strategy returns from a file."""
    net_returns = pd.Series.from_csv(filename, header=0)
    t, p = analyze_returns(net_returns)
    print("t-statistic: {:.3f}\np-value: {:.6f}".format(t, p))


if __name__ == '__main__':
    test_run()