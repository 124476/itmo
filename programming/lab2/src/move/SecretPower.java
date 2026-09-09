package move;

import ru.ifmo.se.pokemon.*;
import pokemon.*;

public class SecretPower extends PhysicalMove {
    public SecretPower() {
        super(Type.PSYCHIC, 70, 100);
    }

    @Override public String describe() {
        return "использует Secret Power";
    }
}