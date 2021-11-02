import org.junit.Test;

import static org.junit.Assert.*;


public class RectangleTest {
    @Test
    public void calculateAreaOnPositiveWidthAndHeight() {
        int width = 2;
        int height = 5;
        Rectangle rectangle = new Rectangle(width, height);

        int expectedArea = width * height;
        int calculatedArea = rectangle.computeArea();

        assertEquals(expectedArea, calculatedArea);
    }

    @Test
    public void calculateAreaOnNotPositiveWidthAndHeight() {
        int width = -3;
        int height = 2;

        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            new Rectangle(width, height);
        });

        String expectedMessage = "Width or Height must be positive!";
        String gotMessage = exception.getMessage();

        assertEquals(expectedMessage, gotMessage);
    }

}