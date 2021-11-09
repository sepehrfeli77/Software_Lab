package AbstractFactory;

import AbstractFactory.Flowers.IranianFlower;
import AbstractFactory.Flowers.JapaneseFlower;
import AbstractFactory.GardenCreators.IranianGardenCreator;
import AbstractFactory.GardenCreators.JapaneseGardenCreator;
import AbstractFactory.Trees.IranianTree;
import AbstractFactory.Trees.JapaneseTree;

import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        IranianGardenCreator iranianGardenCreator = new IranianGardenCreator();
        JapaneseGardenCreator japaneseGardenCreator = new JapaneseGardenCreator();
        IranianFlower iranianFlower;
        IranianTree iranianTree;
        JapaneseFlower japaneseFlower;
        JapaneseTree japaneseTree;
        boolean isIranian;

        int input;

        firstLoop:
        while(true) {
            setNationality();
            input = scanner.nextInt();
            switch (input) {
                case 1:
                    isIranian = true;
                    break firstLoop;
                case 2:
                    isIranian = false;
                    break firstLoop;
                default:
                    System.out.println("Invalid input");
            }
        }

        while(true) {
            showMenu();
            input = scanner.nextInt();
            switch (input) {
                case 1:
                    if(isIranian) {
                        iranianFlower = (IranianFlower) iranianGardenCreator.createFlower();
                        System.out.println(iranianFlower.createFlowerResult());
                    }
                    else{
                        System.out.println("Iranian flowers can't be created by a japanese garden creator");
                    }
                    break;
                case 2:
                    if(isIranian) {
                        iranianTree = (IranianTree) iranianGardenCreator.createTree();
                        System.out.println(iranianTree.createTreeResult());
                    }
                    else{
                        System.out.println("Iranian trees can't be created by a japanese garden creator");
                    }
                    break;
                case 3:
                    if(isIranian){
                        System.out.println("Japanese flowers can't be created by an iranian garden creator");
                    }
                    else {
                        japaneseFlower = (JapaneseFlower) japaneseGardenCreator.createFlower();
                        System.out.println(japaneseFlower.createFlowerResult());
                    }
                    break;
                case 4:
                    if(isIranian){
                        System.out.println("Japanese flowers can't be created by an iranian garden creator");
                    }
                    else {
                        japaneseTree = (JapaneseTree) japaneseGardenCreator.createTree();
                        System.out.println(japaneseTree.createTreeResult());
                    }
                    break;
                case 5:
                    return;
            }
        }
    }
    public static void showMenu(){
        System.out.println("1. Create Iranian Flower");
        System.out.println("2. Create Iranian Tree");
        System.out.println("3. Create Japanese Flower");
        System.out.println("4. Create Japanese Tree");
        System.out.println("5. END");
        System.out.println("Enter your choice");
    }

    public static void setNationality(){
        System.out.println("Which one?");
        System.out.println("1. Iranian");
        System.out.println("2. Japanese");
    }
}
