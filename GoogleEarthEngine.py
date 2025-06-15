import ee
import geemap.core as geemap


ee.Authenticate()
ee.Initialize(project='my-project')
print(ee.String('Hello from the Earth Engine servers!').getInfo())