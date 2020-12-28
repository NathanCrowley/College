package cs3318.raytracing;

// All the public variables here are ugly, but I
// wanted Lights and Surfaces to be "friends"
class Light {
    public static final int AMBIENT = 0;
    public static final int DIRECTIONAL = 1;
    public static final int POINT = 2;

    public final int lightType;
    public Vector3D lvec; // the position of a point light or the direction to a directional light
    public final float ir;
    public final float ig;
    public final float ib; // intensity of the light source

    /**
     * Light constructor used to generate light with vector object and light intensity and type information.
     *
     * @param type - where the light is Ambient or not. Type: int.
     * @param v - the velocity of the vector. Type: Vector3D object.
     * @param r - Type: float.
     * @param g - Type: float.
     * @param b - Type: float. Intensity of light.
     */
    public Light(int type, Vector3D v, float r, float g, float b) {
        lightType = type;
        ir = r;
        ig = g;
        ib = b;
        if (type != AMBIENT) {
            lvec = v;
            if (type == DIRECTIONAL) {
                lvec.normalize();
            }
        }
    }
}

