# Absentee-List

A windows(64 Bit) application to compile a list of absentees from an online meeting.

## How to run
1. Create a new folder in a comfortable and easily accessible location on your computer
2. Download [main.exe](https://drive.google.com/file/d/1M4k3AcZ0eA_uZTltdSvWtD0x673nGHvE/view?usp=sharing) File and move it to the Newly created folder.
3. Run the `main.exe` file.
4. See [below](#Commands) for the list of commands


## How to run (advanced users) (PRO)
1. Clone this git repo: `git clone https://github.com/DevHyperCoder/Absentee-List.git`
2. Create and activate a virtual environment
3. Install the python packages: `pip install -r requirements.txt`
4. Run the `main.py` file `python main.py <CLASS-NAME>`
5. See [below](#Commands) for the list of commands

## Commands

Enter the name of the class when prompted

(FOR PRO): If `CLASS-NAME` is not specified (as a argument) then it should prompt you to enter the class name.

`help` : Should give a guide for how the files are supposed to be named!

## File Structure

The excel files should be in the same folder the `main.exe` or (PRO)`main.py` is present.

The master list (containing the list of all the students) should be named like this: `<CLASS-NAME>_Master.xlsx` For eg, `XA_Master.xlsx`

The current attendance list should be named like this: `<CLASS-NAME>.xlsx` For eg, `XA.xlsx`

## Excel file structure

The master list should have `name` at `A1` ie the top-left most column.

The current attendance list file should be in `xlsx` and NOT in `.csv`

## Output

The program should output the list of absentees like this:

```
Absent List: ['a', 'b', 'c']
```

Also a new excel file (`<CLASS-NAME>_ABSENT.xlsx`) would be created

## Contribution
Pull Requests and Issues are appreciated 😇 

## License
© DevHyperCoder
[MIT License](LICENSE)
