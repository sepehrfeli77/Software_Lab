package Prototype;

public class Client {
    public static void main(String[] args) {

        Circle circle = new Circle();
        circle.x = 10;
        circle.y = 20;
        circle.radius = 15;
        circle.color = "red";

        Rectangle rectangle = new Rectangle();
        rectangle.width = 10;
        rectangle.height = 20;
        rectangle.color = "blue";

        Circle anotherCircle = (Circle) circle.clone();
        System.out.println(circle.equals(anotherCircle));
    }
}

