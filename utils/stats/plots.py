"""
Stats plots (just a test)
"""
import statsmodels.api as sm
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from . import _preprocess
from utils.plots.plotly import get_figure

def qqplot(x, alpha=0.3, ms=20):
        pp = sm.ProbPlot(x, fit=True)
        qq = pp.qqplot(marker='.', markerfacecolor='k', markeredgecolor='k', alpha=alpha, markersize=ms)
        sm.qqline(qq.axes[0], line='45', fmt='k--')
        return
    
def density_kernel(*X, cov_factor=0.1, n_points=300, **kwargs):
    fig = get_figure(yaxis_title="Probability density", **kwargs)
    for x in X:
        xs, density = _preprocess.density_kernel(x, cov_factor=cov_factor, n_points=n_points)
        
        fig.add_trace(go.Scatter(x=xs, y=density, mode="lines", showlegend=False, line_width=4))
    return fig