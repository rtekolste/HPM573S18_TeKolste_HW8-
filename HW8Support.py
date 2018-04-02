import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat

def print_outcomes(multi_cohort, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of patient survival time
    survival_mean_PI_text = Format.format_estimate_interval(
        estimate=multi_cohort.get_mean_total_reward,
        interval=multi_cohort.get_PI_total_reward(alpha=.05),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean survival time (years) and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          survival_mean_PI_text)


def print_comparative_outcomes(multi_cohort_odds1, multi_cohort_odds2):
    """ prints expected and percentage increase in average survival time when drug is available
    :param multi_cohort_no_drug: multiple cohorts simulated when drug is not available
    :param multi_cohort_with_drug: multiple cohorts simulated when drug is available
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Difference in Earnings',
        x=multi_cohort_odds2.get_mean_total_reward(),
        y_ref=multi_cohort_odds1.get_mean_total_reward()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI_total_reward(alpha=.05),
        deci=1
    )
    print("Expected increase earnings and {:.{prec}%} prediction interval:".format(.95, prec=0),
          estimate_CI)

    # % increase in mean survival time
    relative_diff = Stat.RelativeDifferenceIndp(
        name='% increase in earnings',
        x=multi_cohort_odds2.get_mean_total_reward(),
        y_ref=multi_cohort_odds1.get_mean_total_reward()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=relative_diff.get_mean(),
        interval=relative_diff.get_PI(alpha=.05),
        deci=1,
        form=Format.FormatNumber.PERCENTAGE
    )
    print("Expected percentage increase in earnings and {:.{prec}%} confidence interval:".format(.95, prec=0),
          estimate_CI)
