public class WarEnded extends RuntimeException {
    public WarEnded(String warName) {
        super("Война уже окончена: " + warName);
    }

    @Override
    public String getMessage() {
        return "Действие невозможно. " + super.getMessage();
    }
}