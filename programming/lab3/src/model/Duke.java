public class Duke extends Leader implements IGiveEscape {
    public Duke(String name, double patience) {
        super(name, patience);
    }

    @Override
    public void giveEscape(IEscape person) {
        if (Math.random() > 0.3) {
            person.letEscape();

            System.out.println(getName() + " дал тайно сбежать " + person);
        } else {
            System.out.println(getName() + " не дал возможности сбежать " + person);
        }
    }

    @Override
    public void reactTo(String text) {
        System.out.println(getName() + " важно кивает: " + text);
    }
}