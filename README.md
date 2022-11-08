# PhD-utils

For people that have to compute and store a large variety of data and/or perform statistical inference.

## Keep your files tidy!

Don't spend time creating directories, deciding filenames, saving, loading, etc. Decorators `savefig` & `savedata` will do it for you with optimal compression. More info at the `tidypath` repo: https://github.com/medinajorge/tidypath

## Estimate confidence intervals
The subpackage `utils.stats.rtopy.resample` allows calls to the `resample` [R package](https://cran.r-project.org/web/packages/resample/resample.pdf).
- Provides CI and permutation tests.
- CIs can account narrowness bias, skewness and other errors in CI estimation, as indicated in the [article](https://arxiv.org/abs/1411.5279)

## Numba-accelerated permutation tests
Subpackage `utils.stats.tests.permutation`. 
- Faster permutation tests for the means and medians. Includes paired case.
- Scheme for adding other statistics in a numba-compatible way (`_permutation_test_2sample_paired` and `_permutation_test_2sample_not_paired` functions)

## Example
Please check `Example.ipynb`
