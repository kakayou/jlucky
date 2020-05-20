import wbw.crawler as crawler
import mysql.luckydb as db

start = "00001"
end = crawler.latest_term()
print(end)
term = db.t_facility_max_term()
print(term[0])
if int(end) > term[0]:
    start = term[0]
    data = crawler.crawler_data(str(start+1), end)
    print(data)
    db.t_facility_insert(data)

