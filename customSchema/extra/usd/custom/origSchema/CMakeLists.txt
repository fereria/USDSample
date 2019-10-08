set(PXR_PACKAGE origSchema)

pxr_plugin(${PXR_PACKAGE}
    LIBRARIES
        tf
        sdf
        usd
        vt

    INCLUDE_DIRS
        ${Boost_INCLUDE_DIRS}
        ${PYTHON_INCLUDE_DIRS}

    PUBLIC_HEADERS
        api.h

    PUBLIC_CLASSES
        tokens
        sampleBase
        concreteBasePrim

    PYTHON_CPPFILES
        moduleDeps.cpp

    PYMODULE_FILES
        __init__.py

    PYMODULE_CPPFILES
        module.cpp
        wrapTokens.cpp
        wrapConcreteBasePrim.cpp
        wrapSampleBase.cpp

    RESOURCE_FILES
        generatedSchema.usda
        plugInfo.json
        schema.usda:schema.usda
)