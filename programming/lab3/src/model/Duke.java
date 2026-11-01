public class Duke extends Leader implements GiveEscapable {
    public Duke(String name, double patience) {
        super(name, patience);
    }

    @Override
    public void giveEscape(Person person) {
        if (person instanceof Cook c) {
            if (Math.random() > 0.3) {
                c.accuseEscape();

                System.out.println(getName() + " дал тайно сбежать " + c.getName());
            } else {
                System.out.println(getName() + " не дал возможности сбежать " + c.getName());
            }
        }
    }

    @Override
    public void reactTo(String text) {
        System.out.println(getName() + " важно кивает: " + text);
    }
}