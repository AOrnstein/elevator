# Elevator

This program simulates an elavator stopping on multiple floors and calulates the time taken and floors visited.

The executible for Mac is `/dist/elevator`.

The command has two arguments:

1. start - the starting floor number
2. floors - a comma sepperated list of flor numbers to visit (e.g. `1,2,3`)

Example:

```bash
./dist/elevator 12 2,9,1,32
```

The returned values are the time (units undefined) and a ordered list of floors visited.

## Assumptions

- The user has python installed or is using a Mac
- Consecutive stops on the same floor should not be included in the result
- Don't use or only lightly use AI

## Unimplemented Features

- config file or environment variables (the single floor travel time was hardcodes)
- Split into multiple files and rename existing ones
- Test cases (I ran some simple tests but haven't written test cases)
- Build files (currently just executing `pyinstaller --onefile --name "elevator" main.py` and manualy removing most artifacts without any real thought)
- Look at other formatters and documentation styles
