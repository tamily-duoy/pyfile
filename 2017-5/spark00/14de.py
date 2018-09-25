#!/usr/bin/python
# -*- coding:utf-8 -*-


import shapefile
#读Shapefiles
sf = shapefile.Reader("C:\\Users\\Administrator\\Desktop\\spark\\数据集\\gtwo\\gtwo_areas_201608062356.shp")
# myshp = open("shapefiles/blockgroups.shp", "rb") #可以读url,zip, database
# r = shapefile.Reader(shp=myshp, dbf=mydbf)

shapes = sf.shapes() #返回 list
print(len(shapes))   #==3
print(len(list(sf.iterShapes())))  #==3
"''bbox' 'parts' 'points' 'shapeType''"
print(shapes[2].shapeType)   #==5
bbox = shapes[2].bbox  # 若shape type 的 multiple points,tuple describes
c=['%.3f' % coord for coord in bbox]
print(c)  # ['-111.415', '16.673', '-102.747', '23.468']
print(shapes[2].parts)    #[0]:only one part
print(len(shapes[2].points))
shape = shapes[1].points[7]  ## Get the 8th point of the 3th shape
c=['%.3f' % coord for coord in shape] ## Truncate coordinates to 3 decimal places
print(c)  #['-110.023', '19.533']
s = sf.shape(1)
c=['%.3f' % coord for coord in s.bbox]
print(c)
