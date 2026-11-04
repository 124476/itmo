public class Prince extends Leader implements IAssert, IReproach {
    public Prince(String name, double patience) {
        super(name, patience);
    }

    @Override
    public void reactTo(String text) {
        System.out.println(getName() + " хмурится: " + text);
    }

    @Override
    public void assert_(String text) {
        System.out.println(getName() + " утверждает, что " + text);
    }

    @Override
    public void reproach(Person person, String text) {
        System.out.println(getName() + " упрекает " + person +  ", в том что " + text);
    }
}