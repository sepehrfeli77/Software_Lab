package AbstractFactory.GardenCreators;

import AbstractFactory.Flowers.Flower;
import AbstractFactory.Trees.Tree;

public abstract class GardenBuilder {
    public abstract Flower createFlower();
    public abstract Tree createTree();
}
