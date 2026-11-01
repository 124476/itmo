import java.util.Objects;

public abstract class Person {
    private String name;

    public Person(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public abstract void reactTo(String text);

    @Override
    public String toString() {
        return this.name;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;

        return Objects.equals(this.name, person.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name);
    }
}