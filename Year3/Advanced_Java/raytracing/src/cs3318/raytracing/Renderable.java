package cs3318.raytracing;

// intersect(), Shade(), toString()

import java.awt.*;
import java.util.List;

interface Renderable {
    void intersect(Ray r);
    Color Shade(Ray r, java.util.List<Object> lights, List<Object> objects, Color bgnd);
    String toString();
}