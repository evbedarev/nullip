def fdate():
    import datetime
    t = datetime.datetime.now()
    sdate = str(t.year) + '-' + str('%02d'%t.month) +'-' + str('%02d'%t.day)+' '+str('%02d'%t.hour)+':'+str('%02d'%t.minute)+':'+str('%02d'%t.second)
    return sdate

