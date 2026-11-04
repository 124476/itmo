public class Main {
    public static void main(String[] args) {
        class Reporter {
            void print(String text) {
                System.out.println("\n=== " + text.toUpperCase() + " ===\n");
            }
        }

        Reporter reporter = new Reporter();

        Duke duke = new Duke("Герцог", 60);
        Prince prince = new Prince("Князь", 60);
        Cook cook = new Cook("Лучший повар");

        reporter.print("Побег повара");

        duke.giveEscape(cook);

        try {
            cook.escape();

            prince.assert_(duke + " дал сбежать " + cook);
            prince.reproach(duke, "нарушил свое слово");

            reporter.print("Война");

            War war = prince.startWar("Травяная война", duke);
            try {
                war.startBattle("Битва на луковой грядке");
                war.startBattle("Сражение у каштанов");
                war.startBattle("Бой за специи");
            } catch (WarEnded e) {
                System.out.println(e.getMessage()); // Кидает ошибку, если война закончилась, а .startBattle еще раз просит
            }

            if (war.getStatus() == WarStatus.END) {
                reporter.print("Праздник");

                Dish dish = Dish.getRandomDish();
                cook.serveDish(dish);

                Person guest = new Person("Иностранный гость") {
                    @Override
                    public void reactTo(String event) {
                        System.out.println(getName() + " удивлен: " + event);
                    }
                };
                guest.reactTo("Герцог оказал должную честь " + dish);

                duke.reactTo(dish + " превосходен");
            }
        } catch (CantEscape e) {
            System.out.println(e.getMessage());
        }
    }
}