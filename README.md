# montecarloop
Utility library for caching and analysis of estimates from Monte Carlo simulations.

## Purpose

Monte Carlo simulations generate random samples based on some theoretical
probabilistic model. A numerical fact of the theoretical model can be estimated
from the random samples generated.

`montecarloop` provides features for two challenges with Monte Carlo estimation:

1. long computation times
2. accuracy of estimates

### Mitigating long computation times

Monte Carlo simulations often make an extreme trade-off between estimation
accuracy vs computation time. `montecarloop` can help make this trade-off less
painful, especially when doing exploratory data analysis of slow Monte Carlo
estimates within Python notebooks.

`montecarloop` can _cache_ running statistics of Monte Carlo estimates into a
file. A slow long running script can run Monte Carlo calculations independent
of Python notebooks which can read and process preliminary estimates without
being blocked.

### Evaluation of estimator accuracy

After running a large nubmer of independent Monte carlo simulations,
`montecarloop` will calculate statistics on the estimates, such as the standard
deviation of the estimates. Furthermore, if `montecarloop` is provided a
function which calculated the theoretical expected value of estimate, a p-value
from a t-test will be performed. By running simulations for long periods of
time, subtle statistical biases can potentially be found.

## Quick Start

```
python3 -m pip install git+https://github.com/NovembreLab/montecarloop.git
```

Checkout the example notebook and script at
[github.com/NovembreLab/montecarloop/example/](https://github.com/NovembreLab/montecarloop/example/).



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

