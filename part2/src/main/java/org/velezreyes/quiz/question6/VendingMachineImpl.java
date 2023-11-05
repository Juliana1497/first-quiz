package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

//implement the methods of class VendingMachine
public class VendingMachineImpl implements VendingMachine {
    private int coins;
    private final Map<String, Integer> drinks;
    
    //constructor
    public VendingMachineImpl() {
        this.coins = 0;
        this.drinks = new HashMap<>();
        // Initialize the available drinks and their prices in the Vending Machine
        drinks.put("ScottCola", 75);
        drinks.put("KarenTea", 100);
    }

    @Override
    public void insertQuarter() {
        //each quarter of coins is = 25
        coins += 25;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        //the name of the drink converted to an Integer called price
        Integer price = drinks.get(name);
        if (price == null) {
            throw new UnknownDrinkException();
        }
        if (coins < price) {
            throw new NotEnoughMoneyException();
        }
        //name are subtracted for the machineResets exception to work
        coins -= price;
        Drink d = new Drink() {
            @Override
            public String getName() {
                return name;
            }

            @Override
            public boolean isFizzy() {
                //since by default it is false, only the case in which it returns true is set
                return name.equals("ScottCola"); 
            }
        };
        return d;
    }

    public static VendingMachine getInstance() {
        //returns the class that implements the interface VendingMachine
        return new VendingMachineImpl();
    }
}
