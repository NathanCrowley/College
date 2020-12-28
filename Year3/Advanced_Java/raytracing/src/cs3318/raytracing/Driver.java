package cs3318.raytracing;

import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.image.Image;
import javafx.scene.paint.Color;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

/**
 * StreamTokenizer was deprecated so we created a BufferedReader object that takes in an Input stream and uses
 * 	this bufferedReader in the SteamTokenizer object.
 */
class Driver  {
    final static int CHUNKSIZE = 100;
    List<Object> objectList;
    List<Object> lightList;
    Surface currentSurface;
	Canvas canvas;
	GraphicsContext gc;

    Vector3D eye, lookat, up;
    Vector3D Du, Dv, Vp;
	// default horizontal field of view
	float fov = 30;

    Color background;

    int width, height;

	/**
	 * Constructor for the Driver class.
	 * @param width - width of the window shown when you run the Main class. {@code width<=0}
	 * @param height - height of the window shown when you run the Main class. {@code height<=0}
	 * @param dataFile - String of the pathname leading to the file with the information about how to present the scene.
	 */
    public Driver(int width, int height, String dataFile) {
        this.width = width;
        this.height = height;

		canvas = new Canvas(this.width, this.height);
		gc = canvas.getGraphicsContext2D();

        gc.setFill(Color.WHITE);
        gc.fillRect(0, 0, width, height);

		// Initialize various lists
        objectList = new ArrayList<>(CHUNKSIZE);
        lightList = new ArrayList<>(CHUNKSIZE);
        currentSurface = new Surface(0.8f, 0.2f, 0.9f, 0.2f, 0.4f, 0.4f, 10.0f, 0f, 0f, 1f);

        // Parse the scene file
        String filename = dataFile != null ? dataFile : "defaultScene.txt";

        InputStream is;
        try {
            is = new FileInputStream(new File(filename));
            ReadInput(is);
            is.close();
        } catch (IOException e) {
			System.err.println("Error reading "+ new File(filename).getAbsolutePath());
			e.printStackTrace();
            System.exit(-1);
        }

        // Initialize more defaults if they weren't specified
        if (eye == null) eye = new Vector3D(0, 0, 10);
        if (lookat == null) lookat = new Vector3D(0, 0, 0);
        if (up  == null) up = new Vector3D(0, 1, 0);
        if (background == null) background = Color.rgb(0,0,0);

        // Compute viewing matrix that maps a
        // screen coordinate to a ray direction
        Vector3D look = new Vector3D(lookat.x - eye.x, lookat.y - eye.y, lookat.z - eye.z);
        Du = Vector3D.normalize(look.cross(up));
        Dv = Vector3D.normalize(look.cross(Du));
        float fl = (float)(width / (2*Math.tan((0.5*fov)*Math.PI/180)));
        Vp = Vector3D.normalize(look);
        Vp.x = Vp.x*fl - 0.5f*(width*Du.x + height*Dv.x);
        Vp.y = Vp.y*fl - 0.5f*(width*Du.y + height*Dv.y);
        Vp.z = Vp.z*fl - 0.5f*(width*Du.z + height*Dv.z);
    }

	/**
	 *
	 * @param st - the StreamTokenizer object that we want to get the Number of.
	 * @return - Type: double.
	 * @throws IOException - if the number is not found in the line, raise IOException.
	 */
    double getNumber(StreamTokenizer st) throws IOException {
        if (st.nextToken() != StreamTokenizer.TT_NUMBER) {
            System.err.println("ERROR: number expected in line "+st.lineno());
            throw new IOException(st.toString());
        }
        return st.nval;
    }

	/**
	 *
	 * @param is - InputStream object used to create Reader object with BufferedReader method.
	 * @throws IOException - if there is no nextToken throw IOException.
	 */
    void ReadInput(InputStream is) throws IOException {
		Reader re = new BufferedReader(new InputStreamReader(is));
	    StreamTokenizer st = new StreamTokenizer(re);
    	st.commentChar('#');
		while (true) {
			if (st.nextToken() == StreamTokenizer.TT_WORD) {
				switch (st.sval) {
					case "sphere": {
						Vector3D v = new Vector3D((float) getNumber(st), (float) getNumber(st), (float) getNumber(st));
						float r = (float) getNumber(st);
						objectList.add(new Sphere(currentSurface, v, r));
						break;
					}
					case "eye":
						eye = new Vector3D((float) getNumber(st), (float) getNumber(st), (float) getNumber(st));
						break;
					case "lookat":
						lookat = new Vector3D((float) getNumber(st), (float) getNumber(st), (float) getNumber(st));
						break;
					case "up":
						up = new Vector3D((float) getNumber(st), (float) getNumber(st), (float) getNumber(st));
						break;
					case "fov":
						fov = (float) getNumber(st);
						break;
					case "background":
						background = Color.rgb((int) getNumber(st), (int) getNumber(st), (int) getNumber(st));
						break;
					case "light": {
						float r = (float) getNumber(st);
						float g = (float) getNumber(st);
						float b = (float) getNumber(st);
						if (st.nextToken() != StreamTokenizer.TT_WORD) {
							throw new IOException(st.toString());
						}
						switch (st.sval) {
							case "ambient":
								lightList.add(new Light(Light.AMBIENT, null, r, g, b));
								break;
							case "directional": {
								Vector3D v = new Vector3D((float) getNumber(st), (float) getNumber(st), (float) getNumber(st));
								lightList.add(new Light(Light.DIRECTIONAL, v, r, g, b));
								break;
							}
							case "point": {
								Vector3D v = new Vector3D((float) getNumber(st), (float) getNumber(st), (float) getNumber(st));
								lightList.add(new Light(Light.POINT, v, r, g, b));
								break;
							}
							default:
								System.err.println("ERROR: in line " + st.lineno() + " at " + st.sval);
								throw new IOException(st.toString());
						}
						break;
					}
					case "surface": {
						float r = (float) getNumber(st);
						float g = (float) getNumber(st);
						float b = (float) getNumber(st);
						float ka = (float) getNumber(st);
						float kd = (float) getNumber(st);
						float ks = (float) getNumber(st);
						float ns = (float) getNumber(st);
						float kr = (float) getNumber(st);
						float kt = (float) getNumber(st);
						float index = (float) getNumber(st);
						currentSurface = new Surface(r, g, b, ka, kd, ks, ns, kr, kt, index);
						break;
					}
				}
			} else {
				break;
			}
		}
        is.close();
	    if (st.ttype != StreamTokenizer.TT_EOF)
	        throw new IOException(st.toString());
	}

	Image getRenderedImage() {
    	return canvas.snapshot(null, null);
	}

	/**
	 *
	 * @param i - the vectors magnitude Type: int. {@code i>=0}
	 * @param j - the vectors direction Type: int.
	 */
	public void renderPixel(int i, int j) {
		Vector3D dir = new Vector3D(
				i*Du.x + j*Dv.x + Vp.x,
				i*Du.y + j*Dv.y + Vp.y,
				i*Du.z + j*Dv.z + Vp.z);
		Ray ray = new Ray(eye, dir);
		if (ray.trace(objectList)) {
			java.awt.Color bg = toAWTColor(background);
			gc.setFill(toFXColor(ray.Shade(lightList, objectList, bg)));
		} else {
			gc.setFill(background);
		}
		gc.fillOval(i, j, 1, 1);
	}

	private java.awt.Color toAWTColor(Color c) {
    	return new java.awt.Color((float) c.getRed(),
				(float) c.getGreen(),
				(float) c.getBlue(),
				(float) c.getOpacity());
	}

	private Color toFXColor(java.awt.Color c) {
		return Color.rgb(c.getRed(), c.getGreen(), c.getBlue(), c.getAlpha() / 255.0);
	}
}