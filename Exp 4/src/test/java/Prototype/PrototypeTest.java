package Prototype;

import org.junit.Test;

import static org.junit.Assert.*;

public class PrototypeTest {
    @Test
    public void CheckCircleAndClonedCircle() {
        Circle circle = new Circle();
        circle.x = 10;
        circle.y = 20;
        circle.radius = 15;
        circle.color = "red";
        Circle anotherCircle = (Circle) circle.clone();

        assertEquals(circle, anotherCircle);

        System.out.println("ProtoType First Test: Passed");
    }

    @Test
    public void CheckRectangleAndClonedRectangle() {
        Rectangle rectangle = new Rectangle();
        rectangle.width = 10;
        rectangle.height = 20;
        rectangle.color = "blue";
        Rectangle anotherRectangle = (Rectangle) rectangle.clone();

        assertEquals(rectangle, anotherRectangle);

        System.out.println("ProtoType Second Test: Passed");
    }

    @Test
    public void CheckTwoDifferentRectanglesWithSameProperty() {
        Rectangle rectangle = new Rectangle();
        rectangle.width = 10;
        rectangle.height = 20;
        rectangle.color = "blue";
        Rectangle rectangle1 = new Rectangle();
        rectangle.width = 10;
        rectangle.height = 20;
        rectangle.color = "blue";

        assertNotEquals(rectangle, rectangle1);

        System.out.println("ProtoType Third Test: Passed");
    }

    @Test
    public void CheckCircleAndRectangleWithTogether() {
        Rectangle rectangle = new Rectangle();
        rectangle.width = 10;
        rectangle.height = 20;
        rectangle.color = "blue";
        Circle circle = new Circle();
        circle.x = 10;
        circle.y = 20;
        circle.radius = 15;
        circle.color = "red";

        assertNotEquals(rectangle, circle);

        System.out.println("ProtoType Forth Test: Passed");
    }

}
