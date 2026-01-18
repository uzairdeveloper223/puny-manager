from getpass import getpass
from .storage import load_vault, save_vault
from .i18n import t

def change_master_password() -> None:
    old = getpass(t("master_password"))
    vault = load_vault(old)

    new1 = getpass(t("set_master_password"))
    new2 = getpass(t("repeat_master_password"))

    if new1 != new2:
        raise ValueError(t("password_mismatch"))

    save_vault(new1, vault)