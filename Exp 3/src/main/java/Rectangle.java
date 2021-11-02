public class Rectangle implements CalculateArea {
    private int width;
    private int height;

    public Rectangle(int width, int height) throws IllegalArgumentException {
        this.width = width;
        this.height = height;
    }


    @Override
    public int computeArea() {
        return width * height;
    }
}
