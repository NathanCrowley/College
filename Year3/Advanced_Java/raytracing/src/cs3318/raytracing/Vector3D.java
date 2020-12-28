package cs3318.raytracing;

// A simple vector class
// several version of dot(), cross(), normalize(), length()
class Vector3D {
    public float x, y, z;

    /**
     * Constructor for Vector3D class.
     *
     * @param x - the x coordinates for the vector object.
     * @param y - the y coordinates.
     * @param z - the z coordinates.
     */
    public Vector3D(float x, float y, float z) {
        this.x = x; this.y = y; this.z = z;
    }

    public Vector3D(Vector3D v) {
        x = v.x;
        y = v.y;
        z = v.z;
    }

    // methods

    /**
     *
     * @param B - vecotr object
     * @return the amount of one vecotor goes in the direction of another.
     */
    public final float dot(Vector3D B) {
        return (x*B.x + y*B.y + z*B.z);
    }

    public final float dot(float Bx, float By, float Bz) {
        return (x*Bx + y*By + z*Bz);
    }

    public static float dot(Vector3D A, Vector3D B) {
        return (A.x*B.x + A.y*B.y + A.z*B.z);
    }

    /**
     *
     * @param B - vector object
     * @return - the cross product of the vector.
     */
    public final Vector3D cross(Vector3D B) {
        return new Vector3D(y*B.z - z*B.y, z*B.x - x*B.z, x*B.y - y*B.x);
    }

    public final Vector3D cross(float Bx, float By, float Bz) {
        return new Vector3D(y*Bz - z*By, z*Bx - x*Bz, x*By - y*Bx);
    }

    // @org.jetbrains.annotations.Contract
    public static Vector3D cross(Vector3D A, Vector3D B) {
        return new Vector3D(A.y*B.z - A.z*B.y, A.z*B.x - A.x*B.z,   A.x*B.y - A.y*B.x);
    }

    public final float length( ) {
        return (float) Math.sqrt(x*x + y*y + z*z);
    }

    /**
     *
     * @param A - vector object
     * @return - length of a given vector.
     */
    public static float length(Vector3D A) {
        return (float) Math.sqrt(A.x*A.x + A.y*A.y + A.z*A.z);
    }

    public final void normalize( ) {
        float t = x*x + y*y + z*z;
        if (t != 0 && t != 1) t = (float) (1 / Math.sqrt(t));
        x *= t;
        y *= t;
        z *= t;
    }

    /**
     * Method to take a vector and keep it pointing in the same direction, changing its length to 1 making it a unit vector.
     * @param A - cector object.
     * @return
     */
    public static Vector3D normalize(Vector3D A) {
        float t = A.x*A.x + A.y*A.y + A.z*A.z;
        if (t != 0 && t != 1) t = (float)(1 / Math.sqrt(t));
        return new Vector3D(A.x*t, A.y*t, A.z*t);
    }

    public String toString() {
        return "[" + x + ", " + y + ", " + z + "]";
    }
}

