public class BrokenOathException extends Exception {
    private String personName;

    public BrokenOathException(String personName) {
        super("Персонаж нарушил слово!");
        this.personName = personName;
    }

    @Override
    public String getMessage() {
        return "Ошибка: " + personName + " нарушил свое слово!";
    }
}