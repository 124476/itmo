public class Cook extends Person implements IEscape, IServe {
    private boolean canEscape = false;

    public Cook(String name) {
        super(name);
    }

    public void letEscape() {
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