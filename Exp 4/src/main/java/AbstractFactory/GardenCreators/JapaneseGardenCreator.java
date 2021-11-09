package AbstractFactory.GardenCreators;

import AbstractFactory.Flowers.Flower;
import AbstractFactory.Flowers.JapaneseFlower;
import AbstractFactory.Trees.JapaneseTree;
import AbstractFactory.Trees.Tree;

public class JapaneseGardenCreator extends GardenCreator {
    @Override
    public Flower createFlower() {
        return new JapaneseFlower();
    }

    @Override
    public Tree createTree() {
        return new JapaneseTree();
    }
}
