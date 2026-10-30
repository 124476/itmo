public class Cook extends Person {
    public Cook(String name) {
        super(name);
    }

    public void escape() {
        System.out.println("[СЮЖЕТ] " + getName() + " тайком сбежал, чтобы не потерять место!");
    }

    public Dish serveDish() {
        return new Dish("Паштет-сюзерен", 100);
    }

    @Override
    public void reactTo(String event) {
        System.out.println(getName() + " (Повар) реагирует на: " + event);
    }
}