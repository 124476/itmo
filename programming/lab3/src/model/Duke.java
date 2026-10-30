public class Duke extends Leader {
    public Duke(String name, double patience) {
        super(name, patience);
    }

    @Override
    public void reactTo(String event) {
        System.out.println(getName() + " (Герцог) важно кивает: " + event);
    }
}