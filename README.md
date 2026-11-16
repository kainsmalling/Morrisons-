# Morrisons barcodes

Searchable barcode sheet for a Home Assistant tablet. Search, tap a card, scan the big barcode with the Morrisons app.

- `items.json` – the data (edit/extend this; Claude updates it from receipts)
- `build.py` + `template.html` – generate `index.html` (`python3 build.py`)
- `index.html` – the finished page (self-contained, works offline, light/dark follows the system)

## Home Assistant setup (Terminal add-on, no cost)

1. Open the Terminal add-on and run:
   ```
   cd /config/www
   git clone -b claude/receipt-item-barcodes-z0vq7i https://github.com/kainsmalling/Morrisons-.git morrisons
   ```
   The page is now at `http://<your-HA>:8123/local/morrisons/index.html`
   (if `/config/www` didn't exist before, restart Home Assistant once).
2. Dashboard: edit a view -> set it to **Panel (1 card)** -> add a **Webpage** card with URL `/local/morrisons/index.html`.
3. Auto-update every 30 min. In `configuration.yaml`:
   ```yaml
   shell_command:
     morrisons_pull: "git -C /config/www/morrisons pull --ff-only"
   ```
   Restart HA, then add an automation:
   ```yaml
   alias: Update Morrisons barcodes
   trigger:
     - platform: time_pattern
       minutes: "/30"
   action:
     - service: shell_command.morrisons_pull
   ```
4. After a pull, refresh the tablet dashboard to see changes.

Don't use the official "Git pull" add-on for this: it syncs the repo into your whole `/config` folder.
