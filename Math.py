class Matrix:
    determinant = None
    scale = None
    translation = None
    isMirrored = None

    roll = None
    pitch = None
    yaw = None

    def preMultiply(self):
        pass

    def set(self):
        pass

    def setScale(self):
        pass

    def applyToAxis(self):
        pass

    def postMultiply(self):
        pass

    def lookAt(self):
        pass

    def setTranslate(self):
        pass

    def applyToOrigin(self):
        pass

    def setRotateYPR(self):
        pass

    def invert(self):
        pass

    def __setstate__(self):
        pass

    def applyPoint(self, vector):
        pass

    def __getstate__(self):
        pass

    def setIdentity(self):
        pass

    def setElement(self):
        pass

    def get(self):
        pass

    def applyVector(self, vector):
        pass

    def orthogonalProjection(self):
        pass

    def setRotateY(self):
        pass

    def setRotateX(self):
        pass

    def setRotateZ(self):
        pass

    def perspectiveProjection(self):
        pass

    def applyV4Point(self):
        pass

    def setZero(self):
        pass

class Vector3:
    pitch = None
    yaw = None
    length = None
    lengthSquared = None
    isReference = None
    x = None
    y = None
    z = None

    def set(self):
        pass

    def flatDistTo(self):
        pass

    def distSqrTo(self):
        pass

    def distTo(self):
        pass

    def cross2D(self):
        pass

    def scale(self):
        pass

    def __setstate__(self):
        pass

    def __getstate__(self):
        pass

    def tuple(self):
        pass

    def normalise(self):
        pass

    def setPitchYaw(self):
        pass

    def list(self):
        pass

    def flatDistSqrTo(self):
        pass

    def dot(self):
        pass
