public enum Dish {
    PATE("Паштет-сюзерен"),
    PIZZA("Пицца пеперони"),
    PIE("Яблочный пирог");

    private final String name;
    Dish(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return this.name;
    }

    public static Dish getRandomDish() {
        Dish[] dishes = values();
        int randomIndex = (int)(Math.random() * dishes.length);
        return dishes[randomIndex];
    }
}