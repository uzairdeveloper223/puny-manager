from .storage import load_vault
from .i18n import t
from .search import smart_find

def get_entry(master_password: str, name: str) -> dict:
    vault = load_vault(master_password)
    entry = smart_find(vault["entries"], name)

    if not entry:
        raise KeyError(t("entry_not_found", name=name))

    return entry

    raise KeyError(t("entry_not_found", name=name))

