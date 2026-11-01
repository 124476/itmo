public class Prince extends Leader implements Assertable, Reproachable {
    public Prince(String name, double patience) {
        super(name, patience);
    }

    @Override
    public void reactTo(String text) {
        System.out.println(getName() + " хмурится: " + text);
    }

    @Override
    public void assertTo(String text) {
        System.out.println(getName() + " утверждает, что " + text);
    }

    @Override
    public void reproachTo(Person person, String text) {
        System.out.println(getName() + " упрекает " + person.getName() +  ", в том что " + text);
    }
}