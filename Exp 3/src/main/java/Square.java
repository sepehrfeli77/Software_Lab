public class Square implements CalculateArea {
    private int edge;
    public Square(int edge) throws IllegalArgumentException{
        if (edge <= 0){
            throw new IllegalArgumentException("Edge should be positive!");
        }
        this.edge = edge;
    }

    public void setEdge(int edge) {
        if (edge <= 0){
            throw new IllegalArgumentException("Edge should be positive!");
        }
        this.edge = edge;
    }
    public int getEdge() {
        return edge;
    }

    @Override
    public int computeArea() {
        return (int)Math.pow(this.edge, 2);
    }
}
