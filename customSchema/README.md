# カスタムスキーマサンプル

詳細は  
https://fereria.github.io/reincarnation_tech/11_Pipeline/USD/Tips/00_create_custom_schema/  
こちらにて解説。  
  
USDのリポジトリに対してこの extra以下をコピーし、ビルドを実行すると  
plugin/usd 以下に origSchema.lib origSchema.dll origSchemaフォルダ  
lib/python/pxr 下に OrigSchema が作成されます。  
  
```python
from pxr import Usd, UsdGeom, Sdf, Gf, OrigSchema

stage = Usd.Stage.CreateInMemory()
hogePrim = OrigSchema.ConcreteBasePrim.Define(stage,'/hoge')
stage.GetRootLayer().Export("I:/test.usda")
```

作成したスキーマは、このように使用することができます。  
