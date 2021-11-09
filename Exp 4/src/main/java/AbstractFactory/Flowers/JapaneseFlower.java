package AbstractFactory.Flowers;

public class JapaneseFlower implements Flower {
    @Override
    public String createFlowerResult() {
        return "Japanese flower created";
    }
}
