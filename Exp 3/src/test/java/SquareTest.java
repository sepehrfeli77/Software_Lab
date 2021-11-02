import org.junit.Test;

import static org.junit.Assert.*;

public class SquareTest{
    @Test
    public void calculateAreaOnPositiveEdge() {
        int edge = 5;
        Square square = new Square(edge);

        int expectedArea = edge * edge;
        int calculatedArea = square.computeArea();

        assertEquals(expectedArea, calculatedArea);
    }

    @Test
    public void calculateAreaOnNotPositiveEdge() {
        int edge = -1;

        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            new Square(edge);
        });

        String expectedMessage = "Edge should be positive!";
        String gotMessage = exception.getMessage();
        assertEquals(expectedMessage, gotMessage);

    }

    @Test
    public void setAndGetPositiveEdge() {
        Square square = new Square(2);
        int edge = 5;
        square.setEdge(edge);
        assertEquals(square.getEdge(), edge);
    }


    @Test
    public void setNotPositiveEdge() {
        Square square = new Square(2);
        int edge = -1;
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            square.setEdge(edge);
        });
        String expectedMessage = "Edge should be positive!";
        String gotMessage = exception.getMessage();
        assertEquals(expectedMessage, gotMessage);
    }
}