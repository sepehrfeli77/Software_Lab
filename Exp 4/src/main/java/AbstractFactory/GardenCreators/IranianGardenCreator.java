package AbstractFactory.GardenCreators;

import AbstractFactory.Flowers.Flower;
import AbstractFactory.Flowers.IranianFlower;
import AbstractFactory.Trees.IranianTree;
import AbstractFactory.Trees.Tree;

public class IranianGardenCreator extends GardenCreator {

    @Override
    public Flower createFlower() {
        return new IranianFlower();
    }

    @Override
    public Tree createTree() {
        return new IranianTree();
    }
}
