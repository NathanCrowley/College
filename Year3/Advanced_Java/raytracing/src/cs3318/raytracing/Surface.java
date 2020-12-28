package cs3318.raytracing;

// surface(), shade()

// An object must implement a Renderable interface in order to
// be ray traced. Using this interface it is straight forward
// to add new object
import java.awt.*;
import java.util.List;

/*
ka =  ambient reflection coefficient
kd = diffuse reflection coefficient
ks = specular reflection coefficient
kt = transmission coefficient
kr = reflectance coefficient
ns phong exponent
 */

/**
 * ib - surfaces intrinsic color.
 * ns - constants for phong model.
 */
class Surface {
    public final float ka,kd,ks,kt,kr,ir,ig,ib,ns,nt;

    private static final float TINY = 0.001f;
    private static final float I255 = 0.00392156f;  // 1/255

    public Surface(float rval, float gval, float bval, float a, float d, float s, float n, float r, float t, float index) {
        ir = rval; ig = gval; ib = bval;
        ka = a; kd = d; ks = s; ns = n;
        kr = r*I255; kt = t; nt = index;
    }

    /**
     *
     * @param p - position vector object
     * @param n - reflection vecotr object
     * @param v - velocity vecotr object
     * @param lights - list of light objects
     * @param objects - list of given objects.
     * @param bgnd - background color.
     * @return - the color of the background in rgb format.
     */
    public Color Shade(Vector3D p, Vector3D n, Vector3D v, java.util.List<Object> lights, List<Object> objects, Color bgnd) {
        float r = 0;
        float g = 0;
        float b = 0;

        for (Object lightSources : lights) {
            Light light = (Light) lightSources;

            if (light.lightType == Light.AMBIENT) {
                r += ka*ir*light.ir;
                g += ka*ig*light.ig;
                b += ka*ib*light.ib;
            } else {
                Vector3D l;
                if (light.lightType == Light.POINT) {
                    l = new Vector3D(light.lvec.x - p.x, light.lvec.y - p.y, light.lvec.z - p.z);
                    l.normalize();
                } else {
                    l = new Vector3D(-light.lvec.x, -light.lvec.y, -light.lvec.z);
                }

                // Check if the surface point is in shadow
                Vector3D poffset = new Vector3D(p.x + TINY*l.x, p.y + TINY*l.y, p.z + TINY*l.z);
                Ray shadowRay = new Ray(poffset, l);

                if (shadowRay.trace(objects))
                    break;

                float lambert = Vector3D.dot(n,l);
                if (lambert > 0) {

                    if (kd > 0) {
                        float diffuse = kd*lambert;
                        r += diffuse*ir*light.ir;
                        g += diffuse*ig*light.ig;
                        b += diffuse*ib*light.ib;
                    }
                    if (ks > 0) {
                        lambert *= 2;
                        float spec = v.dot(lambert*n.x - l.x, lambert*n.y - l.y, lambert*n.z - l.z);

                        if (spec > 0) {
                            spec = ks*((float) Math.pow(spec, ns));
                            r += spec*light.ir;
                            g += spec*light.ig;
                            b += spec*light.ib;
                        }
                    }
                }
            }
        }

        // Compute illumination due to reflection
        if (kr > 0) {
            float t = v.dot(n);

            if (t > 0) {
                t *= 2;
                Vector3D reflect = new Vector3D(t*n.x - v.x, t*n.y - v.y, t*n.z - v.z);
                Vector3D poffset = new Vector3D(p.x + TINY*reflect.x, p.y + TINY*reflect.y, p.z + TINY*reflect.z);
                Ray reflectedRay = new Ray(poffset, reflect);

                if (reflectedRay.trace(objects)) {
                    Color rcolor = reflectedRay.Shade(lights, objects, bgnd);
                    r += kr*rcolor.getRed();
                    g += kr*rcolor.getGreen();
                    b += kr*rcolor.getBlue();
                } else {
                    r += kr*bgnd.getRed();
                    g += kr*bgnd.getGreen();
                    b += kr*bgnd.getBlue();
                }
            }
        }

        // Add code for refraction here

        r = Math.min(r, 1f);
        g = Math.min(g, 1f);
        b = Math.min(b, 1f);

        r = (r < 0) ? 0 : r;
        g = (g < 0) ? 0 : g;
        b = (b < 0) ? 0 : b;

        return new Color(r, g, b);
    }
}