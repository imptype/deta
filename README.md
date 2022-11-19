# deta

An async library to interact with deta.sh base & drive

- [Discord](https://discord.gg/bh99VTt9dH)
- [GitHub](https://github.com/jnsougata)

# Table of Contents
- [deta](#deta)
- [Table of Contents](#table-of-contents)
- [Installing](#installing)
- [Quick Start](#quick-start)
- [Async Context Manager](#async-context-manager)
- [Usage](#usage)
- [Base](#base)
- [Drive](#drive)
- [Records](#records)
- [Queries](#queries)
- [Updates](#updates)

# Installing

**Recommended:** Python 3.8.0 or higher

```shell
pip install git+https://github.com/jnsougata/deta
```

# Quick Start

```python
import asyncio
from deta import Deta, Record


async def main():
    deta = Deta()

    # instantiating a drive
    drive = deta.drive(name='TEST_DRIVE')

    # instantiating a base
    base = deta.base(name='TEST_BASE')

    # storing a json obj to deta base
    await base.put(
      Record(
        {
          'name': 'John Doe', 
          'age': 20
        }, 
        key='xyz', 
        expire_after=100
      )
    )

    # downloading a song stored in deta drive
    resp = await drive.get('song.mp3')
    with open('song.mp3', 'wb') as f:
        f.write(resp.read())

    # closing deta connection
    await deta.close()

    
if __name__ == '__main__':
    asyncio.run(main())
```

# Async Context Manager
```python
async def main():
    async with Deta() as d:
        base = d.base('TEST_BASE')
        print(await base.get())
```

# Usage

# Base
- `put(*records: Record)` 
  - **Returns:** Dict[str, Any]
- `delete(self, *keys: str)` 
  - **Returns:** Optional[List[Dict[str, str]]]
- `get(*keys: str)`
  - **Returns:** List[Dict[str, Any]]
- `insert(*records: Record)`
  - **Returns:** Optional[List[Dict[str, Any]]]
- `update(key: str, updater: Updater)`
  - **Returns:** Dict[str, Any]
- `query(*queries: Query, limit: Optional[int], last: Optional[str])`
  - **Returns:** Dict[str, Any]

# Drive
- `files(limit: int = None, prefix: str = None)`
  - **Returns:** List[Dict[str, Any]]
- `delete(*names: str)`
  - **Returns:** Dict[str, Any]
- `upload(content: [str | bytes], name: str)` 
  - **Returns:** Dict[str, Any]
- `get(name: str)`
  - **Returns:** io.BytesIO"

# Records
- Base class **Record** 
- **Args**:
  - `data: Dict[str, Any]`
- **KwArgs**:
  - `key: Optional[str]`
  - `expire_at: Optional[datetime]`
  - `expire_after: Optional[int]`

# Queries
- Base class **Query**
- Methods:
  - `equal(field: str, value: Any)`
  - `not_equal(field: str, value: Any)`
  - `contains(field: str, value: Any)`
  - `not_contains(field: str, value: Any)`
  - `greater_than(field: str, value: Any)`
  - `greater_equal(field: str, value: Any)`
  - `less_than(field: str, value: Any)`
  - `less_equal(field: str, value: Any)`
  - `prefix(field: str, value: Any)`
  - `range(field: field: str, start: float, end: float)`

# Updates
- Base class **Updater**
  - `set(field: str, value: Any)`
  - `delete(field: str)`
  - `increment(field: str, value: int)`
  - `append(field: str, value: Any)`
  - `prepend(field: str, value: Any)`
