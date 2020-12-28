package cs3318.raytracing;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {

    /**
     *
     * @param primaryStage - Type: Stage object. Used as the window that is shown when the application is run.
     * @throws Exception - if there is a problem with running the primaryStage throw an Exception.
     */
    @Override
    public void start(Stage primaryStage) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("render.fxml"));
        //Parent root = loader.load(getClass().getResource("render.fxml").openStream());
        Parent root = loader.load();
        Controller controller = (Controller) loader.getController();

        primaryStage.setTitle("Simple Ray Tracing");
        primaryStage.setScene(new Scene(root, 860, 1000));
        //

        //controller.setStage(primaryStage);
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
