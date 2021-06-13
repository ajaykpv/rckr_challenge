from math import radians, cos, sin, asin,pi,sqrt
import requests
import pandas as pd


radius=6371
pop_limit=int(input("Enter the Population limit: "))

#to find the distance between two points in earth (in the form of longitude and latitude in degree) using  harvesien formula

def distance(lat1,lon1,lat2,lon2):
    lon1=(lon1* pi)/180
    lon2=(lon2* pi)/180
    lat1=(lat1* pi)/180
    lat2=(lat2* pi)/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    a = (pow( sin(dlat / 2), 2) +
         pow( sin(dlon / 2), 2) *
              cos(lat1) *  cos(lat2))
    c = 2 *  asin( sqrt(a))
    return round(c*radius*100)/100

tot=0
url_d='https://cdn.jsdelivr.net/gh/apilayer/restcountries@3dc0fb110cd97bce9ddf27b3e8e1f7fbe115dc3c/src/main/resources/countriesV2.json'

res=requests.get(url_d).json()

df=pd.DataFrame(res)

sorted_df=df.sort_values(by='population')

ll=[]
i=0
for index, row in sorted_df.iterrows():
    
    if row['population'] >= pop_limit:
        try:
            
            lat, lng = row['latlng'][:]
            s=[lat,lng]
            ll.append(s)
            i+=1
        except Exception:
            lng = lat = 0
            s=[lat,lng]
            ll.append(s)
            i+=1
    if i>20:
        break


for i in range(0,20):
    for j in range(i+1,20):
        tot+=distance(ll[i][0],ll[i][1],ll[j][0],ll[j][1])

tot=round(tot*100)/100
print('%.2f'%tot)



