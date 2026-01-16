from .storage import load_vault, save_vault

def remove_entry(master_password: str, name: str) -> None:
    vault = load_vault(master_password)

    entries = vault["entries"]
    new_entries = [e for e in entries if e["name"] != name]

    if len(new_entries) == len(entries):
        raise KeyError(f"Eintrag '{name}' nicht gefunden.")

    vault["entries"] = new_entries
    save_vault(master_password, vault)
