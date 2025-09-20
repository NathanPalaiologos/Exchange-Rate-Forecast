library(tidyverse)
library(lubridate)
library(cansim)

get_exchange_rate_data <- function(start_date = "2000-01-01", 
                                   currency = "Chinese renminbi, daily average") 
{
    # Obtain exchange rate data from CANSIM
    exchange_rate <- cansim::get_cansim("33-10-0036-01") |>
        filter(Date >= start_date) |>
        filter(`Type of currency` == currency) |>
        filter(VALUE != 0.00)

    df <- exchange_rate |>
        select(Date, VALUE) |>
        rename(date = Date, exchange_rate = VALUE) |>
        arrange(date)

    # Return the cleaned data frame
    return(df)
}