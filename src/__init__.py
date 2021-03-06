# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeometryCopier
                                 A QGIS plugin
 Help to copy geometry in layers
                             -------------------
        begin                : 2013-03-22
        copyright            : (C) 2013 by Nikulin Evgeniy
        email                : nikulin.e at gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def classFactory(iface):
    # load GeometryCopier class from file GeometryCopier
    from geometry_copier import GeometryCopier
    return GeometryCopier(iface)
