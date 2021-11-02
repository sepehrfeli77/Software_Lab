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

    @Test
    public void setAndGetPositiveWidthAndHeight() {
        Rectangle rectangle = new Rectangle(2, 5);

        int width = 20;
        rectangle.setWidth(width);
        assertEquals(rectangle.getWidth(), width);

        int height = 50;
        rectangle.setHeight(height);
        assertEquals(rectangle.getHeight(), height);
    }

    @Test
    public void setNonPositiveWidthOrHeight() {
        Rectangle rectangle = new Rectangle(2, 5);
        int width = -12;
        Exception widthException = assertThrows(IllegalArgumentException.class, () -> {
            rectangle.setWidth(width);
        });

        String widthRealMessage = "Width should be positive!";
        String widthGotMessage = widthException.getMessage();
        assertEquals(widthRealMessage, widthGotMessage);

        int height = -14;
        Exception heightException = assertThrows(IllegalArgumentException.class, () -> {
            rectangle.setHeight(height);
        });

        String heightRealMessage = "Height should be positive!";
        String heightGotMessage = heightException.getMessage();
        assertEquals(heightRealMessage, heightGotMessage);
    }
}