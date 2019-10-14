# -*- coding: utf-8 -*-

# %%

from pxr import Usd, UsdGeom, Sdf, Gf, UsdShade

USD_PATH_ROOT = "D:/usd_test"

stage = Usd.Stage.CreateInMemory()
rootLayer = stage.GetRootLayer()

sphere = UsdGeom.Sphere.Define(stage, '/test/sphere')

matPath = Sdf.Path("/Model/Material/MyMat")
mat = UsdShade.Material.Define(stage, matPath)
shader = UsdShade.Shader.Define(stage, matPath.AppendChild('testShader'))

# Shaderのアトリビュート設定
# 色をつけただけの基本のPBRシェーダーを作る
# https://graphics.pixar.com/usd/docs/UsdPreviewSurface-Proposal.html#UsdPreviewSurfaceProposal-PreviewSurface
shader.CreateIdAttr('UsdPreviewSurface')
shader.CreateInput('diffuseColor', Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f(0, 1, 0))
shader.CreateInput('metalic', Sdf.ValueTypeNames.Float).Set(0.9)
shader.CreateInput('roughness', Sdf.ValueTypeNames.Float).Set(0.2)
shader.CreateInput('opacity',Sdf.ValueTypeNames.Float).Set(0.5)
# Shaderの結果をMatにつなげる
mat.CreateSurfaceOutput().ConnectToSource(shader, "surface")

# Bind
UsdShade.MaterialBindingAPI(sphere.GetPrim()).Bind(mat)


# %%
print(stage.GetRootLayer().ExportToString())

# %%
stage.GetRootLayer().Export(USD_PATH_ROOT + "/shaderSample.usda")


#%%
