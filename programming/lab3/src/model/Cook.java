public class Cook extends Person implements Escapable, Servable {
    private boolean canEscape = false;

    public Cook(String name) {
        super(name);
    }

    protected void accuseEscape() {
        this.canEscape = true;
    }

    @Override
    public void escape() throws CantEscape {
        if (!this.canEscape) throw new CantEscape(getName());

        System.out.println(getName() + " тайком сбежал");
    }

    @Override
    public void serveDish(Dish dish) {
        System.out.println("На стол подан: " + dish);
    }

    @Override
    public void reactTo(String text) {
        System.out.println(getName() + " реагирует на: " + text);
    }
}