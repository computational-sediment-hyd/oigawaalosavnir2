
# coding: utf-8

# In[ ]:


import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import pandas as pd
import hvplot.xarray
# import hvplot.pandas
import geoviews as gv
import holoviews as hv

gv.extension('bokeh', logo=False)
hv.extension('bokeh', logo=False)
renderer = hv.Store.renderers['bokeh'].instance(mode='server', holomap='server')


# In[ ]:


ds = xr.open_dataset('data/rgb.nc')
# ds = ds.isel(time=slice(0,2))


# In[ ]:


# def parser(date):
#     b = date.split(' ')
#     c = b[1].split(':')
#     return pd.datetime.strptime(b[0],'%Y/%m/%d') + pd.Timedelta(hours=int(c[0]), minutes=int(c[1])) 

# f = r'data/kanza_Q.csv'
# dfQ = pd.read_csv(f, engine='python', index_col=0, parse_dates=True, header=None, date_parser=parser)
# dfQ.columns = ['kanza_Q']
# dfQ.index.name='time'
# dfQ = dfQ.replace(-9999, np.nan)

# gQ = dfQ.hvplot(width=700)

# t = ds.time.values
# timeUTC = pd.to_datetime(t, utc=True).tz_convert('Asia/Tokyo').round('1H')

# Qp = []
# for time in pd.to_datetime( timeUTC.tz_localize(None) ):
#     Qp.append( dfQ[ dfQ.index==time ].kanza_Q.values[0] )
    
# dsQ = xr.Dataset({'kanza_Q': (['time'], np.array(Qp))}, coords={'time': ds['time'].values } )
# gp = dsQ.hvplot.scatter('time','kanza_Q', groupby='time', legend=False, color='red', size=100)


# In[ ]:


outcrs = ccrs.epsg(6676)
url = 'https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{Z}/{X}/{Y}.jpg'
geomap = gv.WMTS(url, crs=outcrs)
# fig = (geomap * ds.hvplot.rgb('x','y', z='z',bands='band',groupby='time', width=700, height=500) + gQ * gp).cols(1)
fig = geomap * ds.hvplot.rgb('x','y', z='z',bands='band',groupby='time', width=700, height=500) 
doc,_ = renderer(fig)
doc.title = "Oigawa_Visualized_by_Alos-Avnir2"

