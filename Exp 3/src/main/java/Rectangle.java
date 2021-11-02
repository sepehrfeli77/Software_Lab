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


    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        if (width <= 0)
            throw new IllegalArgumentException("Width should be positive!");
        this.width = width;
    }

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        if (height <= 0)
            throw new IllegalArgumentException("Height should be positive!");
        this.height = height;
    }
}
