import wbw.crawler as crawler
import mysql.luckydb as db

start = "00001"
end = crawler.latest_term()
term = db.t_facility_max_term()
if len(term) > 0 & end > term[0]:
    start = term[0]
    data = crawler.crawler_data(start,end)
    db.t_facility_insert(data)

