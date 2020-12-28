package cs3318.raytracing;

// trace(), shade()

import java.awt.Color;
import java.util.List;


class Ray {
    public static final float MAX_T = Float.MAX_VALUE;
    final Vector3D origin;
    final Vector3D direction;
    float t;
    public Renderable object;

    /**
     *
     * @param eye - the Vector object representing the users eye.
     * @param dir - vector object represnting direction.
     */
    public Ray(Vector3D eye, Vector3D dir) {
        origin = new Vector3D(eye);
        direction = Vector3D.normalize(dir);
    }

    /**
     *
     * @param objects - list of renderable objects.
     * @return - if the list of renderable objects is not null.
     */
    public boolean trace(List<Object> objects) {
        t = MAX_T;
        object = null;
        for (Object objList : objects) {
            Renderable object = (Renderable) objList;
            object.intersect(this);
        }
        return (object != null);
    }

    // The following method is not strictly needed, and most likely
    // adds unnecessary overhead, but I preferred the syntax
    //
    //            ray.Shade(...)
    // to
    //            ray.object.Shade(ray, ...)
    //
    public final Color Shade(List<Object> lights, List<Object> objects, Color bgnd) {
        return object.Shade(this, lights, objects, bgnd);
    }

    public String toString() {
        return ("ray origin = "+origin+"  direction = "+direction+"  t = "+t);
    }
}

