from osgeo import ogr

# open shapefile
driver = ogr.GetDriverByName("ESRI Shapefile")
ds = driver.Open("C:/Users/thinu/OneDrive/Desktop/SL_Province/SL_Province.shp", 1)
layer = ds.GetLayer()


# get a single feature
feature = layer.GetFeature(1)

# create a new attribute field
newfield = ogr.FieldDefn("Perimeter", ogr.OFTReal)
newfield.SetWidth(10)
newfield.SetPrecision(3)
layer.CreateField(newfield)

# get the perimeter of each polygon
for feature in layer:
    geom = feature.GetGeometryRef()
    perim = geom.Boundary().Length()
    feature.SetField("Perimeter", perim)
    layer.SetFeature(feature)
    

