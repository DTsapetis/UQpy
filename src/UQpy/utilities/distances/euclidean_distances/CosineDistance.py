from typing import Union

from scipy.spatial.distance import pdist

from UQpy.utilities.distances.baseclass.EuclideanDistance import EuclideanDistance
from UQpy.utilities.ValidationTypes import NumpyFloatArray


class CosineDistance(EuclideanDistance):
    def compute_distance(self, xi: NumpyFloatArray, xj: NumpyFloatArray) -> float:
        """
        Given two points, this method calculates the Cosine distance.

        :param xi: First point.
        :param xj: Second point.
        :return: A float representing the distance between the points.
        """

        return pdist([xi, xj], "cosine")[0]
