public class CantEscape extends Exception {
    private String personName;

    public CantEscape(String personName) {
        super("Персонаж не может сбежать");
        this.personName = personName;
    }

    @Override
    public String getMessage() {
        return "Ошибка: " + personName + " не может сбежать, так как ему не разрешили";
    }
}