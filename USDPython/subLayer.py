# -*- coding: utf-8 -*-
"""
subLayerで合成する
"""

# %%

from pxr import Usd, UsdGeom, Sdf, Gf

USD_PATH_ROOT = "I:/usd_test"
kitchenSetRoot = USD_PATH_ROOT + "/Kitchen_set/assets/"

stage = Usd.Stage.CreateInMemory()
rootLayer = stage.GetRootLayer()

rootLayer.subLayerPaths = [kitchenSetRoot + "/Book/Book.usd", kitchenSetRoot + "/Ball/Ball.usd"]

bookPath = Sdf.Path("/Book")
bookPrim = stage.GetPrimAtPath(bookPath)
UsdGeom.XformCommonAPI(bookPrim).SetTranslate((0, 50, 0))


# %%
print(stage.GetRootLayer().ExportToString())
# %%
stage.GetRootLayer().Export(USD_PATH_ROOT + "/subLayerTest.usda")
# %%
