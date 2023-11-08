# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import h5py
import datetime

st_dtg=str(2020090106)
end_dtg=str(2020113018)

yr=st_dtg[0]+st_dtg[1]+st_dtg[2]+st_dtg[3]
month=st_dtg[4]+st_dtg[5]
day=st_dtg[6]+st_dtg[7]
hr=st_dtg[8]+st_dtg[9]
date = datetime.datetime(int(yr),int(month),int(day),int(hr),0,0)


count=0
while st_dtg != end_dtg:
    print(st_dtg)
    
    if count==0:    
        increment=h5py.File(('navgem_increments_T0359L060_slthin_quad_%s_000000.h5' % (st_dtg)),'r')
        ps_inc=increment['Gaussian']['ps']
        theta_inc=increment['Gaussian']['theta']
        u_inc=increment['Gaussian']['uwind']
        v_inc=increment['Gaussian']['vwind']
        hum_inc=increment['Tracers']['spchum']
        ps_avg=ps_inc[:]
        theta_avg=theta_inc[:]
        u_avg=u_inc[:]
        v_avg=v_inc[:]
        hum_avg=hum_inc[:]
        increment.close()
        count=1
    else:
        increment=h5py.File(('navgem_increments_T0359L060_slthin_quad_%s_000000.h5' % (st_dtg)),'r')
        ps_inc=increment['Gaussian']['ps']
        theta_inc=increment['Gaussian']['theta']
        u_inc=increment['Gaussian']['uwind']
        v_inc=increment['Gaussian']['vwind']
        hum_inc=increment['Tracers']['spchum']
        ps_avg=ps_avg+ps_inc[:]
        theta_avg=theta_avg+theta_inc[:]
        u_avg=u_avg+u_inc[:]
        v_avg=v_avg+v_inc[:]
        hum_avg=hum_avg+hum_inc[:]
        increment.close()
        count=count+1
        
    date += datetime.timedelta(hours=6)
    st_dtg=date.strftime("%G%m%d%H")

ps_avg=ps_avg/count
theta_avg=theta_avg/count
u_avg=u_avg/count
v_avg=v_avg/count
hum_avg=hum_avg/count
avgf=h5py.File('navgem_increments_T0359L060_slfull_quad_avg_10.h5','r+')

psavg=avgf['Gaussian']['ps']
thetaavg=avgf['Gaussian']['theta']
uavg=avgf['Gaussian']['uwind']
vavg=avgf['Gaussian']['vwind']
humavg=avgf['Tracers']['spchum']

psavg[...]=ps_avg
thetaavg[...]=theta_avg
uavg[...]=u_avg
vavg[...]=v_avg
humavg[...]=hum_avg
    
avgf.close()

print(count)
