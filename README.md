````md
# MySQL to PostgreSQL Migration

A Python-based migration project to move data from one MySQL source database into multiple PostgreSQL target databases.

The project supports:

- Multiple environments: `dev`, `qa`, `prod`
- State-based configuration
- One MySQL source database
- Multiple PostgreSQL target databases
- Common table mapping
- Environment-specific database names
- Logs separated by environment and state

```

Database names are configured manually per environment and state.
No database naming pattern is assumed.

## Setup

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment file:

```bash
cp .env.example .env
```

Update `.env` with your local credentials.

## Environment Variables

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=migration_user
MYSQL_PASSWORD=change_me

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=change_me
```

## Run Migration

Run all modules for one state and environment:

```bash
python main.py --state ld --env dev
```

Run one module:

```bash
python main.py --state ld --env dev --module billing
```

Run one table:

```bash
python main.py --state ld --env dev --module billing --table bill_master
```

Dry run without moving data:

```bash
python main.py --state ld --env dev --dry-run
```

## Supported Environments

```text
dev
qa
prod
```

## Notes

* Do not store real passwords in config files.
* Use `.env` for credentials.
* Keep table mappings common when possible.
* Keep database names environment-specific.
* Validate row counts after every table migration.
* Review logs after every migration run.

```
```

