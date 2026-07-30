class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        def enqueue(queue: List[int], item: int):
            queue.append(item)

        def peek(queue: List[int]) -> int:
            return queue[0]

        def dequeue(queue: List[int]) -> int:
            if len(queue) == 0:
                return
            item = peek(queue)
            queue[:] = queue[1:]
            return item

        pref_counts = [0, 0]
        for pref in students:
            pref_counts[pref] += 1

        while True:
            student_pref = dequeue(students)
            top_sandwich = peek(sandwiches)
            
            if student_pref == top_sandwich:
                dequeue(sandwiches)
                pref_counts[student_pref] -= 1
            else:
                enqueue(students, student_pref)

            if len(students) == 0:
                break

            if not all(pref_counts):
                if peek(students) != peek(sandwiches):
                    break

        return len(students)


        