package AbstractFactory.GardenCreators;

import AbstractFactory.Flowers.Flower;
import AbstractFactory.Trees.Tree;

public abstract class GardenCreator {
    public abstract Flower createFlower();
    public abstract Tree createTree();
}
