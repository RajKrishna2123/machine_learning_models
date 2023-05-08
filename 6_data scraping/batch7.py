import wget
year=int(input("enter the yr"))
month=['JUL','AUG','SEP','OCT','NOV','DEC']



l=["1800","1830","1900","1930","2000","2030"]



days=["01","02","03","04","05","06","07","08","09","10",
      "11","12","13","14","15","16","17","18","19","20",
      "21","22","23","24","25","26","27","28","29","30"]


for i in month:
    for j in days:
        for k in l:
            try:
                url = "http://satellite.imd.gov.in/ImageArchive/3DIMG/{}/{}/3DIMG_{}{}{}_{}_L1C_ASIA_WV_TEMP_V01R00.jpg".format(year,i,j,i,year,k)
                file_name = wget.download(url)
                print('Image Successfully Downloaded: ', file_name)
            except:
                print("not present")
