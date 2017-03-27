import loadip
a = loadip.load_ip('172.29.96.', 1, 253)
a = loadip.load_ip('172.29.97.', 0, 253)
a = loadip.load_ip('172.29.98.', 0, 253)
a = loadip.load_ip('172.29.99.', 0, 253)
a.sql_ins()


# import Pingn, tdate
# import sqlite3
#
# nw = Pingn.PingNet('172.29.96.', 5, 10)
# ipaddr = nw.printIp()
#
# con = sqlite3.connect("/home/admin/google/Projects/django/nullip/db.sqlite3")
# cur = con.cursor()
# for i in ipaddr:
#   if i[1] == 0:
#     cur.execute(
#       "DELETE from ip_consume where ip like \'{}\'".format(i[0])
#     )
#     con.commit()
#   else:
#     cur.execute(
#       "insert into ip_consume (ip,status,intstates,dt) VALUES(\'{}\',\'offline\',{},\'{}\')".format(i[0], i[1], tdate.fdate())
#     )
#     con.commit()
#
# cur.execute(
#   """
#   INSERT INTO ip_post (ip,status,intstates,dt)
#   select ip,status,sum(intstates),max(dt) from ip_consume
#   group by ip,status,intstates
#   """
#   )
# con.commit()
#
#
# # import datetime
# # a = PingNet("172.29.96.", 1, 2)
# # a.printIp()
# #
# # t = datetime.datetime.now()
# # print(str(t.year) + '-' + str('%02d'%t.month) +'-' + str('%02d'%t.day))
#
#
#
# """
# import sqlite3
# text = ''
# con = sqlite3.connect("/home/admin/google/Projects/django/nullip/db.sqlite3")
# cur = con.cursor()
# for i in
# cur.execute(
#         "DELETE from ip_post where ip like \'{}\'".format(value)
# )
# con.commit()
# for i in range(1, 255):
#     text = "10.247.104.{0}".format(str(i))
#     cur.execute(
#         "INSERT INTO ip_post (id,ip,status,intstates,dt) VALUES(NULL,\'{}\',\'online\',\'2\',\'2017-03-16 22:22:22\')".format(text))
#     con.commit()
# """