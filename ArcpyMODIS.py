# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:48:48 2019

@author: LBN
"""

#to tif---extract subdataset
import arcpy

arcpy.CheckOutExtension("Spatial")

inDir="D:/MOD15"
outDir="D:/MOD15V1"

arcpy.env.workspace=inDir
rasters=arcpy.ListRasters("*","hdf")

for raster in rasters:
    print(raster)
    outName=outDir+"\\"+raster[10:24]+".tif"
    arcpy.ExtractSubDataset_management(raster,outName,"0")
    print(outName)





#mosaic---mosaic to new raster
import os
import arcpy

inDir="D:/MOD15V1"
outDir="D:/MOD15V2"

for year in range(2022,2023):
    print(year)  
    for eday in range(181,274,4):
        filename1=inDir+'\\'+str(year)+str(eday)+'.h27v05'+'.tif'
        filename2=inDir+'\\'+str(year)+str(eday)+'.h27v06'+'.tif'
        filename3=inDir+'\\'+str(year)+str(eday)+'.h28v05'+'.tif'
        filename4=inDir+'\\'+str(year)+str(eday)+'.h28v06'+'.tif'
        expression=filename1+';'+filename2+';'+filename3+';'+filename4
        outName=str(year)+str(eday)+'_mosaic.tif'
        print(expression)
        arcpy.MosaicToNewRaster_management(expression,outDir,outName,"#","8_BIT_UNSIGNED", "#", "1", "#","#") 
        print(outName)

 


        
#reproject---project raster
import arcpy

inDir="D:/MOD15V2"
outDir="D:/MOD15V3"

arcpy.CheckOutExtension("spatial")

arcpy.env.workspace=inDir
rasters=arcpy.ListRasters("*","tif")

for raster in rasters:
    print(raster)
    outName=outDir+'\\'+raster[0:7]+'_Reproject.tif'
    print(outName)
    projecttype = "D:/rice/shp/Export_Output_wgs84.prj"
    arcpy.ProjectRaster_management(raster, outName, projecttype, "BILINEAR", "#","#", "#", "#")
print("OK")


        
#extract---extract by mask
import arcpy
arcpy.CheckOutExtension("spatial")
inDir="D:/MOD15V3"
outDir="D:/MOD15V4"
arcpy.gp.overwriteOutput=1
arcpy.env.workspace = inDir
rasters = arcpy.ListRasters("*", "tif")
mask = "D:/rice/shp/Export_Output_wgs84.shp"
for raster in rasters:
    print(raster)
    outName= outDir+'\\'+raster[0:7]+'_extrac.tif'
    print(outName)
    arcpy.gp.ExtractByMask_sa(raster, mask, outName)
print("OK")