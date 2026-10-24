import time
import threading


class TaskManager:

    def __init__(self, engine):
        self.engine = engine
        self.tasks = []
        self.running = False
        self.thread = None
        self.current_index = 0

    def set_tasks(self, tasks):
        self.tasks = tasks or []
        self.current_index = 0

    def start(self):
        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._loop,
            daemon=True
        )

        self.thread.start()

    def stop(self):
        self.running = False

    def _loop(self):

        while self.running:

            if not self.tasks:
                time.sleep(self.engine.task_delay)
                continue

            executed = False

            task_count = len(self.tasks)

            for _ in range(task_count):

                if not self.running:
                    break

                task = self.tasks[
                    self.current_index % task_count
                ]

                self.current_index = (
                    self.current_index + 1
                ) % task_count

                try:

                    if task.is_ready():

                        task.run()
                        executed = True

                        time.sleep(
                            self.engine.task_delay
                        )

                        break

                except Exception as exc:

                    self.engine.handle_error(
                        task,
                        exc
                    )

                    time.sleep(
                        self.engine.task_delay
                    )

            if not executed:

                time.sleep(
                    self.engine.task_delay
                )