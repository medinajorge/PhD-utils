# PhD-utils

For people that have to compute and store a large variety of data and/or perform statistical inference.

## Keep your files tidy!

Don't spend time creating directories, deciding filenames, saving, loading, etc. Decorators `savefig` & `savedata` will do it for you with optimal compression. More info at the `tidypath` [repository](https://github.com/medinajorge/tidypath).

## Estimate confidence intervals
The module `utils.resample` allows calls to the `resample` [R package](https://cran.r-project.org/web/packages/resample/resample.pdf).
- Provides CI and permutation tests.
- CIs can account narrowness bias, skewness and other errors in CI estimation, as indicated in the [article](https://arxiv.org/abs/1411.5279)

## Numba-accelerated permutation tests
Subpackage `utils.stats.tests.permutation`. 
- Permutation tests for any statistic. 
- Includes paired and block-paired cases.

## Demo
Please check the [example notebook](https://github.com/medinajorge/PhD-utils/blob/master/tests/Example.ipynb).

## Documentation
[Github pages](https://medinajorge.github.io/PhD-utils/phdu.html)

## Install
- For the R compatible installation first install R:

  ```conda install -c conda-forge r r-essentials r-base```
  
- Install with dependencies:

  ```pip install phdu[dependencies]```
  
  Where `dependencies` can be `base` (recommended), `all`, `r` (needed for `resample` to work), `statsmodels`, `matplotlib` or `plotly`.
