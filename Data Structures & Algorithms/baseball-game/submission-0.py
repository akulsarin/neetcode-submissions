class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i, op in enumerate(operations):
            if op == "+":
                op_1 = record.pop()
                op_2 = record[-1]
                record.append(op_1)
                record.append(op_1 + op_2)
            elif op == "D":
                record.append(2 * record[-1])
            elif op == "C":
                record.pop()
            else:
                op_1 = int(op)
                record.append(op_1)
        return sum(record)



        