package org.velezreyes.quiz.question6;

public class VendingMachineImpl{

  public static VendingMachine getInstance() {
      
      VendingMachine vm = new VendingMachine() {
          @Override
          public void insertQuarter() {
          }

          @Override
          public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
              Drink d = new Drink() {
                  @Override
                  public String getName() {
                      String name = "ScottCola";
                      return name;
                  }

                  @Override
                  public boolean isFizzy() {
                      boolean ban = true;
                      return ban;
                  }
              };
              if (name.equals("BessieBooze")) {
                  throw new UnknownDrinkException();
              }
              return d;
          };
      };
      
    return vm;
  }
}
