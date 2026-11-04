import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class War {
    private String name;
    private Leader attacker;
    private Leader defenser;
    private WarStatus warStatus;

    class WarLog {
        void log(String message) {
            System.out.println("[" + War.this.name + "] " + message);
        }
    }
    WarLog logger = new WarLog();

    public War(String name, Leader attacker, Leader defenser) {
        this.name = name;
        this.warStatus = WarStatus.WAR;
        this.attacker = attacker;
        this.defenser = defenser;

        attacker.addWar(this);
        defenser.addWar(this);
        logger.log(attacker + " объявил войну " + defenser + "!");
    }

    public void endWar() {
        warStatus = WarStatus.END;

        attacker.removeWar(this);
        defenser.removeWar(this);

        logger.log(name + " закончена");
    }

    private boolean attackPerson(IBattle leader) {
        double damage = Math.random() * 30;
        leader.takeDamage(damage);

        if (leader.getPatience() <= 0) {
            logger.log(leader + " больше не может терпеть поражения!");

            Contract contract = leader.endWar(this, "Паштетный мир");
            logger.log("Заключен " + contract.name());
            return true;
        }

        return false;
    }

    public void startBattle(String location) {
        if (warStatus == WarStatus.END) {
            throw new WarEnded(this.name);
        }

        logger.log("Произошло сражение: " + location);

        if (attackPerson(defenser)) return;
        attackPerson(attacker);
    }

    public WarStatus getStatus() {
        return this.warStatus;
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, attacker, defenser, warStatus);
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        War war = (War) o;

        return Objects.equals(name, war.name) &&
                Objects.equals(attacker, war.attacker) &&
                Objects.equals(defenser, war.defenser);
    }

    @Override
    public String toString() {
        return this.name + " между " + this.attacker + " " + this.defenser;
    }
}