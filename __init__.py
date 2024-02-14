# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Transition
                                 A QGIS plugin
 truc
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-02-03
        copyright            : (C) 2024 by Transition
        email                : Transition
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Transition class from file Transition.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .transition_qgis import Transition
    return Transition(iface)