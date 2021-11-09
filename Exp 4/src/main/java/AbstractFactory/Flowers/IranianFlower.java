package AbstractFactory.Flowers;

public class IranianFlower implements Flower {
    @Override
    public String createFlowerResult() {
        return "Iranian flower created";
    }
}
