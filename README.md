# montecarloop
Utility library for caching and analysis of estimates from Monte Carlo simulations.

## Columns of data table returned by `Dealer.summary()`

* `stat`: the name of the statistic returned by monte carlo simulation estimator
* `num`: number of monte carlo estimates calculated
* `mean`: the average value of the `num` estimates calculated
* `std_dev`: the standard deviation of the `num` estimates calculated
* `std_err`: the estimated standard deviation of an average of `num` random estimates
* @_..._: parameters passed to the monte carlo simulation estimator

### if `Dealer.summary(theoretical_calc)` called with a parameter

* `null_hypo`: the null hypothesis estimate returned by `theoretical_calc`
* `pvalue`: the p-value from a two-tailed t-test

