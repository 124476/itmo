public class Prince extends Leader {
    public Prince(String name, double patience) {
        super(name, patience);
    }

    @Override
    public void reactTo(String event) {
        System.out.println(getName() + " (Князь) хмурится: " + event);
    }
}