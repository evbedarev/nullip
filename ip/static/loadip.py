class load_ip(object):
    def __init__(self, net, minip, maxip):
        """В этом классе обращаемся к классу PingNet(пингует заданную сети и возвращает список),
            передаем ему параметры сети, и заносим полученные результаты в таблицу ip_consume
        """
        import Pingn, tdate
        import sqlite3

        nw = Pingn.PingNet(net, minip, maxip)
        ipaddr = nw.printIp()

        con = sqlite3.connect("/home/admin/google/Projects/django/nullip/db.sqlite3")
        cur = con.cursor()
        for i in ipaddr:
            if i[1] == 0:
                cur.execute(
                    "DELETE from ip_consume where ip like \'{}\'".format(i[0])
                )
                con.commit()
            else:
                cur.execute(
                    "insert into ip_consume (ip,status,intstates,dt) VALUES(\'{}\',\'offline\',{},\'{}\')".format(i[0],
                                                                                                                  i[1],
                                                                                                                  tdate.fdate())
                )
                con.commit()
        cur.close()

    def sql_ins(self):

        import sqlite3

        con = sqlite3.connect("/home/admin/google/Projects/django/nullip/db.sqlite3")
        cur = con.cursor()

        cur.execute(
            """
                DELETE FROM ip_post
            """
        )
        con.commit()

        cur.execute(
            """
            INSERT INTO ip_post (ip,status,intstates,dt)
            select ip,status,sum(intstates),max(dt) from ip_consume
            group by ip,status,intstates
            order by intstates
            """
        )
        con.commit()
