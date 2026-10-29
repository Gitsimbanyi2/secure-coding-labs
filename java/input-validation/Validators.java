package lab.validation;

import java.util.regex.Pattern;

public final class Validators {
    private static final Pattern ACCOUNT = Pattern.compile("^[0-9]{6,12}$");

    private Validators() {}

    public static boolean accountId(String raw) {
        return raw != null && ACCOUNT.matcher(raw).matches();
    }
}
