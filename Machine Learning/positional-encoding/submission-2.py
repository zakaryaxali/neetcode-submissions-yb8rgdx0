import numpy as np
from numpy.typing import NDArray


class Solution:
    def get_positional_encoding(self, seq_len: int, d_model: int) -> NDArray[np.float64]:
        # PE(pos, 2i)   = sin(pos / 10000^(2i / d_model))
        # PE(pos, 2i+1) = cos(pos / 10000^(2i / d_model))
        #
        # Hint: Use np.arange() to create position and dimension index vectors,
        # then compute all values at once with broadcasting (no loops needed).
        # Assign sine to even columns (PE[:, 0::2]) and cosine to odd columns (PE[:, 1::2]).
        # Round to 5 decimal places.
        def pe(pos, n, d_model):
            if n%2 == 0:
                res = np.sin(pos/(10000**(n/d_model)))
            else:
                res = np.cos(pos/(10000**((n-1)/d_model)))
            return res

        res= []
        for i in range(seq_len):
            vec= np.arange(d_model)
            vec=[pe(i,j,d_model) for j in vec]
            res.append(vec)


        return np.round(res,5)
