"""
Helper funcs for plotly figures
"""
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import ImageColor
from collections import defaultdict

def get_common_range(subplots, axes=["x", "y"], offset_mpl=[0,0], offset_constant=[0,0]):
    data = defaultdict(list)
    for plot in subplots.data:
        for ax, off_m, off_c in zip(axes, offset_mpl, offset_constant):          
            if hasattr(plot, f"error_{ax}") and getattr(plot, f"error_{ax}").array is not None:
                additions = [np.array([*plot[f"error_{ax}"]["array"]]), -np.array([*plot[f"error_{ax}"]["array"]])] 
            else:
                additions = [0]
            for addition in additions:
                arr = (plot[ax] + addition)[~np.isnan(plot[ax])]
                arr_min, arr_max = arr.min(), arr.max()
                data[f"{ax}-min"].append(arr_min * (1-off_m if arr_min > 0 else 1+off_m) - off_c)
                data[f"{ax}-max"].append(arr_max * (1+off_m if arr_max > 0 else 1-off_m) + off_c)
    for k, v in data.items():
        func = min if "min" in k else max
        data[k] = func(v)
    ranges = {ax: [data[f"{ax}-min"], data[f"{ax}-max"]] for ax in axes}
    return ranges

get_tickdata = lambda subplots, axes=["x","y"], size=24: {"{}axis{}_tickfont_size".format(ax, i): size for ax in axes for i in [""] + [*range(1, subplots + 1)]}
get_logaxes = lambda subplots, axes=["y"]: {"{}axis{}_type".format(ax, i): "log" for ax in axes for i in [""] + [*range(1, subplots + 1)]}
get_exponent_format = lambda subplots, axes=["y"]: {"{}axis{}_exponentformat".format(ax, i): "power" for ax in axes for i in [""] + [*range(1, subplots + 1)]}
get_logaxes_expformat = lambda subplots, axes=["y"]: {**get_logaxes(subplots, axes), **get_exponent_format(subplots,axes)}
get_range_data = lambda subplots, axes, ranges: {"{}axis{}_range".format(ax, i): r for (ax, r) in zip(axes, ranges) for i in [""] + [*range(1, subplots + 1)]}
format_data = lambda subplots, key, val, axes=["x","y"]: {"{}axis{}_{}".format(ax, i, key): val for ax in axes for i in [""] + [*range(1, subplots + 1)]}

non_visible_axes_specs = dict(visible=False, showgrid=False, zeroline=False) 
get_delete_axes = lambda subplots, axes=["x", "y"]: {f"{ax}axis{i}": non_visible_axes_specs for ax in axes for i in [""] + [*range(1, subplots + 1)]}

def get_subplots(cols, rows=1, horizontal_spacing=0.03, height=None, width=2500, ticksize=32, font_size=40, font_family="sans-serif", hovermode=False,
                 delete_axes=False,
                 **kwargs):
    height = 800*rows if height is None else height
    fig = make_subplots(figure=go.Figure(layout=dict(margin=dict(l=100, r=20, b=80, t=80, pad=1), height=height, width=width)),
                        horizontal_spacing=horizontal_spacing, rows=rows, cols=cols, **kwargs
                       )
                    
    fig.for_each_annotation(lambda a: a.update(font={'size':font_size, "family":font_family}))
    ticks_data = {'{}axis{}_tickfont_size'.format(ax, i): ticksize for ax in ["x", "y"] for i in [""] + [*range(1, (rows*cols) + 1)]}
    fig.update_layout(**ticks_data, legend_font_size=font_size, hovermode=hovermode)
    if delete_axes:
        fig.update_layout(**get_delete_axes(cols*rows), margin=dict(l=0, t=0, b=0, r=0), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig

def get_figure(height=800, width=1200, ticksize=32, font_size=40, margin=None, font_family="sans-serif", hovermode=False, delete_axes=False, **kwargs):
    fig = go.Figure(layout=dict(margin=dict(l=100, r=20, b=80, t=20, pad=1) if margin is None else margin,
                                height=height, width=width, yaxis=dict(tickfont_size=ticksize),
                                xaxis=dict(tickfont_size=ticksize), font_size=font_size, legend_font_size=font_size,
                                font_family=font_family, hovermode=hovermode,
                                **kwargs))
    if delete_axes:
        fig.update_layout(**get_delete_axes(0), margin=dict(l=0, t=0, b=0, r=0), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig

def get_alternate_dashes(reps=10):
    return ["solid", "dash", "dot"] * reps

def transparent_colorscale(fig, threshold=1e-10):
    """Values below threshold are invisible."""
    colorscale = fig.layout["coloraxis"]["colorscale"]
    low_limit = colorscale[0]
    new_low_limit = (threshold, low_limit[1])
    new_colorscale = ((0, 'rgba(0,0,0,0)'), new_low_limit, *colorscale[1:])
    return new_colorscale

def color_std(color, opacity=0.2):
    """Colors for the band y_mean +- y_std"""
    return "rgba" + str((*ImageColor.getrgb(color), opacity))