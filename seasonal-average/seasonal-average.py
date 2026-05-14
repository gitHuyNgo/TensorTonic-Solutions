def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    # Write code here
    season_averages = []

    for i in range(period):
        values = series[i::period]
        avg = sum(values) / len(values)
        season_averages.append(avg)

    return season_averages