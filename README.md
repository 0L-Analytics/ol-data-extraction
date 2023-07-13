# ol-data-extraction
Extraction tools for 0L-blockchain data

## Prerequisites
- Have docker installed
- Have docker compose installed

## Assumtions
- Should run on Windows machine but has only been tested on Debian Linux

## Services
### Treeview
Generate a json file with format:
```
[{
  account: <address>,
  parent_tree: [<oldest address>, <newest address>] // oldest ancestor first, the PARENT of this account last.
}]
```
#### Steps to run
1. Update *services/treeview/.env* file if needed with olfyi database credentials.
2. From project source directory run `docker compose up -d treeview`
3. When process finished, a json file should appear in the configured directory (default: ./assets).