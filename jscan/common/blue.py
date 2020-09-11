import numpy as np
import common.arithmetics as arith
import mysql.t_facility as fc

def predicted():
    sql = "SELECT red1, red2, red3, red4, red5, red6, blue from t_facility order by term DESC LIMIT 1"
    oldBlue = fc.t_facility_sql(sql)[0][6]
    rates_blue = arith.random_Rate("blue")
    blue = np.random.choice(list(rates_blue.keys()), 1, False, list(rates_blue.values()))[0]
    while abs(int(blue)-int(oldBlue))<2:
        blue = np.random.choice(list(rates_blue.keys()), 1, True, list(rates_blue.values()))[0]
    return blue

