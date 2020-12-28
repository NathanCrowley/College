package cs3318.A3;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
class ColourTest {
    //must specify three colour components
    @Test       //pass this test
    public void acceptIfThreeColourComponents(){
        final Colour TEST_COLOUR = new Colour(10,10,10);
        assertTrue(Colour.satisfiesRequirements(TEST_COLOUR), "Three components.");
    }
    /*@Test       //fail this test.
    public void rejectIfThreeColourComponents(){
        final Colour TEST_COLOUR = new Colour(10,10);
        assertFalse(Colour.satisfiesRequirements(TEST_COLOUR), "Accepts three components on Constructor.");
    }*/

    //not allowed to create Colour object without valid component values
    //Valid = in range 0-255
    @Test       //pass this test
    public void acceptIfComponentInRange(){
        final Colour TEST_COLOUR = new Colour(10,10,10);
        assertTrue(Colour.satisfiesRequirements(TEST_COLOUR),"Componets within range 0-255.");
    }
    @Test       //fail this test.
    public void rejectIfComponentNotInRange(){
        final Colour TEST_COLOUR = new Colour(256,10,10);
        assertFalse(Colour.satisfiesRequirements(TEST_COLOUR), "Accepts components in range 0 - 255.");
    }

    //Test if model is String
    @Test
    public void acceptIfModelString(){
        final Colour TEST_COLOUR = new Colour(10,10,10);
        TEST_COLOUR.setModel("YGB");
        assertTrue(Colour.satisfiesRequirements(TEST_COLOUR),"Model is a String.");
    }
}