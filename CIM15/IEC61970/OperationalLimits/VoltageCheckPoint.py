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

from CIM15.IEC61970.OperationalLimits.CheckPoint import CheckPoint


class VoltageCheckPoint(CheckPoint):
    """TODO.
    """

    def __init__(self, LowerLimitsCurve=None, UpperLimitsCurve=None, VoltageLimitSet=None, *args, **kw_args):
        """Initialises a new 'VoltageCheckPoint' instance.
        """

        self._LowerLimitsCurve = LowerLimitsCurve

        self._UpperLimitsCurve = UpperLimitsCurve

        self._VoltageLimitSet = VoltageLimitSet

        super(VoltageCheckPoint, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["LowerLimitsCurve", "UpperLimitsCurve", "VoltageLimitSet"]
    _many_refs = []

    def getLowerLimitsCurve(self):
        return self._LowerLimitsCurve

    def setLowerLimitsCurve(self, value):
        self._LowerLimitsCurve = value

    LowerLimitsCurve = property(getLowerLimitsCurve, setLowerLimitsCurve)

    def getUpperLimitsCurve(self):
        return self._UpperLimitsCurve

    def setUpperLimitsCurve(self, value):
        self._UpperLimitsCurve = value

    UpperLimitsCurve = property(getUpperLimitsCurve, setUpperLimitsCurve)

    def getVoltageLimitSet(self):
        return self._VoltageLimitSet

    def setVoltageLimitSet(self, value):
        self._VoltageLimitSet = value

    VoltageLimitSet = property(getVoltageLimitSet, setVoltageLimitSet)
