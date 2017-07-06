"""!

@brief Unit-tests for pyclustering package that is used for exchange between ccore library and python code.

@authors Andrei Novikov (pyclustering@yandex.ru)
@date 2014-2017
@copyright GNU Public License

@cond GNU_PUBLIC_LICENSE
    PyClustering is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    PyClustering is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
@endcond

"""


import unittest;


from pyclustering.core.pyclustering_package import package_builder, package_extractor;
from ctypes import c_ulong, c_size_t, c_double, c_uint


class Test(unittest.TestCase):
    def templatePackUnpack(self, dataset, c_type_data = None):
        package_pointer = package_builder(dataset, c_type_data).create();
        unpacked_package = package_extractor(package_pointer).extract();
        
        assert dataset == unpacked_package;


    def testListInteger(self):
        self.templatePackUnpack([1, 2, 3, 4, 5]);

    def testListIntegerSingle(self):
        self.templatePackUnpack([2]);

    def testListIntegerNegative(self):
        self.templatePackUnpack([-1, -2, -10, -20]);

    def testListIntegerNegativeAndPositive(self):
        self.templatePackUnpack([-1, 26, -10, -20, 13]);

    def testListFloat(self):
        self.templatePackUnpack([1.1, 1.2, 1.3, 1.4, 1.5, 1.6]);

    def testListFloatNegativeAndPositive(self):
        self.templatePackUnpack([1.1, -1.2, -1.3, -1.4, 1.5, -1.6]);

    def testListLong(self):
        self.templatePackUnpack([100000000, 2000000000]);

    def testListEmpty(self):
        self.templatePackUnpack([]);

    def testListOfListInteger(self):
        self.templatePackUnpack([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]);

    def testListOfListDouble(self):
        self.templatePackUnpack([ [1.1, 5.4], [1.3], [1.4, -9.4] ]);

    def testListOfListWithGaps(self):
        self.templatePackUnpack([ [], [1, 2, 3], [], [4], [], [5, 6, 7] ]);

    def testListSpecifyUnsignedLong(self):
        self.templatePackUnpack([1, 2, 3, 4, 5], c_ulong);

    def testListSpecifyUnsignedSizeT(self):
        self.templatePackUnpack([1, 2, 3, 4, 5], c_size_t);

    def testListSpecifyDouble(self):
        self.templatePackUnpack([1.1, 1.6, -7.8], c_double);

    def testListOfListSpecifySizeT(self):
        self.templatePackUnpack([ [1, 2, 3], [4, 5] ], c_size_t);

    def testListOfListSpecifyUnsignedIntWithGaps(self):
        self.templatePackUnpack([ [1, 2, 3], [], [4, 5], [], [] ], c_uint);

    def testListOfListEmpty(self):
        self.templatePackUnpack([ [], [], [] ]);

    def testListOfListOfListInteger(self):
        self.templatePackUnpack([ [ [1], [2] ], [ [3], [4] ], [ [5, 6], [7, 8] ] ]);


if __name__ == "__main__":
    unittest.main();