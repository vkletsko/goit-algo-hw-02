from queue import Queue
import time

queue = Queue()


def generate_request(request):
    queue.put(request)


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


def main():
    while True:
        task_name = input("Enter a task: ")

        if task_name in ["bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            generate_request(task_name)
            process_request()


if __name__ == "__main__":
    main()
