package AbstractFactory;

import AbstractFactory.Flowers.IranianFlower;
import AbstractFactory.Flowers.JapaneseFlower;
import AbstractFactory.GardenCreators.IranianGardenCreator;
import AbstractFactory.GardenCreators.JapaneseGardenCreator;
import AbstractFactory.Trees.IranianTree;
import AbstractFactory.Trees.JapaneseTree;
import org.junit.Test;
import java.lang.ClassCastException;

import static org.junit.Assert.assertEquals;

public class GardenCreatorTest {
    @Test
    public void IranianGardenWithIranianTreesAndFlowers(){
        IranianGardenCreator iranianGardenBuilder = new IranianGardenCreator();

        IranianFlower iranianFlower = (IranianFlower) iranianGardenBuilder.createFlower();
        IranianTree iranianTree = (IranianTree) iranianGardenBuilder.createTree();

        assertEquals("Iranian flower created", iranianFlower.createFlowerResult());
        assertEquals( "Iranian tree created", iranianTree.createTreeResult());

        System.out.println("First test: pass");
    }

    @Test
    public void IranianGardenWithJapaneseTrees(){
        IranianGardenCreator iranianGardenBuilder = new IranianGardenCreator();
        try{
            JapaneseTree japaneseTree = (JapaneseTree) iranianGardenBuilder.createTree();
        } catch (ClassCastException e){
            System.out.println("Japanese trees can't be created by an iranian garden creator");
            return;
        }catch (Exception e){

        }
        System.out.println("Second test: fail");
    }

    @Test
    public void IranianGardenWithJapaneseFlowers(){
        IranianGardenCreator iranianGardenBuilder = new IranianGardenCreator();
        try{
            JapaneseFlower japaneseFlower = (JapaneseFlower) iranianGardenBuilder.createFlower();
        } catch (ClassCastException e){
            System.out.println("Japanese flowers can't be created by an iranian garden creator");
            return;
        }catch (Exception e){

        }
        System.out.println("Third test: fail");
    }

    @Test
    public void JapaneseGardenWithJapaneseTreesAndFlowers(){
        JapaneseGardenCreator japaneseGardenBuilder = new JapaneseGardenCreator();

        JapaneseFlower japaneseFlower = (JapaneseFlower) japaneseGardenBuilder.createFlower();
        JapaneseTree japaneseTree = (JapaneseTree) japaneseGardenBuilder.createTree();

        assertEquals("Japanese flower created", japaneseFlower.createFlowerResult());
        assertEquals("Japanese tree created", japaneseTree.createTreeResult());

        System.out.println("Forth test: pass");
    }

    @Test
    public void JapaneseGardenWithIranianTrees(){
        JapaneseGardenCreator japaneseGardenBuilder = new JapaneseGardenCreator();
        try{
            IranianTree iranianTree = (IranianTree) japaneseGardenBuilder.createTree();
        } catch (ClassCastException e){
            System.out.println("Iranian trees can't be created by a japanese garden creator");
            return;
        }catch (Exception e){

        }
        System.out.println("Fifth test: fail");
    }

    @Test
    public void JapaneseGardenWithIranianFlowers(){
        JapaneseGardenCreator japaneseGardenBuilder = new JapaneseGardenCreator();
        try{
            IranianFlower iranianFlower = (IranianFlower) japaneseGardenBuilder.createFlower();
        } catch (ClassCastException e){
            System.out.println("Iranian flowers can't be created by a japanese garden creator");
            return;
        }catch (Exception e){

        }
        System.out.println("sixth test: fail");
    }
}
