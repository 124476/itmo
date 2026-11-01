public class NotHaveWar extends Exception {
    public String attackerName;
    public String defenserName;

    public NotHaveWar(String attackerName, String defenserName) {
        super("Персонаж не может завершить войну");
        this.attackerName = attackerName;
        this.defenserName = defenserName;
    }

    @Override
    public String getMessage() {
        return "Ошибка: " + attackerName + " не ведет войну с " + defenserName;
    }
}