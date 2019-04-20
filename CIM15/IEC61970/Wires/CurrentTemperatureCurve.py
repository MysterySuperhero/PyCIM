# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Core.Curve import Curve


class CurrentTemperatureCurve(Curve):
    def __init__(self, ACLineSegments=None, *args, **kw_args):
        """Initialises a new 'CurrentTemperatureCurve' instance.

        @param ACLineSegments: ACLineSegments using this curve.
        """

        self._ACLineSegments = []
        self.ACLineSegments = [] if ACLineSegments is None else ACLineSegments

        super(CurrentTemperatureCurve, self).__init__(*args, **kw_args)

    _attrs = ["hydrogenPressure", "coolantTemperature"]
    _attr_types = {"hydrogenPressure": float, "coolantTemperature": float}
    _defaults = {"hydrogenPressure": 0.0, "coolantTemperature": 0.0}
    _enums = {}
    _refs = ["ACLineSegments"]
    _many_refs = ["ACLineSegments"]

    def getACLineSegments(self):
        return self._ACLineSegments

    def setACLineSegments(self, value):
        for p in self._ACLineSegments:
            filtered = [q for q in p.CurrentTemperatureCurves if q != self]
            self._ACLineSegments._CurrentTemperatureCurves = filtered
        for r in value:
            if self not in r._CurrentTemperatureCurves:
                r._CurrentTemperatureCurves.append(self)
        self._ACLineSegments = value

    ACLineSegments = property(getACLineSegments, setACLineSegments)

    def addACLineSegments(self, *ACLineSegments):
        for obj in ACLineSegments:
            if self not in obj._CurrentTemperatureCurves:
                obj._CurrentTemperatureCurves.append(self)
            self._ACLineSegments.append(obj)

    def removeACLineSegments(self, *ACLineSegments):
        for obj in ACLineSegments:
            if self in obj._CurrentTemperatureCurves:
                obj._CurrentTemperatureCurves.remove(self)
            self._ACLineSegments.remove(obj)
