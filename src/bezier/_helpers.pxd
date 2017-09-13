# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Cython wrapper for ``helpers.f90``."""


from libcpp cimport bool as bool_t


cdef extern from "bezier/helpers.h":
    void cross_product(double *vec0, double *vec1, double *result)
    void bbox(
        int *num_nodes, double *nodes, double *left,
        double *right, double *bottom, double *top)
    void wiggle_interval(double *value, double *result, bool_t *success)
    void contains_nd(
        int *num_nodes, int *dimension, double *nodes,
        double *point, bool_t *predicate)
