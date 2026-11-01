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
        logger.log(attacker.getName() + " объявил войну " + defenser.getName() + "!");
    }

    public void startBattle(String location) {
        if (warStatus == WarStatus.END) {
            throw new WarEnded(this.name);
        }

        logger.log("Произошло сражение: " + location);

        double damage = Math.random() * 40;
        defenser.decreasePatience(damage);

        if (defenser.getPatience() <= 0) {
            logger.log(defenser.getName() + " больше не может терпеть поражения!");

            try {
                Contract peaceTreaty = new Contract("Паштетный мир", defenser, attacker);
                defenser.endWar(peaceTreaty, attacker);
            } catch (NotHaveWar e) {
                System.out.println(e.getMessage());
            }

            return;
        }

        damage = Math.random() * 40;
        attacker.decreasePatience(damage);

        if (attacker.getPatience() <= 0) {
            logger.log(attacker.getName() + " больше не может терпеть поражения!");

            try {
                Contract peaceTreaty = new Contract("Паштетный мир", attacker, defenser);
                attacker.endWar(peaceTreaty, defenser);
            } catch (NotHaveWar e) {
                System.out.println(e.getMessage());
            }

            return;
        }
    }

    public void makePeace(Contract contract) {
        if (this.warStatus == WarStatus.END) throw new WarEnded(this.name);

        this.warStatus = WarStatus.END;
        logger.log("Война окончена!");
        logger.log("Заключен " + contract.name() + " между " + contract.signer1().getName() + " и " + contract.signer2().getName());
    }

    public boolean equalsWar(Leader attacker, Leader defenser) {
        return this.attacker == attacker && this.defenser == defenser|| this.defenser == attacker && this.attacker == defenser;
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