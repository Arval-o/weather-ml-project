import requests
response = requests.get("https://nomads.ncep.noaa.gov/pub/data/nccf/com/hrrr/prod/hrrr.20260416/conus/hrrr.t00z.wrfsfcf00.grib2")
print(response.status_code)
