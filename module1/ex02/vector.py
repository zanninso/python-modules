import enum


class VVT(enum.Enum):
    Column = 1
    Row = 2


class Vector:
    def __init__(self, values):
        if (isinstance(values, int)):
            values = range(0, values)

        if (isinstance(values, range)):
            self.type = VVT.Column
            self.values = []
            for n in values:
                self.values.append([float(n)])

        elif (isinstance(values, list)):
            if (len(values) == 0):
                raise Exception("can not initialize Vector with empty list")

            if (len(values) == 1):
                values = values[0]

            # list of lists
            if (all(isinstance(i, list) for i in values)):
                if (all(isinstance(i, float) for i in sum(values, []))):
                    if (all(len(v) == 1 for v in values) is False):
                        raise Exception("len of lists different  than 1")
                    self.type = VVT.Column
                    self.values = values
                else:
                    raise Exception("the values should be all float")

            # list of floats
            elif (all(isinstance(i, float) for i in values)):
                self.type = VVT.Row
                self.values = values
            else:
                raise Exception("the values should be all float")
        else:
            raise Exception("invalide input")

        # set dimensions
        rows_count = 1 if (self.type == VVT.Row) else len(values)
        column_count = 1 if (self.type == VVT.Column) else len(values)
        self.shape = (rows_count, column_count)

    def __add__(self, other):
        # add : only vectors of same dimensions.
        if (isinstance(other, Vector) is False):
            raise Exception('Right value is not a Vector')

        if (self.type is not other.type):
            other = other.T()

        if (self.shape != other.shape):
            raise Exception('Can not add Vectors of different dimension')

        v = None
        if (self.type == VVT.Row):
            v = [x + y for x, y in zip(self.values, other.values)]
        elif (self.type == VVT.Column):
            v = [[x[0] + y[0]] for x, y in zip(self.values, other.values)]
        return Vector(v)

    def __radd__(self, other):
        raise Exception('Can not add Vector to scaler')

    def __sub__(self, other):
        # sub : only vectors of same dimensions.
        if (isinstance(other, Vector) is False):
            raise Exception('Right value is not a Vector')

        if (self.type is not other.type):
            other = other.T()

        if (self.shape != other.shape):
            raise Exception('Can not substruct Vectors of different dimension')
        v = None
        if (self.type == VVT.Row):
            v = [x - y for x, y in zip(self.values, other.values)]
        elif (self.type == VVT.Column):
            v = [[x[0] - y[0]] for x, y in zip(self.values, other.values)]
        return Vector(v)

    def __rsub__(self, other):
        raise Exception('Can not substruct Vector from scaler')

    def __truediv__(self, scalar):
        # div : only scalars.
        if ((isinstance(scalar, float) or isinstance(scalar, int)) is False):
            raise Exception('Right value is not a scalar')

        if (scalar == 0):
            raise Exception('zero division')

        if (self.type == VVT.Row):
            return Vector([x / scalar for x in self.values])
        elif (self.type == VVT.Column):
            return Vector([[x[0] / scalar] for x in self.values])

    def __rtruediv__(self, other):
        raise Exception('A scalar cannot be divided by a Vector')

    def __mul__(self, scalar):
        # mul : only scalars.
        if ((isinstance(scalar, float) or isinstance(scalar, int)) is False):
            raise Exception('Right value is not a scalar')

        if (self.type == VVT.Row):
            return Vector([x * scalar for x in self.values])
        elif (self.type == VVT.Column):
            return Vector([[x[0] * scalar] for x in self.values])

    def __rmul__(self, other):
        raise Exception('A scalar cannot be multiplied by a Vector')

    def __str__(self):
        return '{}'.format(self.values)

    def __repr__(self):
        return('Vector({})'.format(self.values))

    def dot(self, other):
        if (isinstance(other, Vector) is False):
            raise Exception('Right value is not a Vector')

        if (self.type is not other.type):
            other = other.T()

        if (self.shape != other.shape):
            raise Exception('Can not operate dot product on \
Vectors of different dimension')

        if (self.type == VVT.Row):
            v = [x * y for x, y in zip(self.values, other.values)]
        elif (self.type == VVT.Column):
            v = [x[0] * y[0] for x, y in zip(self.values, other.values)]
        return sum(v)

    def T(self):
        if (self.type == VVT.Row):
            return Vector([[x] for x in self.values])
        elif (self.type == VVT.Column):
            return Vector([x[0] for x in self.values])
