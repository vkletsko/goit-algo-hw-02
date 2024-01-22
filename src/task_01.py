from queue import Queue
import time
import uuid

queue = Queue()


def generate_request():
    task_uuid = uuid.uuid4()
    queue.put(task_uuid)


def process_request():
    if not queue.empty():
        item = queue.get()
        print(f"Processing task {item}")
        time.sleep(1)
        print(f"Processed task {item}")
        time.sleep(1)
        queue.task_done()
    else:
        print("Queue is empty")


if __name__ == "__main__":
    try:
        input("Press Enter to run tasks processing: ")

        while True:
            generate_request()
            process_request()

    except KeyboardInterrupt as err:
        print(err)
    except ValueError as err:
        print(err)
