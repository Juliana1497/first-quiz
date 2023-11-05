package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

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
        //the name of drink converted in a Integer calls price
        Integer price = drinks.get(name);
        if (price == null) {
            throw new UnknownDrinkException();
        }
        if (coins < price) {
            throw new NotEnoughMoneyException();
        }
        coins -= price;
        Drink d = new Drink() {
            @Override
            public String getName() {
                return name;
            }

            @Override
            public boolean isFizzy() {
                return name.equals("ScottCola"); 
            }
        };
        return d;
    }

    public static VendingMachine getInstance() {
        return new VendingMachineImpl();
    }
}
