from pandas import Series


def salary_to_cat(salary_series: Series, boundary: dict) -> list:
    """Convert salary from numerical feature to categorical feature

    Args:
        - salary
        - boundary: key-value pair where the value is the min-max rule
            of each key.
            example - {
                "low": {"min": 20_000},
                "mid-low": {"min": 20_000, "max": 25_000}
            }
    """
    result = []
    series_gen = salary_series.iterrows()
    for _, value in series_gen:
        salary = value.values[0]
        salary_cat = None
        for cat, rule in boundary.items():
            min_rule = rule.get("min")
            max_rule = rule.get("max")
            if not max_rule and salary < min_rule:  # lowest salary
                salary_cat = cat
            elif not min_rule and salary > max_rule:  # highest salary
                salary_cat = cat
            elif (
                min_rule and
                max_rule and
                min_rule <= salary <= max_rule
            ):  # mid-low/mid-high
                salary_cat = cat
            if salary_cat:
                result.append(salary_cat)
                break
    return result


def credit_to_cat(credit_series: Series, boundary: dict) -> list:
    """Convert credit from numerical feature to categorical feature

    Args:
        - credit
        - boundary: key-value pair where the value is the min-max rule of
            each key.
            example - {
                "low": {"min": 20_000},
                "mid-low": {"min": 20_000, "max": 25_000}
            }
    """
    result = []
    series_gen = credit_series.iterrows()
    for _, value in series_gen:
        credit = value.values[0]
        credit_cat = None
        for cat, rule in boundary.items():
            min_rule = rule.get("min")
            max_rule = rule.get("max")
            if credit == 0:
                credit_cat = 0
            elif not max_rule and credit < min_rule:  # lowest salary
                credit_cat = cat
            elif not min_rule and credit > max_rule:  # highest salary
                credit_cat = cat
            elif (
                min_rule and
                max_rule and
                min_rule <= credit <= max_rule
            ):  # mid-low/mid-high
                credit_cat = cat

            if credit_cat is not None:
                result.append(credit_cat)
                break
    return result
