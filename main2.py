
# coding: utf-8

# In[ ]:


import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import pandas as pd
import hvplot.xarray
import hvplot.pandas
import geoviews as gv
import holoviews as hv

gv.extension('bokeh', logo=False)
hv.extension('bokeh', logo=False)
renderer = hv.Store.renderers['bokeh'].instance(mode='server', holomap='server')


# In[ ]:


ds = xr.open_dataset('data/rgb.nc')
# ds = ds.isel(time=slice(0,2))


# In[ ]:


outcrs = ccrs.epsg(6676)
url = 'https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{Z}/{X}/{Y}.jpg'
geomap = gv.WMTS(url, crs=outcrs)


# In[ ]:


timeUTC = pd.to_datetime(ds.time.values, utc=True).tz_convert('Asia/Tokyo').round('1H')
fnames = timeUTC.strftime('%Y/%m/%d %H:%M')
l = []
for i in range(len(ds.time.values)):
    tmp = geomap * ds.isel(time=i).hvplot.rgb('x','y', z='z',bands='band', width=350, height=350, title=fnames[i]) 
    l.append(tmp)
    
fig = hv.Layout(l)
doc,_ = renderer(fig)
doc.title = "Oigawa_Visualized_by_Alos-Avnir2"

