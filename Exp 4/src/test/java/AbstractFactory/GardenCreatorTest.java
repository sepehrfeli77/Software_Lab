package AbstractFactory;

import AbstractFactory.Flowers.IranianFlower;
import AbstractFactory.Flowers.JapaneseFlower;
import AbstractFactory.GardenCreators.IranianGardenBuilder;
import AbstractFactory.GardenCreators.JapaneseGardenBuilder;
import AbstractFactory.Trees.IranianTree;
import AbstractFactory.Trees.JapaneseTree;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

public class GardenCreatorTest {
    @Test
    public void IranianGardenWithIranianTreesAndFlowers(){
        IranianGardenBuilder iranianGardenBuilder = new IranianGardenBuilder();
        String expectedFlowerMessage = "Iranian flower created";
        String expectedTreeMessage = "Iranian tree created";

        IranianFlower iranianFlower = (IranianFlower) iranianGardenBuilder.createFlower();
        String realFlowerMessage = iranianFlower.getMessage();

        IranianTree iranianTree = (IranianTree) iranianGardenBuilder.createTree();
        String realTreeMessage = iranianTree.getMessage();

        assertEquals(realFlowerMessage, expectedFlowerMessage);
        assertEquals(realTreeMessage, expectedTreeMessage);
    }

    @Test
    public void IranianGardenWithJapaneseTrees(){
        IranianGardenBuilder iranianGardenBuilder = new IranianGardenBuilder();
        assertThrows(ClassCastException.class, () -> {
            JapaneseTree japaneseTree = (JapaneseTree) iranianGardenBuilder.createTree();
        });
    }

    @Test
    public void IranianGardenWithJapaneseFlowers(){
        IranianGardenBuilder iranianGardenBuilder = new IranianGardenBuilder();
        assertThrows(ClassCastException.class, () -> {
            JapaneseFlower japaneseFlower = (JapaneseFlower) iranianGardenBuilder.createFlower();
        });
    }

    public void JapaneseGardenWithJapaneseTreesAndFlowers(){
        JapaneseGardenBuilder japaneseGardenBuilder = new JapaneseGardenBuilder();
        String expectedFlowerMessage = "Japanese flower created";
        String expectedTreeMessage = "Japanese tree created";

        JapaneseFlower japaneseFlower = (JapaneseFlower) japaneseGardenBuilder.createFlower();
        String realFlowerMessage = japaneseFlower.getMessage();

        JapaneseTree japaneseTree = (JapaneseTree) japaneseGardenBuilder.createTree();
        String realTreeMessage = japaneseTree.getMessage();

        assertEquals(realFlowerMessage, expectedFlowerMessage);
        assertEquals(realTreeMessage, expectedTreeMessage);
    }

    @Test
    public void JapaneseGardenWithIranianTrees(){
        JapaneseGardenBuilder japaneseGardenBuilder = new JapaneseGardenBuilder();
        assertThrows(ClassCastException.class, () -> {
            IranianTree iranianTree = (IranianTree) japaneseGardenBuilder.createTree();
        });
    }

    @Test
    public void JapaneseGardenWithIranianFlowers(){
        JapaneseGardenBuilder japaneseGardenBuilder = new JapaneseGardenBuilder();
        assertThrows(ClassCastException.class, () -> {
            IranianFlower iranianFlower = (IranianFlower) japaneseGardenBuilder.createFlower();
        });
    }
}
