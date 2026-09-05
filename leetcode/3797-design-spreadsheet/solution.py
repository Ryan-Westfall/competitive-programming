class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.spreadsheet[cell] = 0
        
    def getValue(self, formula: str) -> int:
        res = formula.split('+')
        cellA = res[0][1:] if res[0][1:].isdigit() else self.spreadsheet[res[0][1:]]
        cellB = res[1] if res[1].isdigit() else self.spreadsheet[res[1]]
        return int(cellA) + int(cellB)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)