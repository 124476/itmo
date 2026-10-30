import java.util.ArrayList;
import java.util.List;

public class War {
    private String name;
    private Leader attacker;
    private Leader defenser;
    private WarStatus warStatus;
    private List<String> battlesHistory = new ArrayList<>();

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
        logger.log(attacker.getName() + " объявил войну " + defenser.getName() + "!");
    }

    public void giveBattle(String location) {
        if (warStatus == WarStatus.END) {
            throw new WarEnded(this.name);
        }

        logger.log("Произошло сражение: " + location);
        battlesHistory.add(location);

        double damage = Math.random() * 40;
        defenser.decreasePatience(damage);

        if (defenser.getPatience() <= 0) {
            logger.log(defenser.getName() + " больше не может терпеть поражения!");
        }
    }

    public void makePeace(Contract contract) {
        this.warStatus = WarStatus.END;
        logger.log("Война окончена!");
        logger.log("Заключен " + contract.name() + " между " + contract.signer1().getName() + " и " + contract.signer2().getName());
        System.out.println("История сражений (" + battlesHistory.size() + " шт.): " + battlesHistory);
    }
}