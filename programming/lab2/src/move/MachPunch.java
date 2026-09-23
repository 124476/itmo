package move;

import pokemon.*;
import ru.ifmo.se.pokemon.*;

public class MachPunch extends PhysicalMove {
    public MachPunch() {
        super(Type.FIGHTING, 40, 100, 1, 1);
    }

    @Override
    public String describe() {
        return "использует Mach Punch";
    }
}
