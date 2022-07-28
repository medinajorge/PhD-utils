import statsmodels.stats.api as sms

def t_interval(x, alpha=0.05, alternative="two-sided"):
    return sms.DescrStatsW(x).tconfint_mean(alpha=alpha, alternative=alternative)