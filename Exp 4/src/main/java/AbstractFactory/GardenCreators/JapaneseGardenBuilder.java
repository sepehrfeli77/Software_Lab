package AbstractFactory.GardenCreators;

import AbstractFactory.Flowers.Flower;
import AbstractFactory.Flowers.JapaneseFlower;
import AbstractFactory.Trees.JapaneseTree;
import AbstractFactory.Trees.Tree;

public class JapaneseGardenBuilder extends GardenBuilder{
    @Override
    public Flower createFlower() {
        return new JapaneseFlower();
    }

    @Override
    public Tree createTree() {
        return new JapaneseTree();
    }
}
