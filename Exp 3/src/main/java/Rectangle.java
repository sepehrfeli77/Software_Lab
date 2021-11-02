public class Rectangle implements CalculateArea {
    private int width;
    private int height;

    public Rectangle(int width, int height) throws IllegalArgumentException {
        if (height <= 0 || width <= 0) {
            throw new IllegalArgumentException("Width or Height must be positive!");
        }

        this.width = width;
        this.height = height;
    }


    @Override
    public int computeArea() {
        return width * height;
    }


}
