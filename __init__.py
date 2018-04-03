# -*- coding: utf-8 -*-
def classFactory(iface):
    from .natusfera_qgis_3 import NatusferaQGIS3
    return NatusferaQGIS3(iface)
