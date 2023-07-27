import math


from plxscripting.easy import *

input_port_i = '10000'
input_port_o = '10001'
input_password = 'MfDgR%~%4~?>rSiG'  # PUT YOUR PLAXIS 3D INPUT PASSWORD HERE
save_path = r'C:\Users\TUF\Desktop'
s_i, g_i = new_server('localhost', 10000, password='MfDgR%~%4~?>rSiG')
s_i.new()
material1 = g_i.soilmat()
material1.setproperties(
    "MaterialName", "Subgrade",
    "Colour", 1602002,
    "SoilModel", 1,
    "gammaUnsat", 18.2,
    "gammaSat", 18.2,
    "nu", 0.35,
    "cref", 0,
    "phi", 0,
    "RayleighBeta", 0,
    "Eref", 50000)

material2 = g_i.soilmat()
material2.setproperties(
    "MaterialName", "Base",
    "Colour", 9079434,
    "SoilModel", 1,
    "gammaUnsat", 22.27,
    "gammaSat", 22.27,
    "nu", 0.35,
    "cref", 0,
    "phi", 0,
    "RayleighBeta", 0,
    "Eref", 102180)

g_i.surface(-11.5, -10, -5, 11.5, -10, -5, 4, -10, -0.5, -4, -10, -0.5, )
g_i.extrude((g_i.Polygon_1), 0, 20, 0)

g_i.setmaterial(g_i.Soil_1, material1)

g_i.surface(3, -2, -0.5, 2.5, -2, 0, 2, -2, 0, 2, -2, -0.175, -2, -2, -0.175, -2, -2, 0, -2.5, -2, 0, -3, -2, -0.5,)
g_i.extrude((g_i.Polygon_2), 0, 4, 0)
g_i.extrude((g_i.Polygon_2), 0, -8, 0)
g_i.setmaterial(g_i.Soil_2, material1)
g_i.setmaterial(g_i.Soil_3, material1)

g_i.surface(3, 2, -0.5, 2.5, 2, 0, 2, 2, 0, 2, 2, -0.175, -2, 2, -0.175, -2, 2, 0, -2.5, 2, 0, -3, 2, -0.5,)
g_i.extrude((g_i.Polygon_3), 0, 8, 0)
g_i.setmaterial(g_i.Soil_4, material1)

g_i.surface(2, -2, 0, 2, -2, -0.175, -2, -2, -0.175, -2, -2, 0,)
g_i.extrude((g_i.Polygon_4), 0, 4, 0)
g_i.extrude((g_i.Polygon_4), 0, -8, 0)
g_i.setmaterial(g_i.Soil_5, material2)
g_i.setmaterial(g_i.Soil_6, material2)
g_i.surface(2, 2, 0, 2, 2, -0.175, -2, 2, -0.175, -2, 2, 0,)
g_i.extrude((g_i.Polygon_5), 0, 8, 0)
g_i.setmaterial(g_i.Soil_7, material2)
g_i.delete(g_i.Polygon_3)
g_i.delete(g_i.Polygon_1)
g_i.delete(g_i.Polygon_2)
g_i.delete(g_i.Polygon_4)
g_i.delete(g_i.Polygon_5)

material3 = g_i.geogridmat()
material3.setproperties(
    "MaterialName", "Biaxial",
    "Colour", 16711680,
    "MaterialNumber" , 0,
    "Elasticity", 0,
    "IsIsotropic", True,
    "EA1", 500,
    "EA2", 500,
    "GA", 250,)

g_i.geogrid((2, -10, -0.04375), (-2, -10, -0.04375), (-2, -2, -0.04375), (2, -2, -0.04375))
g_i.geogrid((2, -2, -0.04375), (-2, -2, -0.04375), (-2, 2, -0.04375),(2, 2, -0.04375))
g_i.geogrid((2, 10, -0.04375), (-2, 10, -0.04375), (-2, 2, -0.04375),(2, 2, -0.04375))
g_i.setmaterial(g_i.geogrid_1, material3)
g_i.setmaterial(g_i.geogrid_2, material3)
g_i.setmaterial(g_i.geogrid_3, material3)

g_i.gotomesh()
g_i.Volume_1_1.CoarsenessFactor = 1 #basesoil
g_i.Volume_2_1.CoarsenessFactor = 0.1 #subgrade_start
g_i.Volume_3_1.CoarsenessFactor = 0.1 #subgrade_mid
g_i.Volume_4_1.CoarsenessFactor = 0.1 #subgrade_end
g_i.Volume_5_1.CoarsenessFactor = 0.3 #base_start_up
g_i.Volume_5_2.CoarsenessFactor = 0.3 #base_start_down
g_i.Volume_6_1.CoarsenessFactor = 0.1 #base_mid_up
g_i.Volume_6_2.CoarsenessFactor = 0.1 #base_mid_down
g_i.Volume_7_1.CoarsenessFactor = 0.3 #base_end_up
g_i.Volume_7_2.CoarsenessFactor = 0.3 #base_end_down
g_i.Polygon_1_1.CoarsenessFactor = 0.3 #geogrid_start
g_i.Polygon_2_1.CoarsenessFactor = 0.1 #geogrid_mid
g_i.Polygon_3_1.CoarsenessFactor = 0.3 #geogrid_end

g_i.mesh( "UseEnhancedRefinements", True, "EMRGlobalScale", 1.2, "EMRMinElementSize", 0.005,"UseSweptMeshing", True)






