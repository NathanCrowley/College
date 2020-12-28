package cs3318.raytracing;

import javafx.scene.image.ImageView;

/**
 * Controller class that has methods -run() and -startRayTrace(), used to render the #
 *  scene from external corodinates in "resources/SceneToRender.txt" file.
 */
public class Controller {
    public ImageView renderedImage;
    private Driver sceneToRender;
    boolean finished = false;


    public void run() {
        long time = System.currentTimeMillis();
        for (int j = 0; j < sceneToRender.height; j += 1) {
            for (int i = 0; i < sceneToRender.width; i += 1) {
                sceneToRender.renderPixel(i, j);
            }
        }
        renderedImage.setImage(sceneToRender.getRenderedImage());
        time = System.currentTimeMillis() - time;
        System.err.println("Rendered in "+(time/60000)+":"+((time%60000)*0.001));
        finished = true;
    }


    public void startRayTrace() {
        sceneToRender = new Driver((int) renderedImage.getFitWidth(),
                                   (int) renderedImage.getFitHeight(),
                "resources/SceneToRender.txt");
        this.run();
    }
}
