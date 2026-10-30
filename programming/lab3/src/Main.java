public class Main {
    public static void main(String[] args) {
        Leader duke = new Duke("Герцог", 100);
        Leader prince = new Prince("Князь", 60);
        Cook cook = new Cook("Повар карлик");

        cook.escape();

        try {
            prince.accuse(duke, "дал повару сбежать и нарушил слово!");
        } catch (BrokenOathException e) {
            System.out.println("ВСПЫШКА КОНФЛИКТА: " + e.getMessage());
        }

        try {
            duke.startWar("Ошибочная война", cook);
        } catch (NotLeaderWar e) {
            System.out.println("ПРЕДОТВРАЩЕНА ОШИБКА: " + e.getMessage());
        }

        try {
            War war = prince.startWar("Травяная война", duke);

            war.giveBattle("Битва на луковой грядке");
            war.giveBattle("Сражение у каштанов");
            war.giveBattle("Бой за специи");

            Contract peaceTreaty = new Contract("Паштетный мир", prince, duke);
            war.makePeace(peaceTreaty);

            System.out.println("\n--- Праздник примирения ---");
            Dish dish = cook.serveDish();
            System.out.println("На стол подан: " + dish.name());

            Person guest = new Person("Иностранный гость") {
                @Override
                public void reactTo(String event) {
                    System.out.println(getName() + " удивлен: " + event);
                }
            };
            guest.reactTo("Герцог оказал должную честь паштету!");

            duke.reactTo("Паштет-сюзерен превосходен!");

            war.giveBattle("Запоздалая битва");

        } catch (NotLeaderWar e) {
            System.out.println(e.getMessage());
        } catch (WarEnded e) {
            System.out.println("\nОШИБКА: " + e.getMessage());
        }
    }
}