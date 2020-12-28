package cs3318.A3;
import java.util.ArrayList;
import java.util.*;

public class Colour {
    private int c1;
    private int c2;
    private int c3;
    private String model = "RGB";

    public Colour(int c1, int c2, int c3){
        this.c1 =c1;
        this.c2 =c2;
        this.c3 =c3;
        this.model = model;
    }

    //default colour model is RGB
    //different colour models specified by using a String to identify name of model when creating Colour object.
    public void setModel(String newModel){
        this.model = newModel;
    }

    public static boolean satisfiesRequirements(Colour test_colour) {
        return ((test_colour.getParameterCount() == 3)||((test_colour.c1 >= 0 && test_colour.c1 <=255)&&(test_colour.c2 >= 0 && test_colour.c2 <=255)&&(test_colour.c3 >= 0 && test_colour.c3 <=255))&&(test_colour.model instanceof String));
    }

    private int getParameterCount() {
        List<Integer> parametersList = new ArrayList<Integer>();
        parametersList.add(this.c1);
        parametersList.add(this.c2);
        parametersList.add(this.c3);
        return parametersList.size();
    }

    //Colour objects can be compared, to be exactly equal must have same colour model and components.
    public boolean compareEqualColours(Colour colour2){
        return ((this.model == colour2.model)&&(this.c1==colour2.c1)&&(this.c2==colour2.c2)&&(this.c3==colour2.c3));
    }
    //Colour objects can be added, if they same model, by adding each components (cannot exceed 255).
    public void addColours(Colour colour2){
        if(this.model == colour2.model){
            this.c1 += colour2.c1;
            this.c2 += colour2.c2;
            this.c3 += colour2.c3;
        }
        //check if any of the components has surpassed 255.
        if(this.c1 > 255){this.c1 = 255;}
        if(this.c2 > 255){this.c2 = 255;}
        if(this.c3 > 255){this.c3 = 255;}
    }

}
