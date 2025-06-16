import ee
import geemap.core as geemap


ee.Authenticate()
ee.Initialize(project='iconic-guard-454717-v9')
print(ee.String('Hello from the Earth Engine servers!').getInfo())

