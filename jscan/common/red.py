import numpy as np
import common.arithmetics as arith
import mysql.t_facility as fc


def predicted():
    sql = "SELECT red1, red2, red3, red4, red5, red6 from t_facility order by term DESC LIMIT 1"
    oldRed1 = fc.t_facility_sql(sql)[0][0]
    rates_red1 = arith.random_Rate("Red1")
    red1 = np.random.choice(list(rates_red1.keys()), 1, False, list(rates_red1.values()))[0]
    while abs(int(red1) - int(oldRed1)) == 0:
        red1 = np.random.choice(list(rates_red1.keys()), 1, False, list(rates_red1.values()))[0]
    return red1
