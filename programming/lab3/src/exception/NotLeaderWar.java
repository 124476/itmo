public class NotLeaderWar extends Exception {
    private String personName;

    public NotLeaderWar(String personName) {
        super("Персонаж не является лидером!");
        this.personName = personName;
    }

    @Override
    public String getMessage() {
        return "Ошибка: " + personName + " не может начать войну, так как он не Leader!";
    }
}