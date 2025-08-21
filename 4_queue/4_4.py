class PrintQueue:
    def __init__(self):
        self.queue = []

    def add(self, job):
        self.queue.append(job)

    def remove(self):
        return self.queue.pop(0) if self.queue else None

    def peek(self):
        return self.queue[0] if self.queue else None

    def count(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)


class OutputTray:
    def __init__(self):
        self.stack = []

    def drop(self, doc):
        self.stack.append(doc)

    def pick(self):
        return self.stack.pop() if self.stack else None

    def has_document(self):
        return len(self.stack) > 0


class JobCommand:
    def __init__(self, op_code, timestamp, content=""):
        self.op = op_code
        self.time = int(timestamp)
        self.content = content


# รับ input
inputs = input("Enter input: ").split(", ")
schedule = PrintQueue()

# แปลงคำสั่งเป็น JobCommand
for entry in inputs:
    first, *rest = entry.split(" ", 1)
    command_type, timestamp = first.split(":")
    content = rest[0] if rest else ""
    schedule.add(JobCommand(command_type, timestamp, content))

# ตัวแปรควบคุมเครื่องพิมพ์
printer_queue = PrintQueue()
tray = OutputTray()
active_job = None
job_data = ""
buffering = ""
paper_left = 3
current_time = 0

# วนจำลองเวลา
while not schedule.is_empty() or active_job:
    # กำลังพิมพ์
    if active_job:
        if paper_left > 0:
            buffering += job_data[:5]
            job_data = job_data[5:]
            if job_data == "":
                paper_left -= 1
                tray.drop(active_job)
                active_job = None
                buffering = ""
        else:
            print(f"[Time {current_time}] Error: Printer is out of paper. Please refill.")

    # ถ้าไม่มีงานอยู่ตอนนี้ → ดึงจาก queue
    if not printer_queue.is_empty() and active_job is None:
        if paper_left == 0:
            print(f"[Time {current_time}] Error: Printer is out of paper. Please refill.")
        else:
            active_job = job_data = printer_queue.remove()

    # ประมวลผลคำสั่งที่เวลานี้
    while not schedule.is_empty() and schedule.peek().time == current_time:
        cmd = schedule.remove()

        if cmd.op == "P":
            if printer_queue.count() < 3:
                printer_queue.add(cmd.content)
                if active_job is None and paper_left > 0:
                    active_job = job_data = printer_queue.remove()
                if paper_left == 0:
                    print(f"[Time {current_time}] Error: Printer is out of paper. Please refill.")
            else:
                print(f"[Time {current_time}] Error: Printer buffer is full. Please try again later.")

        elif cmd.op == "S":
            if active_job:
                print(f'[Time {current_time}] Status: Printing... "{active_job}" and Pending {printer_queue.count()} file(s) in queue.')
            else:
                print(f'[Time {current_time}] Status: Idle. Pending {printer_queue.count()} file(s) in queue.')

        elif cmd.op == "R":
            paper_left += int(cmd.content)
            if active_job is None and not printer_queue.is_empty():
                active_job = job_data = printer_queue.remove()

        elif cmd.op == "T":
            if not tray.has_document():
                print(f"[Time {current_time}] You got: Nothing in tray.")
            else:
                print(f"[Time {current_time}] You got: ", end="")
                result = []
                while tray.has_document():
                    result.append(f'"{tray.pick()}"')
                print(", ".join(result))

    current_time += 1